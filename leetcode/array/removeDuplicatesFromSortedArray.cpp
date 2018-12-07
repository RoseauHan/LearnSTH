//Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length;
#include <iostream>
using namespace std;
int main(){
		int test[5]={1,2,2,3,4};
		int size = sizeof(test) / sizeof(test[0]);
		
		int index = 1;
		for (int i = 1; i < size; i++){
				if (test[i] != test[index-1]){
						test[index++]=test[i];
				}
		}

		for (int i=0; i<index; i++){
				cout << test[i] << " ";
		}
}
