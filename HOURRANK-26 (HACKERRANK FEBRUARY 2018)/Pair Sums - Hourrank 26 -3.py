n=int(input())
arr=list(map(int,input().split()))
maxsofar=-11111111111111111111111111111111111
maxendhere=0
start=0
end=0
s=0
for i in range(n):
    maxendhere+=arr[i]
    if(maxsofar<maxendhere):
        maxsofar=maxendhere
        start=s
        end=i
    if(maxendhere<0):
        maxendhere=0
        s=i+1
arr1=arr[start:end+1]
#print(end-start)
ans=0
length=end-start+1
arr2=[0]*(length)
suma=sum(arr1)
arr2[0]=suma-arr1[0]
for i in range(1,length):
    arr2[i]=arr2[i-1]-arr1[i]
for i in range(end-start+1):
    ans+=arr1[i]*arr2[i]
print(ans)