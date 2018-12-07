//Given an array and a value, remove all instances of that value in place and return the new length.
#include <iostream>
using namespace std;
int main(){
		int A[5] = {1,2,3,4,2};
		int n = sizeof(A)/sizeof(*A);
		int value = 2;
		int i = 0;
		int j = 0;

		for ( ; i < n; i++){
				if (A[i] == value){
						continue;
				}
				A[j] = A[i];
				j++;
		}


		for (int t = 0; t < j; t++){ cout << A[t] << " ";}
		cout  << endl << "=======================================" << endl;
		cout << "New length:" << j << endl;
}


