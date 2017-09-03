n,m,k=map(int,input().split())
a=list(map(int,input().split()))
#a.insert(0,-1)
ans=0
c=1
che=[]
suma=[]
cou=0
first=a.index(1)
ans+=(first)
for i in range(n):
    if(a[i]==1):
        che.append(i)
        cou+=1
for i in range(1,cou):
    if(c==m):
        #print("c",c,ans)
        break
    c+=1
    t1=che[i]-che[i-1]
    ans+=t1*(c-1)*k
answer=ans
#print(answer)
for i in range(m,cou):
    diff=che[i-m+1]-che[i-m]-((che[i-1]-che[i-m])*k)+((che[i]-che[i-1])*(m-1)*k)
    ans+=diff
    #print([ans])
    answer=min(answer,ans)
if(cou<m or m>n):
    print(-1)
else:
    print(answer)