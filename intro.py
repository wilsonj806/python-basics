# Comments are done with the pound
print("Hello World");

# Basic variables
num = 2;
print(num + num);

# Strings
## Note you don't need the semi-colon
string = "Hello there!"
print(string)

# String concat
newSection = " General Kenobi. You are a bold one!"
print(string + newSection);

# String indexing
print(string[3])

# String index from the right
## note the negative indicates you start from the other side
## Also note that it doesn't start from -0
print(string[-1])

# String slicing
print(string[:4])
print(string[6:9])

# Lists
newList = ['a', 'b', 'c']
print(newList)
newList[2] = 'x'
print(newList)
newList.append(33)
print(newList)
print(len(newList))
