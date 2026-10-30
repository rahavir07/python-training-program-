'''num=int(input("enter a num:"))
if (num &1==1):
    print("the num is odd")
else:
    print("the num is even")

'''

'''
num=int(input("enter a num:"))
a="the num is odd" if num&1 else "the num is even"
print(a)
'''

'''n=float(input("enter a cgpa:"))
str=input("dept:")
if n>8 and str=='IT':
    print("eligible for training")
else:
    print("not eligibe for training") '''

'''
num="hello world"
print(num*10)
'''
"""n=int(input("enter a number:"))
for i in range(1, 1001):
    print(i,"x",n, "=", n * i)
    """
'''a=int(input("enter a num1:"))
b=int(input("enter a num2:"))
for i in range(a,b):
    if i/i:
        print(i)
    else:
        print("no prime numbers")'''

'''
#what the prime num and how many 
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

count = 0
for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            count += 1

print("Count of prime numbers:", count)
'''
'''
#duplicate char
s=input("enter a string:")
for i in s:
    if i in s[s.index(i)+1:]:
        print(i)
        break
'''

'''#first non-repetative char
s=input("enter a string:")
for i in s:
    if s.count(i)==1:
        print(i)
        break '''
'''#print last 3 char in str:
a=input("enter a string:")
print(a[-3:])'''

'''#remove ordinary space(using replace)
text="H ello world"
print(text.replace(" ",""))'''

'''#using join and replace
text="H ello world"
print("".join(text.split()))'''

'''#count the words
a=input()
b=a.split()
print(len(b))
'''


'''#using loop
a=input("enter a string:")
count=0
for i in a.split():
    count+=1
print(count)'''

'''#count vowels and consonants only Bulit in method :
a=input("enter a string:")
vowels=0
consonants=0
for i in a.upper():
    if i in "AEIOU":
        vowels+=1
    elif i.isalpha():
        consonants+=1
print("vowels:",vowels)
print("consonants:",consonants)'''

        
'''#count vowels and consonants only native method :
a=input("enter a string:")
vowels=0
consonants=0
for i in a.upper():
    if i in "AEIOU":
        vowels+=1
    elif 'A' <= i <= 'Z':
        consonants+=1
print("vowels:",vowels)
print("consonants:",consonants)'''

'''#count words starting with a vowels:
a=input("enter a string:")
count=0
for word in a.split():
    if word[0].lower() in "aeiou":
        count+=1
print("starting words of a vowel:",count)'''

'''#replace vowels with"*":
a=input("enter a string:")
b=""
for i in a:
    if i.lower() in "aeiou":
        b+="*"
    else:
        b+=i
print(b)'''

'''#reverse each word without changing word order:
#input:Hello world
#output:ooleH dlrow
s = input("Enter a string: ")
words = s.split()
for i in words:
    print(i[::-1], end=" ")'''

'''#anagram:
a=input("enter first string:")
b=input("enter second string:")
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")'''

'''#jewels and stones:
jewels=input("enter a jewels:")
stones=input("enter a stones:")
count=0
for i in stones:
    if i in jewels:
       count+=1
print(count)'''

'''#Toggle case without using swapcase (ASCII):
s = input("Enter a string: ")
result = ""
for i in s:
    if 'A' <= i <= 'Z':
        result += chr(ord(i) + 32)
    elif 'a' <= i <= 'z':
        result += chr(ord(i) - 32)
    elif '0' <= i >= '9':
        result += i
print(result)

#using mtehod:
s = input("Enter a string: ")
result = ""
for i in s:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
print(result)'''


'''#most frequent charcter no multiple char
a=input("enter a string:")
max_count=0
result=""
for i in a:
    count=a.count(i)
    if count>max_count:
        max_count=count
        result=i
print(result)'''

'''#first pallindrome in a string:
s=input().split()
for i in s:
    if i==i[::-1]:
        r=i
        break
    else:
        r=""
print(r)'''

'''#print in a same line:
subjects = ["python", "Java", "C", "SQL"]
for subject in subjects:
    print(subject, end=" ")'''


'''# calculate total and avg:
n = int(input("How many subjects? "))
total = 0

for i in range(n):
    a =int(input("Enter a mark: "))
    total = total + a

average = total / n

print("Total:", total)
print("Average:", average)'''

'''# by using append()
a=[]
sub=int(input("no.of.sub:"))
for i in range(sub):
    num=int(input("enter the marks:"))
    a.append(num)
sum=0
for i in a:
    sum=sum+i
avg=sum/sub
print(sum)
print(sub)'''

'''#sum the ranges:
a=[]
n=int(input("total no of n:"))
for i in range(n):
        a.append(i)
sum=0
for i in a:
    sum=sum+i
print(sum)'''

'''#find min and max without using bulit-in function:
small = int(input("Enter a number: "))
large = small

for i in range(4):
    a = int(input("Enter a number: "))

    if a < small:
        small = a
    if a > large:
        large = a

print("Minimum:", small)
print("Maximum:", large)'''

'''#getting input directly:
a=[95,80,97,96,99]
highest=a[0]
lowest=a[0]
for num in a:
    if num>highest:
        highest=num
    if num<lowest:
        lowest=num
print("highest num:",highest)
print("lowest num:",lowest)'''


'''#TUPLES:
a = ()
n = int(input("How many numbers? "))
for i in range(n):
    b = int(input("Enter a number: "))
    a = a + (b,)
x = int(input("Enter number to count: "))
print(a.count(x))'''

'''#word is equal to substring of another word
words = input().split()
result = []
for i in words:
    for j in words:
        if i != j and i in j:
            result.append(i)
            break
print(result)'''


'''#move zeroes:
nums=eval(input())
a = []
for i in nums:
    if i != 0:
        a.append(i)
for i in nums:
    if i == 0:
        a.append(i)
print(a)'''

'''#count vowels:
a = input("Enter a word: ")
count = 0
for i in a:
    if i in "aeiouAEIOU":
        count += 1
print("Vowel count:", count)'''


'''#rearange a string:
words = input().split()
result = []

for i in range(1, len(words) + 1):
    for j in words:
        if str(i) in j:
            result.append(j[:-1])

print(" ".join(result)'''


'''#half the word check the vowels are equal:
s=input()
vowels="aeiouAEIOU"
mid=len(s)//2
a=s[:mid]
b=s[mid:]
count1=0
count2=0
for i in a:
    if i in vowels:
        count1+=1
for j in b:
    if j in vowels:
        count2+=1
print(count1==count2)'''


'''#add the next num:
nums = eval(input())
result = []
total = 0
for i in nums:
    total += i
    result.append(total)
print(result)'''

'''#get a input as a string store a unique words in a list:
a=input().split()
b=set(a)
print(list(b))'''


    



            


                  
