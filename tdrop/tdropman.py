#!/usr/bin/env python

import sys
import pyxhook
import time
import subprocess

running = True


def main(d="T"):
    global direction
    direction = d

    # Create hookmanager
    hookman = pyxhook.HookManager()
    # Define our callback to fire when a key is pressed down
    hookman.KeyDown = kbevent
    # Hook the keyboard
    hookman.HookKeyboard()
    # Start our listener
    hookman.start()

    # Create a loop to keep the application running
    global running
    while running:
        time.sleep(0.1)

    # Close the listener when we are done
    hookman.cancel()

# This function is called every time a key is presssed


def translate_ascii(num):
    if num == 81:
        return "L"
    elif num == 82:
        return "T"
    elif num == 83:
        return "R"
    elif num == 84:
        return "B"


def kbevent(event):
    global running
    print direction
    # print key info
    print(event)

    running = False
    if event.Ascii > 80 and event.Ascii < 85:
        drop(translate_ascii(event.Ascii))


def drop(arrow):
    global direction
    location = "{}{}".format(direction, arrow)
    prefix = "tdrop -ma --name 'dropdown terminal'"
    suffix = "gnome-terminal"
    cmd = prefix
    if location == "TT":
        cmd = "{} {}".format(cmd, "-n tdropTT -h 600 -s tdropTT -y -1")
        # undo that up key
        # we should really be capturing input but this works fine
        subprocess.call("xdotool key Down", shell=True)
    elif location == "TL":
        cmd = "{} {}".format(
            cmd, "-n tdropTL -h 560 -s tdropTL -x 20 -y 30 -w 930")
    elif location == "TR":
        cmd = "{} {}".format(
            cmd, "-n tdropTR -h 560 -s tdropTR -x 970 -y 30 -w 930")
    elif location == "BB":
        cmd = "{} {}".format(cmd, "-n tdropBB -h 600 -s tdropBB -y 600")
    elif location == "BL":
        cmd = "{} {}".format(
            cmd, "-n tdropBL -h 560 -s tdropBL -x 20 -y 620 -w 930")
    elif location == "BR":
        cmd = "{} {}".format(
            cmd, "-n tdropBR -h 560 -s tdropBR -x 970 -y 620 -w 930")
    if cmd != prefix:
        cmd = "{} {}".format(cmd, suffix)
        print location, cmd
        subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    arg = "B" if len(sys.argv) > 1 and sys.argv[1] != "T" else "T"
    main(arg)
