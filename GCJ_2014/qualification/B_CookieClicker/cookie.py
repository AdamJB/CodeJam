#!/usr/bin/env python

"""
  Problem : Cookie Clicker Alpha
  Code by : AdamJB
  Info    : https://code.google.com/codejam/contest/2974486/dashboard#s=p1
"""

def cookie(cookies, case):  
  c = cookies[0]
  f = cookies[1]
  x = cookies[2]

  cookiesPerSecond = 2.0

  totalTimeForCookiesFarm = 0.0
  # Start with worst case?
  lastTimeTotal = x / cookiesPerSecond
  
  while (1):
    # Increase last total time to buy farm
    totalTimeForCookiesFarm += c / cookiesPerSecond
    # Boost Speed after farm is bought
    cookiesPerSecond = cookiesPerSecond + f
    
    # See if we're getting slower or faster in producing cookies
    currentTotalTime = (x / cookiesPerSecond) + totalTimeForCookiesFarm
    if currentTotalTime < lastTimeTotal:
      lastTimeTotal = currentTotalTime
    else:
      break

  print("Case #%d: %.7f" % (case, lastTimeTotal))

  
numCases = int(input())

for case in range(0, numCases):
  cookies = [float(i) for i in raw_input().strip().split()]
  cookie(cookies, case+1)
