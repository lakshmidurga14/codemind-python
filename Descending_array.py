a=int(input())
l=[int(x) for x in input().split()]
z=sorted(l,reverse=True)
if z==l:
    print("yes")
else:
    print("no")