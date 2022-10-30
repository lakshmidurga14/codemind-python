a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    rev=0
    while (t>0):
        r=t%10
        rev=(rev*10)+r
        t=t//10
    if i==rev:
        print(i,end=" ")
