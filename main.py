from PCA9685 import PCA9685
from time import sleep

pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)

pwm.setAngle(0, 50)
sleep(0.5)
pwm.setAngle(0, 90)
