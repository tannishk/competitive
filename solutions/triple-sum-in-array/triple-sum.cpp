#include <bits/stdc++.h>
using namespace std;

int main(){
	int n;
	vector<int> arr;
	cin >> n;
	int x;
	for(int i=0;i<n;i++){
		cin >> x;
		arr.push_back(x);

	}
  int sum;
	cin >> sum;
	
	int l,r;
	sort(arr.begin(), arr.end());
	for(int i=0;i<n;i++){
		l=i+1;
		r=arr.size()-1;
		while(l<r){
			if(arr[i]+arr[l]+arr[r]==sum){
				cout << "The Triplet is: " << arr[i] << " " << arr[l] << " " << arr[r] << endl;
				break;
			}
			else if(arr[i]+arr[l]+arr[r]<sum){
				cout << "We are below our sum" << endl;
				l++;
			}
			else{
				cout << "we are above our required sum." << endl;
				r--;
			}
		}
	}

	return 0;
}
