#!/usr/bin/env python

import sys

def main():
  _sum = 0
  _max = 4000000000
  fib = [1,2]

  while True:
    nf = fib[-1]+fib[-2]

    if nf >= _max:
      break

    fib.append(nf)

    if nf % 2 is 0:
      _sum += nf

  print _sum

if __name__ == '__main__':
  main()
