#odd or even number
a=int(input("enter a number:"))
if a/2==0:
    print("even")
else:
    print("odd") 

#positive or negative or zero
num=int(input("enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#largest of two numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print(a,"is largest number")
else:
    print(b,"is largest number")

#voting eligibility
age=int(input("enter your age:"))
if age>=18:
    print("eligible for voting")    
else:
    print("not eligible for voting")

#pass or fail
marks=int(input("enter your marks:"))
if marks>=65:
    print("pass")
else:
    print("fail")

#largest of three num
a=int(input("enter first number:"))
b=int(input("enter second number:"))    
c=int(input("enter third number:"))
if a>b and a>c:
    print(a,"is largest number")
elif b>c:
    print(b,"is largest number")
else:
    print(c,"is largest number") 

#leap year or not
year=int(input("enter a year:"))
if year%4==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year") 

#calculator 
a=int(input("enter a number:"))
b=int(input("enter a number:"))
z=a+b
print("addition:",z) 

#num divisible by 5 or not
num=int(input("enter your number:"))
if num%5==0:
    print("divisible by 5")  
else:
    print("not divisible by 5") 

#student eligible for discount or not
age=int(input("enter your age:"))
if age<=18:
    print("eligible for discount")
else:
    print("not eligible for discount") 

#smallest of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a<b and a<c:
    print(" a is smallest number")
elif b<c:
    print("b is smallest number")
else:
    print("c is smallest number") 

#num div by both 5 and 3
num=int(input("enter your number:"))
if num%5==0 and num%3==0:
    print("divisible by both 5 and 3") 

#last digit of a number
num=int(input("enter your number:"))
last_digit=num%10
print("last digit of a number is 7") 

#sum of first and last digit of a number
num=int(input("enter your number:"))
first_digit=num
while first_digit>=10:
    first_digit=first_digit//10
last_digit=num%10
print("sum of first and last digit of a number is:", first_digit + last_digit) 


#swap two numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
a=a+b
b=a-b
a=a-b
print("after swapping first number is:",a)
print("after swapping second number is:",b) 

#num lies within in a range or not
num=int(input("enter your number:"))
if num>=1 and num<=100:
    print("number lies within the range") 

#check whether a triangle is valid or not
a=int(input("enter first side of triangle:"))
b=int(input("enter second side of triangle:"))
c=int(input("enter third side of triangle:"))
if a+b>c and a+c>b and b+c>a:
    print("triangle is valid")
else:
    print("triangle is not valid")  