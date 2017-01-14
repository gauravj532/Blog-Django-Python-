#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
      void rotate(vector<vector<int>>& matrix) {
        vector<vector<int> rotated;
        
        for(int i=0;i<matrix.row;i++)
        {
        	for(int j=0;j<matrix.col;j++)
        	{
        		rotated[j][matrix.col-i-1]=matrix[i][j]
        	}
        }
        matrix = rotated
    }
    
};

int main()
{
	Solution a;
	int m,n;
	vector<vector<int> v[2][2];
	// for(int i=0;i<m;i++)
	// {	
	// 	cin>>temp;
	// 	v1.push_back(temp);
	// }
	// for(int i=0;i<n;i++)
	// {	
	// 	cin>>temp;
	// 	v2.push_back(temp);
	// }
	// a.merge(v1,m,v2,n);
	// for(int i=0;i<m+n;i++)
	// 	cout<<v1[i]<<" ";
	v[0][0]=1;v[0][1]=2;
	v[1][0]=3;v[1][1]=4;
	a.rotate(v);
	for(int i=0;i<2;i++){
		for(int j=0;j<2;j++)
			cout<<v[i][j];
		cout<<endl;
	}
}