n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=[-1]*n
ans1=[[-1,-1,-1]]*n
def cost(arr,l,r):
    ans=0
    maxi=arr[l]
    mini=arr[l]
    eor=arr[l]
    eand=arr[l]
    for i in range(l+1,r):
        maxi=max(arr[i],maxi)
        mini=min(arr[i],mini)
        eor|=arr[i]
        eand&=arr[i]
    return eor-eand-maxi+mini
for i in range(n):
    for j in range(i,n):
        #arr1=arr[i:j+1]
        cost1=cost(arr,i,j+1)
        if(cost1>=k):
            for k1 in range(i,j+1):
                if(ans[k1]<j+1-i):
                    ans[k1]=j+1-i
print(*ans,sep="\n",end="\n")