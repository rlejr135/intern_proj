#-*- coding:utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import _pickle as pickle
#import connection


# output data to file
# recommend True
file_output = True

# chrome browser headless
# recommend False
headless = False

# crawl all festival data. if it is false, find three festival data only
# recommend False
ALL_data = False

# crawl data by three categories. if it is false, user must input data
crawl_alldata = False

#if it is true, find all region in region_data
find_all_region = True
festival_region = '충남'

region_data = {
    "서울": "1", '부산': '6', '대구': '4', '인천': '2', '광주': '5', '대전': '3', '울산': '7', '세종': '8',
    '경기': '31', '강원': '32', '충북': '33', '충남': '34', '경북': '35', '경남': '36', '전북': '37', '전남': '38',
    '제주': '39'
}
# order by
if crawl_alldata is False:
    while True:
        print("1 : 최신순, 2 : 거리순, 3 : 인기순")
        order_type = input()
        if order_type.isdigit() is False:
            continue
        if int(order_type) > 4 or int(order_type) < 1:
            continue
        break

iter_num = 0

for k in region_data.keys():
    if find_all_region is True:
        festival_region = k
    where = festival_region

    iter_num = 0
    while iter_num < 3:
        iter_num += 1
        if crawl_alldata is True:
            order_type = str(iter_num)

        # where

        '''		
        while True:
            print("지역 입력")
            where = input()
        
            if where in region_data:
                break
            print("지역 없음. ex) 서울 / 부산 / 대전")
        '''



        # open chrome browser
        ch_op = webdriver.ChromeOptions()
        if headless == True:
            ch_op.add_argument('headless')
            ch_op.add_argument('--disable-gpu')
        ch_op.add_argument('window-size=1600x900')
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=ch_op)
        driver.get('https://korean.visitkorea.or.kr/list/fes_list.do')
        driver.implicitly_wait(5)

        html = driver.page_source




        # where to go
        driver.find_element_by_xpath('//*[@id="' + region_data.get(where) + '"]/button').click()


        # order by recent/ popular/ distance
        goto_popular = driver.find_elements_by_xpath('//*[@id="' + order_type + '"]')
        for find in goto_popular:
            if find.text == '인기순' or find.text == '거리순' or find.text == '최신순':
                find.click()
                break




        # crawl data start
        festival_num = 0
        save_data = []


        # at start, page is 1
        for pg_num in range(2, 500):
            #for synchronization
            sleep(1.9)

            # find all content and extract proceeding festival
            for i in range(1 ,11):
                notice = driver.find_elements_by_xpath('//*[@id="contents"]/div[2]/div[1]/ul/li[' + str(i) + ']')
                if len(str(notice)) <= 1:
                    break

                saved_notice = notice
                for n in saved_notice:
                    string = n.text.split('\n')

                    # if festival is now proceeding, crawl data
                    if string[0] == "진행중" or string[0] == '상시':
                        driver.find_element_by_xpath('    // *[ @ id = "contents"] / div[2] / div[1] / ul / li[' + str(i) + '] / div[2] / div / a ').click()
                        content = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[2]/div[2]/div/div/ul')
                        fest_name = driver.find_element_by_xpath('// *[ @ id = "contents"] / div[2] / h2')

                        festival_name = fest_name.text
                        todo_save = content.text.split('\n')

                        save_content = {}
                        save_content["title"] = festival_name
                        if "시작일" in todo_save:
                            save_content["start"] = todo_save[todo_save.index("시작일") + 1]
                        if "종료일" in todo_save:
                            save_content["finish"] = todo_save[todo_save.index("종료일") + 1]
                        if "전화번호" in todo_save:
                           save_content["number"] = todo_save[todo_save.index("전화번호") + 1]
                        if "주소" in todo_save:
                            save_content["address"] = todo_save[todo_save.index("주소") + 1]
                        #save_content["start"] = todo_save[todo_save.index("시작일") + 1]

                        save_content["img"] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div[1]/ul/li[1]/button/img').get_attribute('src')


                        tag = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[2]/div[3]/div')
                        save_content["tag"] = tag.text
                        # save data
                        save_data.append(save_content)



                        festival_num += 1

                        # go back
                        driver.back()


                    # if finish, break
                    if festival_num >= 3 and ALL_data is False:
                        break

                    sleep(0.25)

                if festival_num >= 3 and ALL_data is False:
                    break

            if festival_num >= 3 and ALL_data is False:
                break


            # find data at next page
            todo = driver.find_elements_by_xpath('//*[@id="'+ str(pg_num) +'"]')

            #goto next page. if not, break
            flag = False
            if len(todo) <= 2:
                break
            for n in todo:
                if n.text.isdigit() or n.text == '다음':
                    flag = True
                    n.click()

            if flag == False:
                break

        # exit driver
        driver.quit()



        # save data as file
        if file_output is True:
            f = open("save_data/" + region_data.get(where) + '_'+order_type+".txt", 'w')
            # print result
            for k in save_data:
                f.write(str(k) + '\n')

            f.close()
        else:
            for k in save_data:
                print(k)

        if crawl_alldata is False:
            break
    if find_all_region is False:
        break
#######################################  connection to server

#connection.connection_start(save_data)


