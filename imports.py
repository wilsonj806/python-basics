# one way
from pkg.module import printMyText
dir(printMyText)
printMyText('doot')

# another way
from pkg import module
dir(module)
module.printMyText('doot')