n=int(input())
l=[int(x) for x in input().split()]
a=int(input())
s=0
for i in l:
    s+=i
    if i==a:
        break
print(s)
