words = ['cat', 'window', 'outty']
for w in words:
  print(w, len(w))

# range()
## Basic usage
## the range() method builds a list of numbers in the range that you input
for i in range(3):
  print(i)
print('starting next for loop')
for j in range(2,5):
  print(j)

## Accessing values in a list
a = ['baby', 'shark', 'doo', 'doo', 'doodoo']
for i in range(len(a)):
  print(i, a[i])

# break, continue, else in a for loop
for n in range(2,8):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
## the else keyword in this case functions a lot like a catch block in JavaScript
  else:
    # loop falls through without finding a factor
    print(n, ' is a prime num')

# Defining functions
def fib(n = 1):
  a, b = 0, 1
  while a < n:
    print(a, sep=' ', end=' ')
    a, b = b, a + b
  print()

fib(10)

def fib2(n = 1):
  res = []
  a, b = 0, 1
  while a < n:
    res.append(a)
    a, b = b, a + b
  return res

myRes = fib2(10)
print(myRes)

# default input
def printMyNum(num = 69):
  print(num)

printMyNum()

# Lambda expressions
## basically syntactic sugar for functions(similar in concept to what arrow functions do)
def increment(num = 0):
  return lambda x: x + num

incBy2 = increment(2)
incBy1 = increment(1)
print(incBy2(1))
print(incBy1(99))

