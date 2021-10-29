

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import random
from datetime import datetime
from awscrt import mqtt

from awsiot import mqtt_connection_builder


ENDPOINT = "a3onae3fkax6ub-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "solar"
PATH_TO_CERT = "certificates/device.crt"
PATH_TO_KEY = "certificates/private.key"
PATH_TO_ROOT = "certificates/AmazonRootCA1.pem"

TOPIC = "test/testing"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
            print(i+1);
            message = {}
            message['Battery Voltage'] = random.randint(94,100)
            message['Solar Current'] = random.randint(60,72)
            message['Load Current'] = random.randint(90,120)
            message['Temperature'] = random.randint(40,70)
            message['Tilt angle'] = random.randint(-40,85)
            message['Datetime'] = datetime.now()
            
           
            
            message_json = json.dumps(message,indent=4, sort_keys=True, default=str)
            myAWSIoTMQTTClient.publish(
                TOPIC,
                json.dumps(message_json),
                1
                )
            t.sleep(1)
            t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()