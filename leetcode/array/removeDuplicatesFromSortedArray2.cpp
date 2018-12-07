#include <iostream>
using namespace std;
int main(){
		int A[7] = {1,2,2,3,4,4,4};
		int j = 0;
		int num = 0;
		for (int i = 0; i < sizeof(A)/sizeof(*A); i++){
				if(A[j] == A[i]){
						num++;
						if (num < 2){
								A[++j] = A[j];
						}
				}else{
						A[++j] = A[i];
						num = 0;
				}
		}
		
		for (int a= 0; a < j; a++){
				cout << A[a] << " ";
				}
}
