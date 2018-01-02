from math import gcd
def func1(a1,b1):
    return gcd(a1,b1)
def func(a,n):
    gcd1=a[0]
    for i in range(1,n):
        gcd1=func1(gcd1,a[i])
    sum1=0
    maxi=max(a)
    for i in range(n):
        sum1+=a[i]
    ans=gcd1*(sum1-maxi)
    return ans
n=int(input())
a=list(map(int,input().split()))
ans=-1
for i in range(n):
    for j in range(i,n):
        ans=max(ans,func(a[i:j+1],j-i+1))
print(ans)