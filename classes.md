# Classes
## Overview
This doc overviews classes in Python along with a short intro on scope and closure.

## Scope and Closure
Scoping in Python can be a lot more explicit than in JavaScript. Easier to show than tell:
```py
def scope_test():
  def do_local():
      spam = "local spam"

  def do_nonlocal():
      nonlocal spam
      spam = "nonlocal spam"

  def do_global():
      global spam
      spam = "global spam"

  spam = "test spam"
  do_local()
  print("After local assignment:", spam)
  do_nonlocal()
  print("After nonlocal assignment:", spam)
  do_global()
  print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
So in the above snippet, we declare `spam` three times. Once in a scope that's local to the method, once in a scope that non-local, and again in a global scope.

When we run the python file, we get the below output:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
So for `do_local()`, we get "test spam" because spam is set inside the closure of `do_local()`.

For `do_nonlocal()`, we get "nonlocal spam" because sets spam to that value within the closure of the class `scope_test`.

For `do_global()`, we get "global spam" when we call `do_local()` *and* when we call spam outside the closure we provided by the class, because we set spam in the global namespace instead.

## Class syntax
So classes in Python get their own set of syntax and some other new things that we probably haven't seen in JS.

First, as some review, classes aren't immediately usable, we need to *instantiate* it. In JavaScript, it'd look like:
```js
class Dog {
  constructor(name = 'shib420') {
    this.name = name
  }

  bark() {
    console.log('woof')
  }

  eat() {
    console.log('gib food')
  }
}

const shiba = new Dog('uwu')
```

Classes in Python are declared in a similar way like so:
```py
class ClassName:
  <...statements>
```

We also have two different operations we can have on classes, *attributes* and *instantiation*

Here's an example of both:
```py
class MyClass:
  """A simple example class"""
  i = 12345

  def f(self):
      return 'hello world'
```
So `MyClass.i` and `MyClass.f` are both class attributes.

But then we instantiate a class in a similar way to JavaScript like so:
```py
x = MyClass()
```
Except here, we don't use the `new` keyword whereas JS does.

### Self Referencing in classes
So referencing the current class in Python is actually very different to JS. JavaScript uses `this` to let you reference the current class object, but in Python, we actually pass in a `self` param in any methods we define.

If we `print(self)` in the above example we get:
```
<__main__.MyClass object at 0x10344c390>
```

And if we `print(self.i)` we get "doot".

### More classes
Python also lets you define a constructor like method that gets called on instantiation. Said method is `__init__()` and is where you'd pass in input args like so:
```py
class Doge:
  def __init__(self, name):
    self.name = name

  def echoName():
    print(self.name)

shib = Doge('bernie')
shib.echoName()
```

Note that `self.name` inside the Doge class is an **instance** variable. If we declared `name` outside the scope of `__init__` then it'd be a static variable and thus available to all instances of the Doge class.

Let's update Doge with a static variable real fast:
```py
class Doge:
  is_good_pup = true
  tricks = []
  ...def otherStuff():

shib = Doge('bernie')
print(shib.is_good_pup)
pup = Doge('carl')
print(pup.is_good_pup)
```
When we fetch the `is_good_pup` property from both class instances, we get `True` as the value.

This would also mean that if we mutate `tricks`, then it actually mutates *all instances* of the class like so:
```py
class Doge:
  tricks = []
  def addTrick(self, trick):
    self.tricks.append(trick)

shib = Doge('bernie')
carl = Doge('carl')
carl.addTrick('flip')
print(shib.tricks)
```
And if we run it our `shib` actually gets the 'flip' trick added.