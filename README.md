# Python 101
## Overview
This is a quick Python tutorial repo. Mostly just following the docs and making new `.py` files as needed. Notes will be included as needed.

## Relevant Files
- [Lists](./lists.md)
- [Classes](./classes.md)

## Syntax stuff
Python uses a lot of indenting to do everything so a function/ if-else in JS looks like:
```js
function aaa() {
  if (1 > 2) {
    doStuff()
  } else {
    doOtherStuff()
  }
}
```
While in Python this looks like:
```py
def aaa:
  if 1 > 2:
    doStuff()
  else:
    doOtherStuff()
```

Important to note that the functions and if-else blocks also require a colon at the end of the thing.

ALSO, note that we don't need to append semi-colons to the end of our statements.

## Module importing
Reference the [docs](https://docs.python.org/3/tutorial/modules.html) for more.

Module importing in Python is similar to how JavaScript handles it, but with a couple of differences.

First, if we want to import the entire module, it looks like this:
```py
import fibo
```
Whereas it looks like:
```js
import * as fibo from 'fibo'
```

We can also import specific functions from modules like so:
```py
from fibo import fib, fib2
```

Python also has syntax to import every named export like so:
```py
from fibo import *
fib(33)
fib2(3333)
```