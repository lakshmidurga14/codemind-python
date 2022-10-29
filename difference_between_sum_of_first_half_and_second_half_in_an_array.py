n=int(input())
l=[int(x) for x in input().split()]
m=n/2
k=int(m)
a=(n//2)
s=0
b=0
for i in l:
    s+=i
    if m==k and i==m:
        break
    elif m%2!=0 and i==a:
        break
for i in l:
    b+=i
j=b-s
print(abs(s-j))
    
