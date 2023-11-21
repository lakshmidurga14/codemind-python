n=int(input())
l=map(int,input().split())
p=[]
f=[]
for i in l:
    if i==0:
        p.append(i)
    else:
        f.append(i)
print(*(p+f))