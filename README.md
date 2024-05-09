# 3D Model
https://www.thingiverse.com/thing:736693

# Hardware
- Rockpi 4 SE, or any board that has an I2C interfaces)
- PWM Servo driver board 16 Channel, using only one channel though
- SG90 Servo 360 degree

# Software
Controlling the Servo
- PCA9685.py: driver code for the PWM board.
- main.py: code that drives the servo once.
- crontab: the cron job specification that schedules the main.py to run every 6 hours

Deploying as an Add-on for Home Assistant OS
- Dockerfile
- config.yaml

**Note**, in the run and crontab, absolute paths are used in order to avoid troubles as an cron job. Edit them if necessary.

**Note**, the address for the I2C bus can be detected using the mraa-i2c tool.

**Note**, I2C bus may not be enabled by default (as Rockpi 4 SE), you need some tricks for kernel device tree overlay to start it.

# Enabling i2c-7 on Rockpi 4 SE
According to the [page](https://wiki.radxa.com/Rock4/hardware/gpio), pins 5 and 7 are the I2C-7 of the RK3399 chip. Linux distributions usually set I2C-7 disabled by default. It is necessary to enable it first in a device tree overlay.

Source code (filename as rockchip-custom.dts) for the overlay.
```
/dts-v1/;

/ {
        compatible = "rockchip,rk3399";
		
        fragment@0 {
                target-path = "/i2c@ff160000";
                __overlay__ {
                        status = "okay";
                };
        };
};
```

Compile it.

```
dtc -O dtb -o rockchip-custom.dtbo -b 0 -@ rockchip-custom.dts
```

On the Home Assistant OS, copy `rockchip-custom.dtbo` to `/mnt/boot/overlays/` and update the file `/mnt/boot/haos-config.txt`.
```
overlays=rk3399-disable-wifi-interrupts rockchip-custom
```

Reboot the OS. Aften that, i2c-7 is enabled.

```
# cat /proc/device-tree/i2c@ff160000/status 
okay

# ls /dev/i2c-*
/dev/i2c-0  /dev/i2c-1  /dev/i2c-3  /dev/i2c-4  /dev/i2c-7
```


# Add-on for Home Assistant OS
Reference: [Add-ons](https://developers.home-assistant.io/docs/add-ons/tutorial/)

In the SSH (the add-on SSH). Clone the repo to `/root/addons`. Then the *Fishfeeder* can be then found in the local add-ons. Click *Install* and *Start*. That's it.

