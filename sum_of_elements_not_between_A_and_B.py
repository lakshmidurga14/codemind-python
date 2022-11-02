a=int(input())
l=[int(x) for x in input().split()]
a,b=map(int,input().split())
s=0
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        s=s+l[i]
print(s)
    
    