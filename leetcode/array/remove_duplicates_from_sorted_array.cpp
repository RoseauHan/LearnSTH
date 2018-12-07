#include <iostream>
using namespace std;
int main(){
		int test[5]={1,2,2,4,5};
		int size = sizeof(test) / sizeof(test[0]);
		cout << size << endl;

		int index = 1;

		for (int i = 1; i < size; i++){
				if (test[i] != test[index-1]){
						test[index++]=test[i];
				}
		}

		for (auto &w :test){
				cout << test[w];
		}
}
