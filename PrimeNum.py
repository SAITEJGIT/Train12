x=int(input("Enter the number:"))
if(x==1):
    print(f"{x} is not a prime number")
elif(x>1):
    for i in range(2,x):
        if(x%i)==0:
            print(f" {x} is not a prime number")
        break
    else:
        
            
        #TTESTSTSST
