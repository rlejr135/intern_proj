
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta

#today = date.today()
yesterday = date.today() - timedelta(1)
#2day = date.today() - timedelta(2)

f = open('weather_day_text.txt', 'w') # 파일 열기



#print(today.strftime('%Y%m%d'))
#print(yesterday.strftime('%Y%m%d'))


driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe') # ..뒤로가기 .현재위치 /들어가기
#driver.get('https://data.kma.go.kr/apiData/getData?type=xml&dataCd=ASOS&dateCd=HR&startDt='+ str(yesterday.strftime('%Y%m%d')) +'&startHh=09&endDt='+ str(yesterday.strftime('%Y%m%d')) +'&endHh=18&stnIds=108&schListCnt=10&pageIndex=1&apiKey=NRJXE%2B%2B7roU76xD0sZxoQPzHvM8u4YgO9d1jJ8IU0oSOtHx1d7tWmIoY%2BHAp56HG')
#driver.get('https://data.kma.go.kr/apiData/getData?type=xml&dataCd=ASOS&dateCd=HR&startDt='+ str(today.strftime('%Y%m%d')) +'&startHh=09&endDt='+ str(today.strftime('%Y%m%d')) +'&endHh=18&stnIds=108&schListCnt=10&pageIndex=1&apiKey=NRJXE%2B%2B7roU76xD0sZxoQPzHvM8u4YgO9d1jJ8IU0oSOtHx1d7tWmIoY%2BHAp56HG')
driver.get('https://data.kma.go.kr/apiData/getData?type=xml&dataCd=ASOS&dateCd=DAY&startDt='+ str(yesterday.strftime('%Y%m%d')) +'&endDt='+ str(yesterday.strftime('%Y%m%d')) +'&stnIds=108&schListCnt=10&pageIndex=1&apiKey=NRJXE%2B%2B7roU76xD0sZxoQPzHvM8u4YgO9d1jJ8IU0oSOtHx1d7tWmIoY%2BHAp56HG')

#for i in range(1,3):
#    driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
#    driver.get('https://data.kma.go.kr/apiData/getData?type=xml&dataCd=ASOS&dateCd=HR&startDt=2011012'+ str(i) +'&startHh=09&endDt=2011012'+ str(i+1) +'&endHh=04&stnIds=108&schListCnt=10&pageIndex=1&apiKey=NRJXE%2B%2B7roU76xD0sZxoQPzHvM8u4YgO9d1jJ8IU0oSOtHx1d7tWmIoY%2BHAp56HG')



#addr = str('#webkit-xml-viewer-source-xml > asostime > info:nth-child(' + str(i+3) + ') > TA')
#addr = str('#collapsible' + str(i) + '> div.expanded > div.collapsible-content > div:nth-child(38) > span.text')
#addr = str('#collapsible' + str(i+1) + ' > div.expanded > div.collapsible-content > div:nth-child(38) > span.text')
#addr = str('#collapsible'+ str(i+1) +' > div.expanded > div.collapsible-content > div:nth-child(14) > span.text')
#tmp = driver.find_element_by_css_selector(addr)


tmp = driver.find_element_by_xpath('//*[@id="collapsible1"]')



item = tmp.text.split('\n')


for iii in item:
        if "<MAX_TA>" in iii:
            newiii = iii.replace("<MAX_TA>", "")
            supernewiii = newiii.replace("</MAX_TA>","")
            #print(supernewiii)
            #print(supernewiii, file=f) #최고기온
                

for jjj in item:
        if "<MIN_TA>" in jjj:
            newjjj = jjj.replace("<MIN_TA>","")
            supernewjjj = newjjj.replace("</MIN_TA>","")
            #print(supernewjjj)
            #print(supernewjjj, file=f) #최저기온

for kkk in item:
        if "<AVG_RHM>" in kkk:
            newkkk = kkk.replace("<AVG_RHM>","")
            supernewkkk = newkkk.replace("</AVG_RHM>","")
            #print(supernewkkk)
            #print(supernewkkk, file=f) #평균 상대습도

flag = False
for lll in item:
        if "<SUM_RN>" in lll:
            newlll = lll.replace("<SUM_RN>","")
            supernewlll = newlll.replace("</SUM_RN>","")
            #print(supernewlll)
            #print('\n')
            #print(supernewlll, file=f) #일강수량
            #print('\n', file=f)
                
            flag = True

if flag is False:
    supernewlll = 0
    #print(supernewlll)
    #print('\n')
    #print(supernewlll, file=f)
    #print('\n', file=f)

print(supernewiii, supernewjjj, supernewkkk, supernewlll)
print(supernewiii, supernewjjj, supernewkkk, supernewlll, file=f) #최고기온 최저기온 상대습도 일강수량
               
#            if "<RN>" not in kkk:
#                print('0')
#                print('\n')

f.close()                
driver.quit()
#driver.quit()





#collapsible1 > div.expanded > div.collapsible-content > div:nth-child(38) > span.text
#collapsible1 > div.expanded > div.collapsible-content > div:nth-child(38) > span.text
#webkit-xml-viewer-source-xml > asostime > info:nth-child(4) > TA
#webkit-xml-viewer-source-xml > asostime > info:nth-child(5) > TA
