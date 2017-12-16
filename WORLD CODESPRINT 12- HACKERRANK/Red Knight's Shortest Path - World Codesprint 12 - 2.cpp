#include"bits/stdc++.h"
using namespace std;
typedef long int ll;


ll hor[] = {-2,-2,0,2,2,0};
ll ver[] = {-1,1,2,1,-1,-2};

bool isvalid(ll x,ll y,ll n){
    if(x<0 || y<0 || x>=n || y>=n)
        return false;
    return true;
}

struct Node
{
ll x;
ll y, dist;
ll pathx[2000];
ll pathy[2000];
/*Node(){
    for(ll i=0;i<2000;i++)
    {
        pathx.push_back(0);
        pathy.push_back(0);
    }
}*/
bool operator<(const Node& o) const
{
return x < o.x || (x == o.x && y < o.y);
}
};

Node maans;

ll BFS(Node src, Node dest,ll n)
{
map<Node, bool> visited;
queue<Node> q;
q.push(src);
while (!q.empty())
{
Node top = q.front();
q.pop();
if (top.x == dest.x && top.y == dest.y){
maans=top;
return top.dist;
}
if (!visited.count(top))
{
visited[top] = true;
ll j;
for (j=0;j<6;j++) 
{
if (isvalid(top.x+hor[j],top.y+ver[j],n)){
    Node now=top;
    now.x=top.x+hor[j];
    now.y=top.y+ver[j];
    now.dist=top.dist+1;
    now.pathx[top.dist]=hor[j];
    now.pathy[top.dist]=ver[j];
q.push(now);
}
}
}
}
return LONG_MAX;
}

int main()
{
ios_base::sync_with_stdio(false);
cin.tie(0);
ll n,i,j,stx,sty,endx,endy;
cin>>n;
cin>>stx>>sty>>endx>>endy;
Node src,dest;
src.x=stx;src.y=sty;
dest.x=endx;dest.y=endy;
ll ans=BFS(src,dest,n);
if(ans==LONG_MAX)
cout<<"Impossible"<<"\n";
else
{
cout<<ans<<"\n";
 //cout<<maans.pathx[0]<<" "<<maans.pathy[0]<<"\n";
for(i=0;i<ans;i++){
    if(maans.pathx[i]==-2 && maans.pathy[i]==-1)
        cout<<"UL"<<" ";
     if(maans.pathx[i]==-2 && maans.pathy[i]==1)
        cout<<"UR"<<" ";
     if(maans.pathx[i]==0 && maans.pathy[i]==2)
        cout<<"R"<<" ";
     if(maans.pathx[i]==2 && maans.pathy[i]==1)
        cout<<"LR"<<" ";
     if(maans.pathx[i]==2 && maans.pathy[i]==-1)
        cout<<"LL"<<" ";
     if(maans.pathx[i]==0 && maans.pathy[i]==-2)
        cout<<"L"<<" ";
}
}
return 0;
}
