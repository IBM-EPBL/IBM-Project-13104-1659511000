from gpiozero import LED
from time import sleep


R= LED(17)      
Y=(22)
G=(27)


while True:
    R.on()                     
    print("Red light is ON")
    for i in range(120,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    R.off()

    Y.on()                   
    print("Yellow light is ON")
    for i in range(20,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    Y.off()

    G.on                   
    print("Green light is ON")
    for i in range(60,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    G.off()
