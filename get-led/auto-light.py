import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led=17
GPIO.setup(led,GPIO.OUT)
botton = 6
state=0
GPIO.setup(botton,GPIO.IN)
while True:
    state= GPIO.input(botton)
    GPIO.output(led,state)