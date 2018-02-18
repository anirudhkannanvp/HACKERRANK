#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll maxi=LLONG_MIN,sumi=0;

typedef struct node{
    ll data,h,st;
    struct node *left;
    struct node *right;
}NODE;
 
NODE *insert(NODE *root,ll data)
{   
    if(root==NULL)
    {   
        NODE * root=(NODE *)malloc(sizeof(NODE));
        root->right=NULL;
        root->left=NULL;
        root->data=data;
        root->st=1;
        return root;
    }
    else if(root->data >data)
    {
    root->left=insert(root->left,data);
    return root;
    }
    else if(root->data <data)
    {
    root->right=insert(root->right,data);
    return root;
    }
    else{
        return root;
    }
}
 

ll height(NODE *root)
{
     if (root==NULL) 
       return 0;
   else
   {
       ll lDepth = height(root->left);
       ll rDepth = height(root->right);
       
       if (lDepth > rDepth) 
           return(lDepth+1);
       else return(rDepth+1);
   }
}
 

void printPreorder(struct node* node)
{   
     if (node == NULL)
          return;
     if(node->left!=NULL)
     node->left->h=node->h-1;
     if(node->right!=NULL)
     node->right->h=node->h-1;
     printPreorder(node->left);
     //cout<<node->data<<"\n";
     printPreorder(node->right);
}    

void printPreorder1(struct node* node)
{   
     if (node == NULL)
          return;
     if(node->st)
     sumi+=height(node)-1;
     //cout<<node->data<<" "<<height(node)-1<<" "<<node->st<<"\n";
     node->st=0;
     printPreorder1(node->left);
     printPreorder1(node->right);
}    
 

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll n,data;
    cin>>n;
    NODE *root=NULL;
    while(n--)
    {
        cin>>data;
         root=insert(root,data);
    }
    ll he=height(root)-1;
    //cout<<he;
    root->h=he;
    printPreorder(root);
    printPreorder1(root);
    cout<<he<<"\n"<<sumi;
return 0;
}