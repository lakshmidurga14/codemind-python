a=int(input())
b=int(input())
s=p=0
for i in range(1,a):
    if a%i==0:
        s+=i
for i in range(1,b):
    if b%i==0:
        p+=i
if s==b and p==a:
    print("Amicable")
else:
    print("Not Amicable")