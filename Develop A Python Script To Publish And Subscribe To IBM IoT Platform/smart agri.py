import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig={
    "identity":{
        "orgId":"74jmsm",
        "typeId":"NodeMCU",
        "deviceId":"12345"
        },
    "auth":{
        "token":"ddd3nribm"
        }
    }
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
def myCommandCallback(cmd):
    print("message received from IBM IOT platform:%s"%cmd.data['command'])
    m=cmd.data['command']
    if(m=="motorn"):
        print("motor is switched on")
        elsif(m=="motoroff")
        print("motor is switched off")
        print("")
        while true:
                soil=random.randint(0,100)
                tem=random.randint(-20,125)
                hum=random.ranint(0,100)
                myData={'soil_moisture':soil,'temperature':tem,'humidity':hum}
                client.publishEvent(eventId="status",msgFormat="json",data=myData,gos=0,onpublish=None)
                print("published data Successsfully:%s",myData)
                time.sleep(2)
                client.commandCallback=myCommandCallback
                client.disconnect()
