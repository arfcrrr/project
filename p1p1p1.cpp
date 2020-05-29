#include <bits/stdc++.h>
using namespace std;

struct factory{
	int cost;
	int revenue;
}; 
int maxRevenue(int budget, vector <factory> &factA, 
			   vector <factory> &factB, vector <factory> &factC){
	int length = factA.size() + factB.size() + factC.size();
	int maxA = factA.size();
	int maxAB = factA.size() + factB.size();
	int result[length+1][budget+1];
	for(int i = 0; i <= budget; i++){
		result[0][i] = 0;
	} 
	//check optimal solution for factory A
	for(int i = 0; i < factA.size(); i++){
		//store temporary cost and revenue
		int idx = i + 1;
		int tc = factA[i].cost;
		int tr = factA[i].revenue;
		for(int c = 0; c <= budget; c++){
			result[idx][c] = result[idx-1][c];
			if(c >= tc && tr > result[idx][c]){
				result[idx][c] = tr;
			}
			cout << " " << result[idx][c];
		}
		cout << endl;
	}
	cout << endl;
	//check optimal solution for factory B 
	//with considering solution of A 
	for(int i = 0; i < factB.size(); i++){
		int idx = i + factA.size() + 1;
		int tc = factB[i].cost;
		int tr = factB[i].revenue;
		for(int c = 0; c <= budget; c++){
			result[idx][c] = result[maxA][c];
			if(c >= tc){
				if(result[maxA][c-tc] + tr > result[idx][c]){
					result[idx][c] = result[maxA][c-tc] + tr;
				}
				else if(i > 0 && result[idx-1][c] > result[idx][c]){
					result[idx][c] = result[idx-1][c];
				}
			}
			cout << " " << result[idx][c];
		}
		cout << endl;
	} 
	cout << endl;
	//check final optimal solution for factory C
	//with considering solution of A and B too
	for(int i = 0; i < factC.size(); i++){
		int idx = i + factA.size() + factB.size() + 1;
		int tc = factC[i].cost;
		int tr = factC[i].revenue;
		for(int c = 0; c <= budget; c++){
			result[idx][c] = result[maxAB][c];
			if(c >= tc){
				if(result[maxAB][c-tc] + tr > result[idx][c]){
					result[idx][c] = result[maxAB][c-tc] + tr;
				}
				else if(i > 0 && result[idx-1][c] > result[idx][c]){
					result[idx][c] = result[idx-1][c];
				}
			}
			cout << " " << result[idx][c]; 
		}
		cout << endl;
	} 
	cout << endl;
	return result[length][budget];
} 
int main(){
	vector <factory> factA =
	{ 
		{0,0}, {2,8}, {3,9}, {4,12}
	};
	vector <factory> factB =
	{ 
		{0,0}, {1,3}
	};
	vector <factory> factC =
	{ 
		{0,0}, {1,5}, {2,6}
	};
	int budget;
	cout << " Input company's budget (in billion) = Rp "; cin >> budget; 
	cout << " Maximum revenue that can be obtained = Rp "
	<< maxRevenue(budget, factA, factB, factC) << " billion";
} 
