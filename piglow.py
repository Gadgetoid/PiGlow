#####################################################
## Python module to control the PiGlow by Pimoroni ##
##                                                 ##
## Written by Phil - @Gadgetoid  -  v1   18/03/05  ##
##            phil@gadgetoid.com                   ##
##                                                 ##
## Original by Jason - @Boeeerb  -  v0.5  17/08/13 ##
##            jase@boeeerb.co.uk                   ##
#####################################################
##
## v1.0 - Major update to depend upon common sn3218 library
## v0.51- Removed RPI for Pi 2 temp fix     - 10/02/15
## v0.5 - Add RPI VER 3 for model B+         - 26/08/14
## v0.4 - Auto detect Raspberry Pi revision  - 17/08/13
## v0.3 - Added fix from topshed             - 17/08/13
## v0.2 - Code cleanup by iiSeymour          - 15/08/13
## v0.1 - Initial release                    - 15/08/13
##

from smbus import SMBus
import atexit
import sn3218

class PiGlow:

    def __init__(self):
        sn3218.enable()
        self.leds = [0x00] * 18

        atexit.register(self.off)

    def off(self):
        self.all(0)
    
    def set_led(self, led, value):
        self.leds[ led - 1 ] = value

    def white(self, value):
        self.set_led(0x0A, value)
        self.set_led(0x0B, value)
        self.set_led(0x0D, value)
        self.update()

    def blue(self, value):
        self.set_led(0x05, value)
        self.set_led(0x0C, value)
        self.set_led(0x0F, value)
        self.update()

    def green(self, value):
        self.set_led(0x06, value)
        self.set_led(0x04, value)
        self.set_led(0x0E, value)
        self.update()

    def yellow(self, value):
        self.set_led(0x09, value)
        self.set_led(0x03, value)
        self.set_led(0x10, value)
        self.update()

    def orange(self, value):
        self.set_led(0x08, value)
        self.set_led(0x02, value)
        self.set_led(0x11, value)
        self.update()

    def red(self, value):
        self.set_led(0x07, value)
        self.set_led(0x01, value)
        self.set_led(0x12, value)
        self.update()

    def all(self, value):
        self.leds = [value] * 18
        self.update()

    def arm(self, arm, value):
        if arm == 1:
            self.set_led(0x07, value)
            self.set_led(0x08, value)
            self.set_led(0x09, value)
            self.set_led(0x06, value)
            self.set_led(0x05, value)
            self.set_led(0x0A, value)
            self.update()
        elif arm == 2:
            self.set_led(0x0B, value)
            self.set_led(0x0C, value)
            self.set_led(0x0E, value)
            self.set_led(0x10, value)
            self.set_led(0x11, value)
            self.set_led(0x12, value)
            self.update()
        elif arm == 3:
            self.set_led(0x01, value)
            self.set_led(0x02, value)
            self.set_led(0x03, value)
            self.set_led(0x04, value)
            self.set_led(0x0F, value)
            self.set_led(0x0D, value)
            self.update()
        else:
            print "Unknown number, expected only 1, 2 or 3"

    def arm1(self, value):
        self.set_led(0x07, value)
        self.set_led(0x08, value)
        self.set_led(0x09, value)
        self.set_led(0x06, value)
        self.set_led(0x05, value)
        self.set_led(0x0A, value)
        self.update()

    def arm2(self, value):
        self.set_led(0x0B, value)
        self.set_led(0x0C, value)
        self.set_led(0x0E, value)
        self.set_led(0x10, value)
        self.set_led(0x11, value)
        self.set_led(0x12, value)
        self.update()

    def arm3(self, value):
        self.set_led(0x01, value)
        self.set_led(0x02, value)
        self.set_led(0x03, value)
        self.set_led(0x04, value)
        self.set_led(0x0F, value)
        self.set_led(0x0D, value)
        self.update()

    def colour(self, colour, value):
        if colour == 1 or colour == "white":
            self.set_led(0x0A, value)
            self.set_led(0x0B, value)
            self.set_led(0x0D, value)
            self.update()

        elif colour == 2 or colour == "blue":
            self.set_led(0x05, value)
            self.set_led(0x0C, value)
            self.set_led(0x0F, value)
            self.update()

        elif colour == 3 or colour == "green":
            self.set_led(0x06, value)
            self.set_led(0x04, value)
            self.set_led(0x0E, value)
            self.update()

        elif colour == 4 or colour == "yellow":
            self.set_led(0x09, value)
            self.set_led(0x03, value)
            self.set_led(0x10, value)
            self.update()

        elif colour == 5 or colour == "orange":
            self.set_led(0x08, value)
            self.set_led(0x02, value)
            self.set_led(0x11, value)
            self.update()
        elif colour == 6 or colour == "red":
            self.set_led(0x07, value)
            self.set_led(0x01, value)
            self.set_led(0x12, value)
            self.update()
        else:
            print "Only colours 1 - 6 or color names are allowed"

    def led(self, led, value):
        leds = [
            "0x00", "0x07", "0x08", "0x09", "0x06", "0x05", "0x0A", "0x12", "0x11",
            "0x10", "0x0E", "0x0C", "0x0B", "0x01", "0x02", "0x03", "0x04", "0x0F", "0x0D"]
        self.set_led(int(leds[led], 16), value)
        self.update()

    def led1(self, value):
        self.set_led(0x07, value)
        self.update()

    def led2(self, value):
        self.set_led(0x08, value)
        self.update()

    def led3(self, value):
        self.set_led(0x09, value)
        self.update()

    def led4(self, value):
        self.set_led(0x06, value)
        self.update()

    def led5(self, value):
        self.set_led(0x05, value)
        self.update()

    def led6(self, value):
        self.set_led(0x0A, value)
        self.update()

    def led7(self, value):
        self.set_led(0x12, value)
        self.update()

    def led8(self, value):
        self.set_led(0x11, value)
        self.update()

    def led9(self, value):
        self.set_led(0x10, value)
        self.update()

    def led10(self, value):
        self.set_led(0x0E, value)
        self.update()

    def led11(self, value):
        self.set_led(0x0C, value)
        self.update()

    def led12(self, value):
        self.set_led(0x0B, value)
        self.update()

    def led13(self, value):
        self.set_led(0x01, value)
        self.update()

    def led14(self, value):
        self.set_led(0x02, value)
        self.update()

    def led15(self, value):
        self.set_led(0x03, value)
        self.update()

    def led16(self, value):
        self.set_led(0x04, value)
        self.update()

    def led17(self, value):
        self.set_led(0x0F, value)
        self.update()

    def led18(self, value):
        self.set_led(0x0D, value)
        self.update()
