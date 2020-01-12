#! /usr/bin/python0

import time
import sys
from multiprocessing import Process, Value, Lock
import os
import signal
import subprocess
import socket

HOST = '192.168.43.191'
PORT = 49007


EMULATE_HX711=False


state=4

percentage_weight=0

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print "Cleaning..."

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

def checkState(b, r, g, percentage_weight, number):
    if percentage_weight >= 50:
        state = 1
        enough_state(b, r, g)
        print `number`+" : enough"
    elif percentage_weight >= 30:
        state = 2
        warning_state(b, r, g)
        print `number`+" : warning"
    elif percentage_weight <= 1:
        state = 3
        none_material(b, r, g)
        print `number`+" : no material"
    else:
        state = 4
        insufficient_state(b, r, g)
        print `number`+" : insufficient"


hx5 = HX711(5, 6)
hx6 = HX711(13, 19)
hx7 = HX711(20, 21)
hx8 = HX711(12, 16)
# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it chan
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx5.set_reading_format("MSB", "MSB")
hx6.set_reading_format("MSB", "MSB")
hx7.set_reading_format("MSB", "MSB")
hx8.set_reading_format("MSB", "MSB")
# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
hx5.set_reference_unit(133)
hx6.set_reference_unit(-134)
hx7.set_reference_unit(-136)
hx8.set_reference_unit(-133)



weight_max_3 = 20000
weight_max_4 = 20000


hx5.reset()
hx6.reset()
hx7.reset()
hx8.reset()

hx5.tare()
hx6.tare()
hx7.tare()
hx8.tare()


kg_flag = True


def sensing_3(percentage_result, lock):
    LED_BLUE = 18
    LED_RED = 23
    LED_GREEN = 24

  
    while kg_flag:
        load3A = max(0, int(hx5.get_weight(20)))
        load3B = max(0, int(hx7.get_weight(20)))
        load3 = load3A + load3B
        percentage_weight_3 = 100 * load3 / weight_max_3
	'''
        print("aaaa")
        print "load3A"
        print load3A
        print "load3B"
        print load3B
        print "total load_3"
        print load3
        print "Percentage weight_3"
        print percentage_weight_3
        '''

	checkState(18, 23, 24, percentage_weight_3, 3)
	lock.acquire()
	try:
    	    percentage_result.value = percentage_weight_3
	finally:
	    lock.release()
        time.sleep(0.25)
        


        # To get weight from both channels (if you have load cells hooked up
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

def sensing_4(percentage_result, lock):
    LED_BLUE = 17
    LED_RED = 27
    LED_GREEN = 22


    while kg_flag:
        load4A = max(0, int(hx6.get_weight(20)))
        load4B = max(0, int(hx8.get_weight(20)))
        load4 = load4A + load4B
        percentage_weight_4 = 100 * load4 / weight_max_4

	'''
        print "load4A"
        print load4A
        print "load4B"
        print load4B
        print "total load_4"
        print load4
        print "Percentage weight_4"
        print percentage_weight_4
	'''

        checkState(17, 27, 22, percentage_weight_4, 4)
	lock.acquire()
	try:
	    percentage_result.value = percentage_weight_4
	finally:
	    lock.release()
        time.sleep(0.25)

load3_per = Value('i', 0)
load4_per = Value('i', 0)

lock3 = Lock()
lock4 = Lock()

p3=Process(target=sensing_3, args=(load3_per, lock3))
p4=Process(target=sensing_4, args=(load4_per, lock4))

        # To get weight from both channels (if you have load cells hooked up
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

print "Tare done! Add weight now..."

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()

p3.start()
p4.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.

        # np_arr8_string = hx.get_np_arr8_string()
        # binary_string = hx.get_binary_string()
        # print binary_string + " " + np_arr8_string

	lock3.acquire()
	try:
	    print "load3", load3_per.value
        finally:
	    lock3.release()

	lock4.acquire()
	try:
	    print "load4", load4_per.value
	finally:
	    lock4.release()

        

	s.sendall(b"%dp%s" % (load3_per.value, load4_per.value))
	data = s.recv(1024)	
	print ('Received', repr(data))
        time.sleep(0.5)
    
    except (KeyboardInterrupt, SystemExit):
        parent_id = os.getpid()
        ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % parent_id, shell=True, stdout=subprocess.PIPE)
        ps_output = ps_command.stdout.read()
        retcode = ps_command.wait()
        for pid_str in ps_output.strip().split("\n")[:-1]:
            os.kill(int(pid_str), signal.SIGTERM)
	s.close()
        
        cleanAndExit()


