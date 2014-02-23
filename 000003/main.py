#!/usr/bin/env python

import sys, math, random, time, decimal

_max = 600851475143
_winner = 0

def go():
  global _max, _winner
  _cursor = 2
  while _max > 1:
    if (_max % _cursor) is 0:
      _max = _max / _cursor
      _winner = _cursor
      _cursor = 2
    else:
      _cursor += 1

def main():
  start_time = time.time()
  go()
  print 'Winner is: ' + str(_winner)
  print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()
