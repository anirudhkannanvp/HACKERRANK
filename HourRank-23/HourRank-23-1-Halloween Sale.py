p,d,m,mon=map(int,input().split())
ans=0
sum1=0
c=0
while(sum1<=mon):
    ans+=1
    sum1+=p
    p-=d
    if(p<m):
        p=m
print(ans-1)