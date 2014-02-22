#!/usr/bin/env python
# Sieve of Eratosthenes

import sys, time

# _max = 600851475143
_max = 10000
_cursor = 2 # start at 2. 1 is a factor of everything
_sieve = {x: True for x in range( _cursor, _max + 1 )}
_primes = []

def sift():
  global _cursor, _max
  next_found = False
  cursor = count = 0

  for i in range( _cursor + 1, len(_sieve) + 1 ):
    if _sieve[i] is True:
      count += 1
      mod = i % _cursor
      if mod is 0:
        _sieve[i] = False
      elif mod is not 0 and next_found is False:
        cursor = i
        next_found = True

  if cursor is not 0:
    _cursor = cursor

  if count > 0:
    return True
  else:
    return False

def main():
  start_time = time.time()

  while sift():
    pass

  for i,x in enumerate(_sieve):
    if _sieve[x] is True:
      _primes.append(x)

  print 'Winner is: ' + str(_primes[-2])
  print time.time() - start_time, "seconds"

if __name__ == '__main__':
  main()

