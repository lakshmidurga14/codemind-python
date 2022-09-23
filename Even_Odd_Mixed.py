n=int(input())
m=n%10
k=n//10
r=k%10
l=k//10
j=l%10
v=l//10
if(m%2==0 and r%2==0 and j%2==0):
    print("Even")
elif(m%2!=0 and r%2!=0 and j%2!=0):
    print("Odd")
else:
    print("Mixed")