def prime(u):
    if u==1:
        return False
    for i in range(2,(int(u**0.5)+1)):
        if u%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
c=0
for j in range(m,n+1):
    if prime(j)==True:
        c+=1
print(c)