#!/usr/bin/env python

import sys, math

def fib(p):
  gr = (1 + math.sqrt(5)) / 2
  return math.trunc( ( math.pow( gr, p ) - math.pow( (1 - gr), p ) ) / math.sqrt(5) )

def main():
  _sum = 0
  _max = 4000000000
  for x in range(0, 100, 3):
    v = fib(x)
    if v >= _max:
      break
    if x is not 0:
      _sum += fib(x)
  print _sum

if __name__ == '__main__':
  main()
