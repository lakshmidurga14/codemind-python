n=int(input())
t=n
rev=0
rev1=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
k=rev*rev
while k>0:
    r1=k%10
    rev1=rev1*10+r1
    k=k//10
print(t*t==rev1)