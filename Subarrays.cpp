#include <bits/stdc++.h>
using namespace std;

void Subarrays(vector<int>&A, vector<vector<int>>&ans,vector<int>temp,int index, int n)
{
    if(index==n)
    {
        ans.push_back(temp);
        return;
    }
    
    Subarrays(A,ans,temp,index+1,n);
    temp.push_back(A[index]);
    Subarrays(A,ans,temp,index+1,n);
    temp.pop_back();
    
}

int main() {
	int n;
	cin>>n;
	vector<int>A(n);
	for (int i=0;i<n;i++)
	    cin>>A[i];
	 vector<vector<int>>ans;
	 vector<int>temp;
	 
	 Subarrays(A,ans,temp,0,n);
	 
	 for (int i=0;i<ans.size();i++)
	 {
	     for (int j =0;j<ans[i].size();j++)
	     {
	         cout<<ans[i][j]<<" ";
	     }
	     cout<<"\n";
	 }
    
    return 0;
}
