a=int(input())
b=int(input())
s=0
m=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        m+=j
if a==m and b==s:
    print("Amicable")
else:
    print("Not Amicable")