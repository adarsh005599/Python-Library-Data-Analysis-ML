x = int(input("Enter the number: "))

if(x>0):
    print("+ve")
elif(x<0):
    print("-ve")
else:
    print("the number is equal to zero!")
    
for i in range (10):
    if i==4:
        continue
    print(i)