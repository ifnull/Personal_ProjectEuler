#!/usr/bin/env python

import math, time

def main():
  start_time = time.time()
  _max = 100
  print sum(range(1,_max+1))**2-sum([i**2 for i in range(1,_max+1)])
  print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()
