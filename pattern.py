x=int(input("enter a pyramid "))
rows = 5
for i in range(1, rows+1):
    print(i)

    for j in range(1,i+1):
        print("*",end=" ")
    print()    
