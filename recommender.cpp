#include<bits/stdc++.h>
#include <fstream>

using namespace std;
#define endl "\n"

int main()
{
	ios_base:: sync_with_stdio(false); cin.tie(0);
	ifstream _data ("./data/ml-latest-small/ratings.csv", ios_base::in);

	string temp="";
	int fg=0;
	while(_data){
		_data>>temp;
		cout<<temp<<endl;
		
		if(fg)break;
		fg=1;
	}
	return 0;
}