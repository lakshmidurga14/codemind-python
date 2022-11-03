def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
a=int(input())
mp=True
if prime(a)==True:
    while a>0:
        r=a%10
        if prime(r)==False:
            mp=False
            break
        a=a//10
    if mp==True:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")