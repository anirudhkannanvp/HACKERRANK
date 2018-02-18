n,t=map(int,input().split())
arr=[]
for i in range(n):
    data=int(input())
    arr.append(data)
arr.sort()
c=0
s=0
for i in range(n):
    s+=arr[i]
    if(s>t):
        break
    c+=1
print(c)