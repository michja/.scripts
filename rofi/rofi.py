#!/usr/bin/python
#title : rofi wrapper

import subprocess
import sys, fileinput
from random import randint

def append_new_line( string ):
  if '\n' not in string:
    string += '\n'
  return string

def rofi( args, stdin=[] ):
  if len( args ) > 1:
    cmd = '-dmenu ' + ' '.join( args )
    stdin = list( map( append_new_line, stdin ) )
    stdin = ''.join( stdin )
  else:
    cmd = '-modi drun -show drun'

  colours = ["#b8bb26", "#fabd2f", "#fb4934", "#83a598", "#d3869b", "#8ec07c", "#fe8019"]
  colour_str =  "-color-normal 'argb:00232221, #a2a2a2, argb:00232221, {}, #14161f'".format(colours[randint(0,len(colours)-1)]) 

  proc = subprocess.Popen('rofi -font "Operator Mono 18" {} {}'.format(colour_str, cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  proc.stdin.write(stdin.encode())
  out, err = proc.communicate()

  return out.decode().replace('\n', '')
  


if __name__ == "__main__":
  sys.stdout.write( rofi( sys.argv[1:], sys.stdin ) )
  sys.stdout.flush()
  sys.exit(0)
