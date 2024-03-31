x= float(input("enter the 1st num:"))
y= float(input("enter the 2nd num:"))
def Rem(x,y):
    result= x%y
    print(f"The reminder of {x} and {y} numbers is:{result}")
def sum(x,y):
    result= x+y
    print(f"The sum of {x} and {y} numbers is:{result}")
def sub(x,y):
    result= x-y
    print(f"The sub of {x} and {y} numbers is:{result}")
def multiplication(x,y):
    result= x*y
    print(f"The mxn of {x} and {y} numbers is:{result}")
print("""Please provide user_seldection input
      For add enter 1
      For sub enter 2
      For remainder enter 3
      For multiplication enter 4""" )
user_selection = input("What operation is needed: ")
if(user_selection=="1"):
   sum(x,y)
elif(user_selection=="2"):
   sub(x,y)
elif(user_selection=="3"):
   Rem(x,y)
else:
   if(user_selection=="4"):
        multiplication(x,y)
   else:
      print("wrong input")

#tttstststst

# p= int(input("enter the percentage : "))
# if (50<=p<=60):
#     print("the grade assigned is C")
# elif(60<p<=70):
#     print("the grade assigned is B")
# elif(70<p<=80):
#     print("the grade assigned is A")
# elif(80<p):
#     print("the grade assigned is A++")
# else:
#     print("the grades are too low ,not worth to mention")
      
# userid=int(input("Enter the userid: "))
# if(userid>=5 and userid<=10):
#     print("student is from batch 5")
# else:
#     print("student is not from batch 5")

# eligible="eligible" if 5<=uid<10 else "not eligible"
# print(eligible)

#TEST
