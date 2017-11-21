#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ll n,minvalue=LLONG_MAX;
    cin >> n;
    char name[1000000],name1[1000000];
    for(ll a0 = 0; a0 < n; a0++){
        ll value,value1,fcou=0,secou=0,dig=0;
        cin >> name >> value;
        value1=value;
        while(value1!=0){
            dig+=1;
            int temp=value1%10;
            if(temp==4)fcou+=1;
            if(temp==7)secou+=1;
            value1/=10;
        }
        if(minvalue>value && fcou==secou && fcou*2==dig){
            //cout<<minvalue<<"\n";
            strcpy(name1,name);
            minvalue=value;
            //cout<<value<<"\n";
        }
        
    }
    if(minvalue!=LLONG_MAX)cout<<name1;
    else cout<<"-1";
    return 0;
}