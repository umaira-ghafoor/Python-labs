# Program 1
x=1
# The initial value of x is 1
if x>0:
    print("These are two comments") #Print a string

# Program 2
txt = input("Enter a string: ")
print(txt)

# Program 3
print("Statement1")
print("Statement2")

# You can write the above two statements in the following way
print("Statement1");print("Statement2")

# Program 4
x = 1

if x == 1:
 print("This statement has a single space indentation")
 print("This statement has a single space indentation")

# Program 5:
x = 1

if x == 1:
    print("This statement has a single tab indentation")
    print("This statement has a single tab indentation")

# Program 6:
x = 1

if x == 1:
    print("This statement has a single space+tab indentation")
    print("This statement has a single space+tab indentation")

# Program 7:
a = 1
print(type(a))

b = -4587
print(type(b))

c = 0
print(type(c))

g = 1.03
print(type(g))

h = -11.23
print(type(h))

i = .34
print(type(i))

j = 2.12e-10
print(type(j))

k = 5E220
print(type(k))

# Program 8:
x = complex(1, 2)
print(type(x))
print(x)

z = 1 + 2j
print(type(z))

# Program 9:
x = True
print(type(x))

y = False
print(type(y))

# Program 10:
str1 = "String"  # String starts and ends with double quotes
print(str1)

str2 = 'String'  # String starts and ends with single quotes
print(str2)

str3 = "Day's"  # Single quote within double quotes
print(str3)

str4 = 'Day"s'  # Double quote within single quotes
print(str4)

# Program 11:
print("This is a backslash (\\) mark.")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")

#Program 12:
string1 = "PYTHON TUTORIAL"

print(string1[0])  # Print first character
print(string1[-15])  # Print first character
print(string1[14])  # Print last character
print(string1[-1])  # Print last character
print(string1[4])  # Print 4th character
print(string1[-11])  # Print 4th character

# Program 13:
my_list1 = [5,12,13,14]  # the list contains all integer values
print(my_list1)

my_list2=['red','bllue','black','white']  # the list contains all string values
print(my_list2)

my_list3=['red',12,112,12]  # the list contains a string, an integer, and a float values
print(my_list3)

# Program 14:
color_list=['red','blue','green','black']  # the list has four elements; indices start at 0 and end at 3
print(color_list[0],color_list[3])  # Print first and last elements
print(color_list[-1])  # Print last element
# print(color_list[4])  # Creates error as index is out of range

# Program 15:
color_list=['red','blue','green','black']  # the list has four elements; indices start at 0 and end at 3
print(color_list[0:2])  # Cut first two items
print(color_list[1:2])  # Cut second item
print(color_list[1:-2])  # Cut second item
print(color_list[:3])  # Cut first three items
print(color_list[:])  # Create a copy of the original list
