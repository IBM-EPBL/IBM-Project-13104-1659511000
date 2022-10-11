import random
while(True):
    r=random.randint(10,99)
    t=random.randint(10,99)
    if(r > 30 and t > 75):
     print("High Temprature and Humidity of:",r,t,"#","alarm is on")
    elif(r < 35 and t < 55):
         print("Normal Temprature and Humidity of:",r,t,"#","alarm is off")
         break
