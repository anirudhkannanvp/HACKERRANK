n=int(input())
a=list(map(int,input().split()))
ans=-11111111111111111111111111111111111111
for i in range(n):
        for j in range(i+1,n):
            if(a[i]<a[j]):
                for k in range(j+1,n):
                    if(a[i]<a[j] and a[j]<a[k]):
                        ans=max(ans,a[i]*a[j]*a[k])
if(ans==-11111111111111111111111111111111111111):
    print("-1")
else:
    print(ans)