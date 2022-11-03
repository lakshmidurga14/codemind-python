n=int(input())
a=abs(n)
r=0
rev=0
while a>0:
    r=a%10
    rev=rev*10+r
    a=a//10
if n>0:
    print(rev)
else:
    print(-rev)
    