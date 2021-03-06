// code15_2 f和x的迭代计算.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
using namespace std;
typedef int *IntArrayPtr;
void initialArray(int **a, int d1, int d2);
template<class T>
T max(T a, T b) {
	return a > b ? a : b;
}

template<class T>
void Knapsack(T p[], int w[], int c, int n, T** f) {
	//对于所有i和y计算f[i][y]
	//初始化f[n][y]
	for (int y = 0; y <= w[n]; y++)
		f[n][y] = 0;
	for (int y = w[n]; y <= c; y++)
		f[n][y] = p[n];
	//计算剩下的f
	for (int i = n - 1; i > 1; i--) {
		for (int y = 0; y <= w[n]; y++)
			f[i][y] = f[i + 1][y];
		for (int y = w[i]; y <= c; y++)
			f[i][y] = max(f[i + 1][y], f[i + 1][y - w[i]] + p[i]);
	}
	f[1][c] = f[2][c];
	if (c >= w[1])
		f[1][c] = max(f[1][c], f[2][c - w[1]] + p[1]);
}
template<class T>
void Traceback(T **f, int w[], int c, int n, int x[]){// 计算x 
	for (int i = 0; i < n; i++)
		if (f[i][c] == f[i + 1][c]) x[i] = 0;
		else {
			x[i] = 1;
			c -= w[i];
		}
		x[n] = (f[n][c]) ? 1 : 0;
}

int main()
{
	int n = 4;
	int a[5] = { 2,2,6,5,4 };
	int *w = a;
	int c = 10;
	int b[5] = { 6,3,5,4,6 };
	int *p = b;
	int i = 0, j = 0;
	int d1=10, d2=10;
	IntArrayPtr *m = new IntArrayPtr[d1];
	for (i = 0; i<d1; i++)
	{
		m[i] = new int[d2];
	}
	initialArray(m, d1, d2);
	int d[5];
	int *x = d;
	Knapsack(p, w, c, n, m);
	Traceback(m, w, c, n, x);
	for (int i = 0; i <= n; i++) {
		cout << x[i] << endl;
	}
	return 0;
}

void initialArray(int **a, int d1, int d2)
{
	for (int i = 0; i<d1; i++)
		for (int j = 0; j<d2; j++)
		{
			a[i][j]=0;
		}

}
