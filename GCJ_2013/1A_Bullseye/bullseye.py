#!/usr/bin/env python
 
"""
  Problem : Bullseye
  Code by : AdamJB
  Note: this solves small problem
"""
 
import numpy as np

def paintNeededForArea(r):
  innerRadius = r**2
  outerRadius = (r+1)**2
  return (int) (outerRadius - innerRadius)
  
def solveCase(case, r, t):
  numCircles = 0

  currentRadius = r
  while (t > 0):    
    # print currentRadius 
    paintUsed = paintNeededForArea(currentRadius)
    t = t - paintUsed    
    if (t >= 0):
      numCircles += 1

    currentRadius = currentRadius+2

  print "Case #" + str(case) + ": " + str(numCircles)
  
def main():
  T = int(raw_input())
 
  for case in xrange(T):
    (r, t) = (int(i) for i in raw_input().strip().split())
    solveCase(case+1, r, t)
 
main()
