# prime number
x = int(input("Type a number: "))
for i in range(2,int(x)):
    #print(i)
    if x % i ==0:
        print("Not prime")
        break
    else:
        print("prime")
        break
print("End")
