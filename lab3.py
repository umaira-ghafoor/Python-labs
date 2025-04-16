#program 1
for i in range(1500,2701):
    if(i%5==0 and i%7==0):
        print(i)

#program 2
c=int(input("enter temp in celsius:"))
f=int(input("enter temp in fahrenheit:"))
temp1=(f-32)*(5/9)
print("Temperature from cel to far",temp1)
temp2=(c*(9/5))+32
print("Temperature from far to cel",temp2)

#program 3
import random
num=random.randint(1,9)
while True:
   n=int(input("Guess number:"))
   if n==num:
      print("Well Guessed")
      break
   else:
      print("Try Again")

#program 4
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for x in range(4,0,-1):
    for y in range(x):
        print("*",end=" ")
    print()

#program 5
str=input("enter word:")
str=str[::-1]
print(str)

#program 6
even=0
odd=0
num=(1,2,3,4,5,6,7,8,9)
for i in num: 
 if(i%2==0):
    even=even+1
 else:
    odd=odd+1
print("Even numbers:",even)
print("Odd numbers:",odd)

#program 7
detalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"classs":'V',"section":'A'}]
for i in detalist:
   print(f"Item:{i},Type:{type(i)}")

#program 8
for i in range(0,7):
   if(i==3 or i==6):
      continue
   else:
      print(i,end=" ")
print()

#program 9
a=0
b=1
for i in range(0,51):
   c=a+b
   print(c,end=" ")
   a=b
   b=c
print()
for i in range(1,51):
   if(i%3==0 and i%5==0):
      print("FizzBuzz")
   elif(i%3==0):
      print("Fizz")
   elif(i%5==0):
      print("Buzz")
   else:
      print(i)

#program 10
m=int(input("enter a number of rows:"))
n=int(input("enter a number of col:"))
result=[[i*j for j in range(n)] for i in range(m)]
print(result)

#program 11
line=[]
while True:
   n=input("enter line:")
   if n=="":
      break
   line.append(n.lower())
for n in line:
   print(n)

#program 12
bin=(input("enter 4 digits binary number:")).split(",")
for i in bin:
   dec=int(i,2)
   if(dec%5==0):
      print(i,end=",")

#program 13
str=input("enter string:")
letters=0
digits=0
for i in range(str):
   if i.isalpha():
      letters+=1
   elif i.isdigit():
      digits+=1
print("Letters:",letters)
print("Digits:",digits)

#program 14
import re
password=input("enter pssword:")
if(6<=len(password)<=16 and 
   re.search(r"[a-z]",password) and
   re.search(r"[A-Z]",password) and
   re.search(r"[0-9]",password) and
   re.search(r"[$#@]",password)):
   print("Valid Password")
else:
   print("Invalid Password")


      


   
   
    

      

