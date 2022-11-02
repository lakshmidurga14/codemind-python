n=int(input())
l=[int(x) for x in input().split()]
k=0
m=0
for i in l:
    if i%2==0:
        print(i,end=" ")
for i in l:
    if i%2!=0:
        print(i,end=" ")