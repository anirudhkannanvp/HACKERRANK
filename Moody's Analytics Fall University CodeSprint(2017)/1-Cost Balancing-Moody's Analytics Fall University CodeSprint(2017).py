m,n=map(int,input().split())
arr=[0]*(n+1)
m1=m
s=0
while(m):
    m-=1
    a,b=map(int,input().split())
    arr[a]+=b
    s+=b
#print(arr)
aj=s//n
#print(aj)
aj1=s-(aj*n)
arr[1]-=(aj+aj1)
for i in range(2,n+1):
    arr[i]-=(aj)
for i in range(1,n+1):
    print(i,arr[i],end=" ",sep=" ")
    print()