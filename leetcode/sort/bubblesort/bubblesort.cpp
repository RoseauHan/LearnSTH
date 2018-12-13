#include <iostream>
#include <vector>

using namespace std;

vector<int> bubbleSort(vector<int> list){
		vector<int> result;
		if (list.empty()){
				return result;
		}

		result = list;
		int temp;

		for (int i = 0; i < result.size() - 1; ++i){
				cout << "the" << i + 1 << "times sort" << endl;
				for (int j = 0; j < result.size() - 1; j++){
						if (result[j + 1] < result[j]){
								temp = result[j + 1];
								result[j + 1] = result[j];
								result[j] = temp;
						}
						cout << "sorting...";
						for (int s = 0; s < result.size(); s++){
								cout << result[s] << " ";
						}
						cout << endl;
				}
				cout << "sort result:";
				for (int s = 0; s < result.size(); s++){
						cout << result[s] << " ";
				}
				cout << endl;
		}
		return result;
}

int main(){
		int arr[] = {6, 4, 8, 1, 2, 3, 9};
		vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
		cout << "before:" << endl;
		for (int i = 0; i < test.size(); i++){
				cout << test[i] << " ";
		}
		cout << endl;
		vector<int> result;
		result = bubbleSort(test);
		cout << "waiting..." << endl;
		for (int i = 0; i < result.size(); i++){
				cout << result[i] << " ";
		}
		cout << endl;
		system("pause");
}
