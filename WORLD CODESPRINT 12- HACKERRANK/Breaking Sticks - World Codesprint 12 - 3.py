from math import sqrt,ceil
def func(n):
    if(n==0 or n==1):
        return 0
    if(n%2==0):
        return n+func(n//2)
    else:
        temp=ceil(sqrt(n))
        for i in range(3,temp+2,2):
            if(n%i==0):
                return n+func(n//i)
        return n
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=func(a[i])+1
print(ans)