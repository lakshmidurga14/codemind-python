n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(1,len(l)-1):
    if l[i-1]%2==0 and l[i]%2==0 and l[i+1]%2==0:
        c+=1
print(c)