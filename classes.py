# Scope and closure
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
print()

# A basic class
class MyClass:
  i = 'doot'

  def f(self):
    return 'hello there!'

sampleClass = MyClass()
print(sampleClass.f())
print(sampleClass.i)

## Instance vars
class Doge:
  is_good_pup = True
  tricks = []
  def __init__(self, name):
    self.name = name

  def echoName(self):
    print(self.name)

  def addTrick(self, trick = ''):
    self.tricks.append(trick)

shib = Doge('bernie')
shib.echoName()
print(shib.is_good_pup)

pup = Doge('carl')
pup.echoName()
print(pup.is_good_pup)
print('mutating is good pup')
pup.addTrick('back flip')

print(shib.tricks)