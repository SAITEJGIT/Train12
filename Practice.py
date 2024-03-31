# 1. even or odd #
"""
Num=int(input("Enter a number: "))
if(Num%2==0):
    print(f"{Num} is an even number")
elif(Num<=0):
    print(f"{Num} is an invalid input")
else:
    print(f"{Num} is an odd number")
"""

# 2. Factorial of given number #
"""
Num=int(input("Enter a number: "))
fact=1
if(Num<0):
    print("factorial of a neg number does not exists")
else:
    for i in range(1,Num+1):
        fact*=i
print(f"Factorial of {Num} is : {fact}")
"""

# 3. Prime numbers #
"""
Num=int(input("Enter a number: "))
if(Num<=1):
    print("It is not a prime number")
elif(Num>1):
    for i in range (2,Num):
        if(Num%i==0):
            print(f"{Num} is not a prime number")
            break
    else:
        print("It is a prime number")
"""

# 4. reverse a string #
"""
a=str(input("Enter a string: "))[::-1]

b=list(a)
a=b[::-1]
c=""
for i in a:
    c+=i
print("Reverse of a string is :", c)
"""

"""
a=str(input("Enter a string: "))[::-1]
print("Reverse of a string is:", a)
"""


# # 5. Check if a string is a palindrome #
""""
a=str(input("Enter a string: "))
b=list(a)
d=b[::-1]
c=""
for i in d:
    c+=i
if(c==a):
    print(f"The given string {a} is a palindrome")
else:
    print(f"The given string {a} is not a palindrome")

"""

# # # 6 and 12. Find the largest and smallest number in the list #

"""
n=int(input("enter the length of the list a: "))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
maxi=max(a)
mini=min(a)
print(f"{maxi} is the largest number")
print(f"{mini} is the largest number")
"""

# cmp=0
# for i in a:
#     if(i>=a[0] and i>=a[2] and i>=a[3] and i>=a[4] and i>=a[1]):
#         print(f"{i} is largest number")
#         break

# 7. Find the vowels in a string #
"""
a=str(input("Enter a string: "))
b=list(a)
count=0
for i in b:
     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" ):
        count=count +1
        print(f"The vowels in the string are {i}")
     else:
         print("the given string has no vowels")
         break
print("The number of vowels in a string are", count)      

"""

# 8.

# 9. sum of elements in a list #
"""
n=int(input("enter the length of the list a: "))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
add=0
for i in a:
    add+=i
print(f"The addition for the elements in a list {a} is: {add}")

"""

#10. Length of a string#
"""
a=str(input("Enter a string: "))
print(len(a))

"""

# 11. Avg of elements in a list #

"""
n=int(input("enter the length of the list a: "))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
add=0
for i in a:
    add+=i
AVG=add/n
print((f"The avg for the elements in a list {a} is: {AVG}"))

"""

#.13 to find a given year is a leap year

"""
year=int(input("please enter the year: "))
if(year%4==0 and year%100!=0 and year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

"""

#14. print common elements from two strings ###

"""
n=int(input("enter the length of the list a: "))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)

n=int(input("enter the length of the list c: "))
c=[]
for i in range(n):
    b=int(input())
    c.append(b)
b=set(a)
d=set(c)    
print(b.intersection(d))

"""

# 25. to find the sum of even numbers in a list#
"""

n=int(input("enter the length of the list a: "))
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
add_even=0
for i in a:
    if(i%2==0):
        add_even+=i
if(add_even==0):
    print("No even numbers are present in the list")
else:
       print((f"The sum of even numbers in a list {a} is: {add_even}"))

"""

# 15. fibonocci series #

n=int(input("enter the length of the list a: "))
fib=0
for i in range(n):
    fib=i+fib
    print(fib)
    for j in range(i):
        fib=j+fib
        print(fib)