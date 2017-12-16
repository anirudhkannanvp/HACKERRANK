t=int(input())
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    a.sort()
    for i in range(1,n):
        ans+=abs(a[i]-a[i-1])
    print(ans)