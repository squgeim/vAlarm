#!/bin/python

import sys,time,subprocess

def timer(day,tm,sc):
  now = time.localtime()

  for i in range(len(day)):
    day[i] = int(day[i])
  for i in range(len(tm)):
    tm[i] = int(tm[i])
  
  dest_l = (day[0], day[1], day[2],
      tm[0], tm[1], tm[2],
      3, 232, 0)

  
  diff = time.mktime(dest_l) - time.time()
  time.sleep(diff)
  subprocess.call(sc.split(' '))

if __name__=='__main__':
  day = sys.argv[1].split(':')
  tm = sys.argv[2].split(':')
  sc = sys.argv[3] 
  
  timer(day,tm,sc)
