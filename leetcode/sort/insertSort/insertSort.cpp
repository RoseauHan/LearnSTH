#include <iostream>
#include <vector>

using namespace std;
vector<int> insertSort(vector<int> list){
		vector<int> result;
		if (list.empty()){
				return result;
		}
		result = list;
		//第一个数肯定有顺序，所以从第二个数开始
		for (int i = 1; i < result.size(); i++){
				//取出第i个数，和前i - 1个数比较后，插入合适的位置
				int temp = result[i];
				//因为前i - 1个数都是从小到大排序的有序序列，所以只要当前比较的数比temp大，就把这个数后移一位。
				int j = i - 1;
				for (j; j >= 0 && result[j] > temp; j--){
						result[j + 1] = result[j];
				}
				result[j + 1] = temp;
		}
		return result;
}

int main(){
		int arr[] = {6, 4, 8, 9, 2, 3, 1};
		vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
		cout << "Before:" << endl;
		for (int i = 0; i < test.size(); i++){
				cout << test[i] << " ";
		}
		cout << endl;
		vector<int> result;
		result = insertSort(test);
		cout << "After:" << endl;
		for (int i = 0; i < result.size(); i++){
				cout << result[i] << " ";
		}
		cout << endl;
		system("pause");
}
				
