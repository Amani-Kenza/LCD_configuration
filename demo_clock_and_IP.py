#! /usr/bin/env python
from datetime import datetime
from subprocess import check_output
from time import sleep

import drivers

display = drivers.Lcd()
IP = check_output(["hostname", "-I"]).split()[0]
try:
    print("Writing to display")
    while True:
        display.lcd_display_string(str(datetime.now().time()), 1)
        display.lcd_display_string(str(IP), 2)
        # Uncomment the following line to loop with 1 sec delay
        # sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
