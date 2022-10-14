t=int(input())
for i in range(t):
    n=int(input())
    a=n
    while True:
        is_prime=True
        for j in range(2,int(a**0.5)+1):
            if a%j==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            a+=1
    b=n
    while True:
        is_prime=True
        for j in range(2,int(a**0.5)+1):
            if b%j==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            b-=1
    d=a-n
    c=n-b
    if d<c:
        print(a)
    else:
        print(b)
        