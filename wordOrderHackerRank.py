num = int(input("Enter an integer n:"))
set1 = {}
for i in range(1,num+1):
    n=input("Enter values:")
    if n in set1:
        set1[n]=set1[n]+1
    else:
        set1[n]=1
print(len(set1))
print()
for i in set1:
    print(set1[i],end=" ")
