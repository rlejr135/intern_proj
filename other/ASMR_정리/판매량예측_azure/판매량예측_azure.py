import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json
import numpy as np
import pandas as pd
import datetime, time
from datetime import datetime
data={}
f = open("weather_day_text.txt", "r")
i = 0
while True:
    line = f.readline()
    if not line: break
    data[i] = line
    i = i + 1
    print(line)

print(data)
now = datetime.now()

region = 1
print('%s-%s-%s'%(now.year, now.month, now.day))
today = str(now.year)+"-"+str(now.month)+"-"+str(now.day)

ff = open("pre_food.txt", 'w')
ff.close()

while True:
    straw_data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Date", "Low_temp", "High_temp", "Rainfall", "Humidity", "Region", "IsHoliday", "Strawberry"],
                        "Values": [[ today, data[1], data[0], data[3], data[2], str(region), "True", "0" ]]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(straw_data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/51c4a723d603403883a9fba3c84c1bce/services/8cf2b119a0bb4b56858fa185b708ff91/execute?api-version=2.0&details=true'
    api_key = '8AHnMz7qw+TyQpMKtF9mfz4AtvNHgqEQCGGZl60c1QOM94pfSMjgA1COKnadagOGkm9OCMZrzM0itsHUmSUNDw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        straw_result = response.read()
        print('strawberry')
        print(straw_result)


    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))
    ###################################################

    banana_data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Date", "Low_temp", "High_temp", "Rainfall", "Humidity", "Region", "IsHoliday", "Banana"],
                        "Values": [[ today, data[1], data[0], data[3], data[2], str(region), "True", "0" ]]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(banana_data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/51c4a723d603403883a9fba3c84c1bce/services/55f2af2c44e34cf9909f0807fa0e1844/execute?api-version=2.0&details=true'
    api_key = 'ET9UArvrHN+zOK6wafpmuWcH08WHyydrsj2Rh2N5oW6QAH2hVOfDJ+5fjNmy5M+m9bCfVHsD2H++9yI8pDxhjg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        banana_result = response.read()
        print('banana')
        print(banana_result)
    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    ###################################################

    watermelon_data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Date", "Low_temp", "High_temp", "Rainfall", "Humidity", "Region", "IsHoliday", "Watermelon"],
                        "Values": [[ today, data[1], data[0], data[3], data[2], str(region), "True", "0" ]]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(watermelon_data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/51c4a723d603403883a9fba3c84c1bce/services/b34edef3c19d4572acdcb5e51720b6d4/execute?api-version=2.0&details=true'
    api_key = '0/4GdTLbUZ/YaGpF7y35QBppNRGWpymjArwer0lfOEN2CGiRnzys1gzaubuSJZeryjVjvMtAnFdYX7elpBDN5A==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        watermelon_result = response.read()
        print('watermelon')
        print(watermelon_result)
    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    ###########################################

    bb_data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Date", "Low_temp", "High_temp", "Rainfall", "Humidity", "Region", "IsHoliday", "Blueberry"],
                        "Values": [[ today, data[1], data[0], data[3], data[2], str(region), "True", "0" ]]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(bb_data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/51c4a723d603403883a9fba3c84c1bce/services/2e265602dac247e68cb5c819f4d136e8/execute?api-version=2.0&details=true'
    api_key = 'NnXvOnJBcrYatiOH4vVJIbrFU0YXBTh0crsAZbeGT8Fm2bPwO0CP1iQQBUTYxxP3cq9+tD6ylT0eh5Smp0jS8Q==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        bb_result = response.read()
        print("blueberry")
        print(bb_result)


    except urllib.request.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))


    ##########################################
    straw1 = straw_result.decode()
    straw2 = straw1.split(',')
    straw3 = straw2[27]
    straw4 = straw3[1:5]

    banana1 = banana_result.decode()
    banana2 = banana1.split(',')
    banana3 = banana2[27]
    banana4 = banana3[1:5]

    watermelon1 = watermelon_result.decode()
    watermelon2 = watermelon1.split(',')
    watermelon3 = watermelon2[27]
    watermelon4 = watermelon3[1:5]

    bb1 = bb_result.decode()
    bb2 = bb1.split(',')
    bb3 = bb2[27]
    bb4 = bb3[1:5]

    f = open("pre_food.txt", 'a')
    f.write(straw4 + '\n' + banana4 + '\n'+ watermelon4 + '\n' + bb4+'\n')

    f.close()

    region = region+1
    if region == 4:
        break

