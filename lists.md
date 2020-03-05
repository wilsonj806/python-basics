# More on Lists
## Overview
In Python, lists serve a similar purpose as arrays in JavaScript(JS arrays are *list-like* though).

Check the [Python docs](https://docs.python.org/3/tutorial/datastructures.html) for more.

## Lists as stacks
Python Lists make it easy to use them as stacks, where the last element inserted is the first element retrieved("last-in, first-out"). We use `append()` to add elements and `pop()` to retrieve the last element.

```py
stack = [3,4,5]
stack.append(6)
stack.append(7)

stack

stack.pop()
stack

stack.pop()
stack
```

## Lists as queues
We can also use lists as queues, but this is wildly inefficient as queues are insert and retrieve from the from, so you have to shift everything around.

Python has a built-in `collections.deque` library that performs the above as fast as possible
```py
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)
```

## List Comprehensions
List comprehensions are a quick concise way to make lists. Easier to show than tell:
```py
squares = []
for x in range(10):
  squares.append(x**2)
print(squares)
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]
print(squares3)
```

We can also perform more complex ops like so:
```py
filterArr = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(filterArr)
```

This is equivalent to:
```py
combs = []
for x in [1,2,3]:
  for y in [3,1,4]:
    if x != y:
      combs.append((x, y))
```

## Dictionaries
Dictionaries are basically objects in JS.
```py
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
```

We can also build a dictionary via the constructor like so:
```py
constructed = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```
Or we can use dictionary comprehensions like so:
```py
comprehen = {x: x**2 for x in (2, 4, 6)}
```
Or if we know the keys are strings:
```py
dict2 = dict(sape=4139, guido=4127, jack=4098)
```

We also can use `dictionary.item()` to fetch both the key and value like so:
```py
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
  for k, v in knights.items():
    print(k, v)
```