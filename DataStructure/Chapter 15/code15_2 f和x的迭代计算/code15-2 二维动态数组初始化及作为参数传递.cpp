// code15-2 二维动态数组初始化及作为参数传递.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<vector>
using namespace std;
typedef double *DoubleArrayPtr;//这里使用typedef后可以批量定义double类型的指针
void initialArray(double **a, int d1, int d2);

int main()
{
	int i = 0, j = 0;
	int d1, d2;
	cout << "Input d1 and d2" << endl;
	cin >> d1 >> d2;
	DoubleArrayPtr *m = new DoubleArrayPtr[d1]; //定义一个double指针数组
	for (i = 0; i<d1; i++)
	{
		m[i] = new double[d2];
	}//为指针数组每一项定义一个数组，形成二维数组
	initialArray(m, d1, d2);
	cout << "Output the input;" << endl;
	for (i = 0; i<d1; i++)
	{
		for (j = 0; j<d2; j++)
		{
			cout << m[i][j] << " ";
		}
		cout << endl;
	}
	for (i = 0; i<d1; i++)
		delete[] m[i];
	delete[] m;//释放内存
//这里应该将动态分配内存的指针清零，防止它处于悬空状态
	system("pause");
	return 0;
}

void initialArray(double **a, int d1, int d2)
{
	cout << "Enter the number" << endl;
	for (int i = 0; i<d1; i++)
		for (int j = 0; j<d2; j++)
		{
			cin >> a[i][j];
		}

}


