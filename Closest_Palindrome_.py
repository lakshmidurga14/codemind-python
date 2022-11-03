def palin(n):
    s=0
    k=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        return True
    else:
        return False
def prepal(n):
    while palin(n)==False:
        n=n-1
    return n
def nexpal(n):
    while palin(n)==False:
        n=n+1
    return n
l=int(input())
a=prepal(l)
b=nexpal(l)
if palin(l)==True:
    print(prepal(l-1),nexpal(l+1))
elif (l-a)<(b-l):
    print(a)
elif(l-a)>(b-l):
    print(b)
elif (l-a)==(b-l):
    print(a,b)