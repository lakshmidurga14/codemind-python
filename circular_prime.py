def prime(u):
    f=0
    for i in range(1,u+1):
        if u%i==0:
            f=f+1
    if f==2:
        return True
    else:
        return False
def rev(u):
    s=0
    k=u
    while u>0:
        r=u%10
        s=s*10+r
        u=u//10
    return s
n=int(input())
m=rev(n)
if prime(n)==True and prime(m)==True:
    print("circular prime")
elif prime(n)==True:
    print("prime but not a circular prime")
else:
    print("not prime")