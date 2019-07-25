#-*- coding:utf-8 -*-

import _pickle as pickle
import connection

def open_navi(where, order_type):

    now_num = 0

    f = open("save_data/" + where + '_' + order_type + ".txt", 'r')
    # print result

    save_data = ''
    lines = f.readlines()
    for line in lines :
        if now_num >= len(lines):
            break
        now_num += 1
        line = line.replace('\n','')
        #save_data.append(line)
        save_data += line
        if now_num is not len(lines):
            save_data += ' //// '


    connection.connection_start(save_data)
    #print(save_data)


    f.close()




