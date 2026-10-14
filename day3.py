#amstrong or not 
num = int(input("Enter your number:"))
numb = str(num)
sum = 0
for i in numb:
    sum += int(i) ** len(numb)
if sum == int(numb):
    print("Armstrong number")
else:
    print("Not Armstrong number") 

#automorphic number or not
num=int(input("enter a number:"))
square=num**2
if str(square).endswith(str(num)):
    print("automorphic number")
else:
    print("not automorphic number") 

#num is neon or not
num=int(input("enter a number:"))
square=num**2
total=0
for i in str(num):
    total+=int(i)
if total==num:
    print("neon num")
else:
    print("not an neon num") 

#pallindrome or not
num=int(input("enter a number:"))
if str(num)==str(num)[::-1]:
  print("pallindrome num")
else:
  print("not a pallindrome num") 

#perfect number or not
num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("perfect number")
else:
    print("not a perfect number") 

