n=int(input())
pos=list(map(int,input().split()))
no=list(map(int,input().split()))
racks=[]
for i in range(n):
    racks.append([pos[i],no[i]])
racks.sort()
l=0
r=0
left=[0]*n
right=[0]*n
left[0]=1
for i in range(n):
    if(left[i]):
        val=pos[i]+no[i]
        for j in range(i+1,n):
            if(pos[j]<=val):
                left[j]=1
l=left[n-1]
right[n-1]=1
for i in range(n-1,-1,-1):
    if(right[i]):
        val=pos[i]-no[i]
        for j in range(i-1,-1,-1):
            if(pos[j]>=val):
                right[j]=1
r=right[0]
if(l and r):
    print("BOTH")
elif(l):
    print("LEFT")
elif(r):
    print("RIGHT")
else:
    print("NONE")