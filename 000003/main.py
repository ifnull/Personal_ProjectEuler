#!/usr/bin/env python

import sys

num = 10000
_range = range(0,num)

def sieve(m):
  for i in range(m, len(_range)):
    if _range[i] is True:
      if (i+1) % m is 0 and i+1 is not m:
        _range[i] = False

def main():
  # Sieve of Eratosthenes
  #num = 600851475143

  for i in range(len(_range)):
    _range[i] = True

  _range[0] = False

  # sieve(2)

  for i in range(1,num):
    sieve(i)

  for x in range(len(_range)):
    if _range[x] is True:
      print x+1

  # print range(0,50)

  # for i in range(1, num):
  #   if num % i is 0:
  #     factors.append(i)
  # print factors

if __name__ == '__main__':
  main()

