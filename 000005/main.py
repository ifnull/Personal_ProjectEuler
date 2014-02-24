#!/usr/bin/env python

import math, time

def main():
  start_time = time.time()

  # for i in range(10,3000):
  #   test = ''.join( str(i) for i in [i % 6, i % 7, i % 8, i % 9, i % 10] )
  #   if test == '00000':
  #     print i
  #     break

  for i in range(20,300000000):
    test = ''.join( str(i) for i in [i % 11, i % 12, i % 13, i % 14, i % 15, i % 16, i % 17, i % 18, i % 19, i % 20] )
    if test == '0000000000':
      print i
      break

  # print 'Winner is: ' + str(_palindromes[-1])
  # print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()
