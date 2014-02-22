#!/usr/bin/env python
# Fermat
# Attempt inverse recursive loop testing for largest prime

import sys, math, random, time, decimal

def main():
  start_time = time.time()

  p = 600851475143
  a = random.randrange(1, 7)

  print (a ** ( p - 1 ) ) %  p

  print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()



