from machine import Pin,PWM
import time

START = Pin(21,Pin.IN)
# Set Sensor
s1 = Pin(0, Pin.IN, Pin.PULL_UP)  
s2 = Pin(1, Pin.IN, Pin.PULL_UP)
s3 = Pin(2, Pin.IN, Pin.PULL_UP)
s4 = Pin(3, Pin.IN, Pin.PULL_UP)
s5 = Pin(4, Pin.IN, Pin.PULL_UP)

#Set Motor
Motor_RIGHT_pwm = PWM(Pin(10))  # ขา PWM ควบคุมความเร็ว
Motor_RIGHT_dir = Pin(11, Pin.OUT)  # ขากำหนดทิศทาง

Motor_LEFT_pwm = PWM(Pin(8))
Motor_LEFT_dir = Pin(9,Pin.OUT)

Motor_RIGHT_pwm.freq(1000)
Motor_LEFT_pwm.freq(1000)

def Move(speedL, speedR, direction="forward"):
    if direction == "forward":
        Motor_RIGHT_dir.value(0)
        Motor_LEFT_dir.value(0)
    elif direction == "backward":
        Motor_RIGHT_dir.value(1)
        Motor_LEFT_dir.value(1)
        
    Motor_RIGHT_pwm.duty_u16(int(speedR * 65535 / 100))
    Motor_LEFT_pwm.duty_u16(int(speedL * 65535 / 100))

def start():
    while True:
        print(s1.value(),s2.value(),s3.value(),s4.value(),s5.value(),"\n")
        
while True:
    if START.value()==0:
        start()