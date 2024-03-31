# write a program idf a user is eligible to enter our class or not . userid should be in between 5 and 10

# uid = int(input("Please enter your user ID: "))
# # if (5<=uid>10):
# #    print("You are eligible for Batch 5")
# # # elif (uid>10):
# # #    print("You are not eligible for Batch 5")
# # else:
# #    print("You are not eligible for Batch 5")

# #ternrary operator 
# eligible="eligible" if 5<=uid<10 else "not eligible"
# print(eligible)
# loops in python
#with the fixed number-- to print first 10 natural numbers
# for loop
# for i in range(100,1,-25):
#     print(i)
# condition
i=0
# while(i<=10):
#     print(i)
#     i=i+1

# for i in range(10):

    
#     if (i==5):
#         break
#     print(i)
# print("outside the loop)")

# for i in range(10):
#     print(i)
# i=2
# print(i*2)
# for i in range(15):
#     print(i)
# print(i)
# data structure
# list,set,tuples,dictionary
# list1=[23,24,20,19,25,67.90,[1,2,3]]
# str="shakulmalik1234 prerna"
# # index
# print(list1[-2])
# print(str[-2])
# # slicing
# print(list1[4:1:-1])
# print(str[2:6])#akul
# print(str[7:2:-2])#alk
# print(str[-3])#r
# print(list1[1:])#24 onwards
# print(list1[:-1])#leaving the last value
# print(str[::-1])
# list2=[2,4,6,8,10,11,13,15]
# for i in list2[5:]:
#          print(i*i)
# list1=[1,2,3,4,5,6,7,8,9,10]
# # for i in list1:
# #      if (i%2!=0):
# #        print (i)
# #change the values
# list1[5]=600
# list1.append(5000)
# list1.insert(3,10000)
# print(list1)
# list1.pop(3)
# del list1[3]
# list1.remove(600)
# print(list1)
# l=[1,2,[3,4,5],6,[7,8,9]]
# # for i in l:
# #      for j in i:
# #         print(j)   


# for i in l:
#     if isinstance(i, list):
#         for j in i:
#             print(j)
#     else:
#        print(i)
list1=[]
while(True):
    num=input("enter the value :-  ")
    list1.append(num)
    choice= input("do you want to enter the values (y/n):-  ")
    if (choice=='n'):
        break
print(list1)
    


