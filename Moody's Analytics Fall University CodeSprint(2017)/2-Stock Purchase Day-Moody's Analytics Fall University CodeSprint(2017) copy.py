n=int(input())
a=list(map(int,input().split()))
minimuma=[0]*n
minimuma[n-1]=a[n-1]
for i in range(n-2,-1,-1):
    minimuma[i]=min(minimuma[i+1],a[i])
q=int(input())
while(q):
    q-=1
    i=int(input())
    st=0
    ans=-1
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(i>=minimuma[mid]):
            ans=max(ans,mid+1)
            low=mid+1
        else:
            high=mid-1
    print(ans)