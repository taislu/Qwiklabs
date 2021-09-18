#!/usr/bin/env python3

def reverse_number(x):
  reverse = 0
  while x != 0:
    p, q = divmod(x, 10)
    reverse = reverse * 10 + q
    x = p
  return(reverse)

print(reverse_number(12345)) # 54321

def sum_of_digits(x):
  sum = 0
  while x != 0:
    p, q = divmod(x, 10)
    sum += q
    x = p
  return(sum)

#print(sum_of_digits(1234)) # 10
#print(sum_of_digits(99)) # 18

def isPrimeNum(x):
  for n in range(2,x):
    remainder = x % n
    if remainder == 0:
      return(False)
  return(True)

#print(isPrimeNum(23)) # True
#print(isPrimeNum(24)) # False


def isPrime(n):
  count = 0
  x = n
  while x != 0:
    p, q = divmod(n, x)
    if q == 0: 
      count += 1
    x -= 1
  
  if count > 2:
    return(False)
  return(True)
  
#print(isPrime(23)) # True
#print(isPrime(24)) # False