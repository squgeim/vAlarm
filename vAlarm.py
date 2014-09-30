#!/bin/python

import sys
import timer

if __name__ == '__main__':
  f = 'file://'+sys.argv[3]
  sc = 'cvlc '+f+' &>/dev/null'
  timer.timer(sys.argv[1].split(':'),sys.argv[2].split(':'),sc)

