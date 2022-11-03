def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if i!=n//i and prime(i)==True and prime(n//i)==True:
            print(i,n//i)
            break
else:
    print(-1)