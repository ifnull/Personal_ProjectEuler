#!/usr/bin/env python

import math, time

_range = range(100,1000)
_palindromes = []

def main():
  start_time = time.time()
  for f in _range:
    for s in _range:
      p = str( f * s )
      if p == p[::-1]:
        _palindromes.append(int(p))
      else:
        continue;
  _palindromes.sort()
  print 'Winner is: ' + str(_palindromes[-1])
  print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()
