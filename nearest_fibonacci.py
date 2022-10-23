n=int(input())
a1=0
b1=1
c1=a1+b1
while (c1<=n):
    a1=b1
    b1=c1
    c1=a1+b1
if (abs(c1-n)>abs(b1-n)):
    print(b1)
elif (abs(c1-n)==abs(b1-n)):
    print(b1,c1)
else:
    print(c1)