import RPi.GPIO as GPIO
import time;

motorRightA = 37;
motorRightB = 35;

GPIO.setmode(GPIO.BOARD);
GPIO.setup(motorRightA, GPIO.OUT);
GPIO.setup(motorRightB, GPIO.OUT);

def setRightMotor(direction):
    if(direction == 1):
        GPIO.output(motorRightA, GPIO.LOW);
        GPIO.output(motorRightB, GPIO.HIGH);

    elif (direction == -1):
        GPIO.output(motorRightA, GPIO.HIGH);
        GPIO.output(motorRightB, GPIO.LOW);
    else:
        GPIO.output(motorRightA, GPIO.LOW);
        GPIO.output(motorRightB, GPIO.LOW);

setRightMotor(0);
pwm = GPIO.PWM(motorRightA, 10000);
pwm.start(1);

time.sleep(2)
pwm.ChangeFrequency(100000);

time.sleep(2)
pwm.ChangeFrequency(1000000);

time.sleep(2)
pwm.ChangeFrequency(1000000);

    #setRightMotor(1);
    #print('1');
    #time.sleep(1);

    #setRightMotor(-1)
    #print('-1');
    #time.sleep(1)

