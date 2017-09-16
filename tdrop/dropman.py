#!/usr/bin/python3.6

import subprocess
from tkinter import *

prefix = "tdrop -ma --name 'dropdown terminal'"
suffix = "gnome-terminal"

keycodes = { 
  111: "T", 
  113: "L", 
  114: "R", 
  116: "B" 
}

tdrop_params = {
  "TT": "-n tdropTT -h 600 -s tdropTT -y -1",
  "TL": "-n tdropTL -h 560 -s tdropTL -x 20 -y 30 -w 930",
  "TR": "-n tdropTR -h 560 -s tdropTR -x 970 -y 30 -w 930",
  "BB": "-n tdropBB -h 600 -s tdropBB -y 600",
  "BL": "-n tdropBL -h 560 -s tdropBL -x 20 -y 620 -w 930",
  "BR": "-n tdropBR -h 560 -s tdropBR -x 970 -y 620 -w 930"
}


def main(d="T"):
  main = Tk()
  main.wait_visibility(main)
  main.wm_attributes('-alpha',0.8)
  main.geometry("1x1+0+0") 

  def keyup(event):
    if event.keycode in keycodes.keys():
      direction = d + keycodes[event.keycode]
      if direction in tdrop_params.keys():
        print(tdrop_params[direction])
        cmd = prefix + tdrop_params[direction] + suffix
        subprocess.call(cmd, shell=True)
      pass
    exit()

  frame = Frame(main, width=1, height=1)
  main.bind("<KeyRelease>", keyup)

  frame.pack()
  main.mainloop()


if __name__ == "__main__":
    arg = "B" if len(sys.argv) > 1 and sys.argv[1] != "T" else "T"
    main(arg)
