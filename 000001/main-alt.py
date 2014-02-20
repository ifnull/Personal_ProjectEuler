#!/usr/bin/env python

import sys, math

# Get sum of multiples in range
def som(m,r):
  fl = math.floor(r/m)
  return m * fl * (fl + 1) / 2;

def main():
  # Sum of multiples of 3 and 5 minus instances of collision
  print math.trunc(som(3,999) + som(5,999) - som(15,999))

if __name__ == '__main__':
  main()