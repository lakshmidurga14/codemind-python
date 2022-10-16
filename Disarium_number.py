n=int(input())
m=str(n)
l=len(m)
Temp = n
Sum = 0
rem = 0
while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem**l)
    Temp = Temp // 10
    l= l- 1
if Sum == n:
    print("True")
else:
    print("False")