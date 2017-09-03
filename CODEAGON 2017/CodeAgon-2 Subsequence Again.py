t=list(input())
n=len(t)
k=int(input())
che=[0]*26
for i in range(n):
    che[ord(t[i])-ord('a')]+=1
for i in range(n):
    if(che[ord(t[i])-ord('a')]>=k):
        print(t[i],sep="",end="")