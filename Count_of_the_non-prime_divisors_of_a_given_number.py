def prime(u):
    f=0
    for i in range(1,u+1):
        if u%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==False:
            c+=1
print(c)