#include <bits/stdc++.h>

using namespace std;

int surfaceArea(vector < vector<int> > a,int h, int w) {
int ans1=0,ans,i,j;
for(i=0;i<h;i++){
    ans=0;
    for(j=1;j<w;j++){
        ans+=abs(a[i][j-1]-a[i][j]);
    }
    ans1+=ans;
}
//cout<<ans1;
for(j=0;j<w;j++){
    ans=0;
    for(i=1;i<h;i++){
        ans+=abs(a[i-1][j]-a[i][j]);
    }
    ans1+=ans;
}
//cout<<ans1;
for(i=0;i<h;i++){
for(j=0;j<w;j++){
    if(i==0)
    ans1+=a[i][j];
}
}
for(i=0;i<h;i++){
for(j=0;j<w;j++){
    if(i==h-1)
    ans1+=a[i][j];
}
}
for(j=0;j<w;j++){
for(i=0;i<h;i++){
    if(j==0)
    ans1+=a[i][j];
}
}
for(j=0;j<w;j++){
for(i=0;i<h;i++){
    if(j==w-1)
    ans1+=a[i][j];
}
}
//if(h==1 && w==1)ans1=0;
 return ans1+2*h*w; 
}
int main() {
    int H;
    int W;
    cin >> H >> W;
    vector< vector<int> > A(H,vector<int>(W));
    for(int A_i = 0;A_i < H;A_i++){
       for(int A_j = 0;A_j < W;A_j++){
          cin >> A[A_i][A_j];
       }
    }
    int result = surfaceArea(A,H,W);
    cout << result << endl;
    return 0;
}
