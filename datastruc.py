# Reference the python docs for more https://docs.python.org/3/tutorial/datastructures.html
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)
print(fruits.pop())

# Lists as Stacks
stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

# Lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)

# List Comprehensions
squares = []
for x in range(10):
  squares.append(x**2)
print(squares)
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]
print('simple list comp', squares3)

## more complex list comprehensions
filterArr = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print('complicated list comprehension', filterArr)

# Deleting list elements
froot = ['apple', 'banana', 'pear', 'orange']
del froot[1]
print(froot)

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel)

del tel['sape']
tel['irv'] = 4127
print(tel)

# List keys
print(list(tel))

# List sorted keys
print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)

## more ways to build a dictionary
constructed = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(constructed)

comprehen = {x: x**2 for x in (2, 4, 6)}
print(comprehen)

dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict2)

## Accessing dictionary pairs
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)

## looping over sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))