from math import pow
mod=1000000007
t=int(input())
while(t):
    t-=1
    k,a,b=map(int,input().split())
    ans=0
    j=1
    while(j<=b):
        ans+=((b-max(j,a)+1)*j)
        j*=(k)
        j+=1
    print(ans%mod)