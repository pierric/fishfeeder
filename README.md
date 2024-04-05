# 3D Model
https://www.thingiverse.com/thing:736693

# Hardware
- Rockpi 4 SE, or any board that has an I2C interfaces)
- PWM Servo driver board 16 Channel, using only one channel though

# Software
- PCA9685.py: driver code for the PWM board.
- main.py: code that drives the servo once.
- crontab: the cron job specification that schedules the main.py to run every 6 hours

**Note**, in the run and crontab, absolute paths are used in order to avoid troubles as an cron job. Edit them if necessary.

**Note**, the address for the I2C bus can be detected using the mraa-i2c tool.

**Note**, I2C bus may not be enabled by default (as Rockpi 4 SE), you need some tricks for kernel device tree overlay to start it.

