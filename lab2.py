# Program 1
# Python program to illustrate
# while loop
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

# Program 2
# Python program to illustrate
# Single statement while block
# count = 0
# while count == 0:
#     print("Hello Geek") 
# Infinite loop

# Program 3
# Python program to illustrate
# Iterating over a list
print("List Iteration")

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Program 4
# Iterating over a tuple (immutable)
print("\nTuple Iteration")

t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Program 5
# Iterating over a String
print("\nString Iteration")

s = "Geeks"
for i in s:
    print(i)

# Program 6
# Python program to illustrate
# Iterating by index
list = ["geeks", "for", "geeks"]
for index in range (len(list)):
    print (list[index])

# Program 7
# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print ('Current Letter :', letter)
    var = 10

# Program 8
for letter in 'geeksforgeeks':
# break the loop as soon it sees 'e' # or 's'
    if letter == 'e' or letter == 's':
        break
print ('Current Letter :', letter)

# Program 9
def my_function():
    print("Hello from a function")
my_function()

# Program 10
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Program 11
def my_function(country ="Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Program 12
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Program 13
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Program 14
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Program 15
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Program 16
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
