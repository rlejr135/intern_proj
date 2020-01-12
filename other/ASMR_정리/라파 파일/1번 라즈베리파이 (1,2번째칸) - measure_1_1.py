#! /usr/bin/python0

import time
import sys
from multiprocessing import Process, Value, Lock
import os
import signal
import subprocess
import socket


HOST = ''
PORT = 49007

EMULATE_HX711=False



percentage_weight=0

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():

    if not EMULATE_HX711:
        GPIO.cleanup()

    print "Bye!"
    sys.exit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)




def enough_state(LED_BLUE, LED_RED, LED_GREEN):
    GPIO.output(LED_BLUE,True)
    GPIO.output(LED_RED,False)
    GPIO.output(LED_GREEN,False)

def warning_state(LED_BLUE, LED_RED, LED_GREEN):
    GPIO.output(LED_BLUE,False)
    GPIO.output(LED_RED,True)
    GPIO.output(LED_GREEN,True)

def none_material(LED_BLUE, LED_RED, LED_GREEN):
    GPIO.output(LED_BLUE,True)
    GPIO.output(LED_RED,True)
    GPIO.output(LED_GREEN,True)

def insufficient_state(LED_BLUE, LED_RED, LED_GREEN):
    GPIO.output(LED_BLUE,False)
    GPIO.output(LED_RED,True)
    GPIO.output(LED_GREEN,False)

def taring_scale(b,r,g):
    hx1.tare()
    hx2.tare()
    hx3.tare()
    hx4.tare()
    none_material(b,r,g)
    time.sleep(0.5)
    GPIO.output(b,False)
    GPIO.output(r,False)
    GPIO.output(g,False)
    time.sleep(0.5)
    none_material(b,r,g)
    time.sleep(0.5)
    GPIO.output(b,False)
    GPIO.output(r,False)
    GPIO.output(g,False)
    time.sleep(0.5)
    none_material(b,r,g)


def checkState(b, r, g, percentage_weight, number):
    if percentage_weight >= 50:
        enough_state(b, r, g)

    elif percentage_weight >= 30:
        warning_state(b, r, g)

    elif percentage_weight <= 5 and percentage_weight >=2:
        taring_scale(b,r,g)

    elif percentage_weight <2:
        none_material(b,r,g)

    else:
        insufficient_state(b, r, g)


hx1 = HX711(5, 6)
hx2 = HX711(13, 19)
hx3 = HX711(20, 21)
hx4 = HX711(12, 16)
# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it chan
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx1.set_reading_format("MSB", "MSB")
hx2.set_reading_format("MSB", "MSB")
hx3.set_reading_format("MSB", "MSB")
hx4.set_reading_format("MSB", "MSB")
# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
hx1.set_reference_unit(-133)
hx2.set_reference_unit(-132)
hx3.set_reference_unit(-136)
hx4.set_reference_unit(-135)



weight_max_1 = 10000
weight_max_2 = 10000


hx1.reset()
hx2.reset()
hx3.reset()
hx4.reset()

taring_scale(18,23,24)
taring_scale(17,27,22)

kg_flag = True


def sensing_1(percentage_result, lock):
    LED_BLUE = 18
    LED_RED = 23
    LED_GREEN = 24

    while kg_flag:
        load1A = max(0, int(hx1.get_weight(20)))
        load1B = max(0, int(hx3.get_weight(20)))
        load1 = load1A + load1B
        percentage_weight_1 = 100 * load1 / weight_max_1
        
        checkState(18, 23, 24, percentage_weight_1, 1)
        lock.acquire()
        try:
            percentage_result.value = percentage_weight_1
        finally:
            lock.release()

        time.sleep(0.25)


        # To get weight from both channels (if you have load cells hooked up
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

def sensing_2(percentage_result, lock):
    LED_BLUE = 17
    LED_RED = 27
    LED_GREEN = 22


    while kg_flag:
        load2A = max(0, int(hx2.get_weight(20)))
        load2B = max(0, int(hx4.get_weight(20)))
        load2 = load2A + load2B
        percentage_weight_2 = 100 * load2 / weight_max_2


        checkState(17, 27, 22, percentage_weight_2, 2)
        lock.acquire()
        try:
            percentage_result.value = percentage_weight_2
        finally:
            lock.release()
        time.sleep(0.25)



def connect_pc(load1_final_val, load2_final_val, load3_final_val, load4_final_val, lock):
    port = 8080

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(('', port))
    ss.listen(1)

    print('READY TO ACCESS PORT NO.%d...'%port)
    connectionSock, address = ss.accept()

    print(str(address), 'ACCESS COMPLETE.')

    while True:
        time.sleep(1)
        lock.acquire()

        print "ttload1 percentage : ", load1_final_val.value
        print "ttload2 percentage : ", load2_final_val.value
        print "ttload3 percentage : ", load3_final_val.value
        print "ttload4 percentage : ", load4_final_val.value

        sendData = str(load1_final_val.value) + '/' + str(load2_final_val.value) + '/' + str(load3_final_val.value) + '/' + str(load4_final_val.value) + '||'

        print sendData
        connectionSock.send(sendData.encode('utf-8'))
        sendData = ''
        lock.release()


        time.sleep(1)

load1_per = Value('i', 0)
load2_per = Value('i', 0)
load1_final_val = Value('i', 0)
load2_final_val = Value('i', 0)
load3_final_val = Value('i', 0)
load4_final_val = Value('i', 0)

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()

p1=Process(target=sensing_1, args=(load1_per, lock1))
p2=Process(target=sensing_2, args=(load2_per, lock2))
p3=Process(target=connect_pc, args=(load1_final_val, load2_final_val, load3_final_val, load4_final_val, lock3))

        # To get weight from both channels (if you have load cells hooked up
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

print "Tare done! Add weight now..."

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()


p1.start()
p2.start()
p3.start()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()



while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.

        # np_arr8_string = hx.get_np_arr8_string()
        # binary_string = hx.get_binary_string()
        # print binary_string + " " + np_arr8_string


        lock3.acquire()

        load1_final_val.value = 0
        load2_final_val.value = 0
        load3_final_val.value = 0
        load4_final_val.value = 0

        lock1.acquire()
        try:
            load1_final_val.value =  load1_per.value
        finally:
            lock1.release()


        lock2.acquire()
        try:
            load2_final_val.value =  load2_per.value
        finally:
            lock2.release()

        time.sleep(0.75)


        print 'Connected by', addr
        data = conn.recv(1024)
        if not data:
            break
        else:
            print "recv data: ", data
        conn.sendall(data)



        load3_final_val.value=int(data[:data.find('p')])
        load4_final_val.value=int(data[data.find('p')+1:])
        print "load1 percentage : ", load1_final_val.value
        print "load2 percentage : ", load2_final_val.value
        print "load3 percentage : ", load3_final_val.value
        print "load4 percentage : ", load4_final_val.value

        lock3.release()


    except (KeyboardInterrupt, SystemExit):
        parent_id = os.getpid()
        ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % parent_id, shell=True, stdout=subprocess.PIPE)
        ps_output = ps_command.stdout.read()
        retcode = ps_command.wait()
        for pid_str in ps_output.strip().split("\n")[:-1]:
            os.kill(int(pid_str), signal.SIGTERM)

        conn.close()
        cleanAndExit()
