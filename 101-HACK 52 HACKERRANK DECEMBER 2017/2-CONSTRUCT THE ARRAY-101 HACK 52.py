mod=1000000007
n,k,x=map(int,input().split())
bef1=1
befo=0
cur1=1
curo=0
for i in range(n-1):
    cur1=((k-1)*befo)%mod
    curo=(((k-2)*befo)%mod+(bef1%mod))%mod
    bef1=cur1
    befo=curo
if(x!=1):
    print(befo)
else:
    print(bef1)