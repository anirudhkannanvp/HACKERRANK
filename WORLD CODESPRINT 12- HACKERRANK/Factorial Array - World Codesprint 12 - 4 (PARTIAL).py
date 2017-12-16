from math import factorial
mod=1000000000
n,m=map(int,input().split())
arr=list(map(int,input().split()))
while(m):
    m-=1
    a,b,c=map(int,input().split())
    if(a==1):
        for i in range(b-1,c):
            arr[i]+=1
    elif(a==2):
        ans=0
        for i in range(b-1,c):
            ans+=factorial(arr[i])
            ans%=mod
        print(ans%mod)
    else:
        arr[b-1]=c