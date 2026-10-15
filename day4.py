#peterson num or not
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == temp:
    print("Peterson number")
else:
    print("Not a Peterson number")

#duck number or not

n = input("Enter a number: ")

if '0' in n and n[0] != '0':
    print("Duck number")
else:
    print("Not a Duck number")

#happy number or not

n = int(input("Enter a number: "))

while n != 1 and n != 4:
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** 2
        n = n // 10

    n = sum

if n == 1:
    print("Happy number")
else:
    print("Not a Happy number") 

#diamond pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


#hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 
