num = int(input())  
sum = 0  
temp = num  
while(temp > 0):  
    fact = 1  
    rem = temp % 10 
    for i in range(1, rem + 1):  
        fact = fact * i  
    sum = sum + fact  
    temp = temp // 10
if (sum == num):  
    print("The number",num, "is a strong number")  
else:  
    print("The number",num, "is not a strong number")  