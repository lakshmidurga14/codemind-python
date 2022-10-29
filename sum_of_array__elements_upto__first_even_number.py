n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in l:
    if i%2==0:
        break
    s+=i
print(s)