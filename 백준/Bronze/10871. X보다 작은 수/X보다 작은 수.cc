#include <stdio.h>
#include <iostream>
using namespace std;



int main()
{
	int a, b, c;

	cin >> a >> b;

	int* arr = new int[a];
	for(int i = 0; i < a; i++)
	{
		cin >> c;
		arr[i] = c;
	}

	for (int i = 0; i < a; i++)
	{
		if (arr[i] < b)
		{
			cout << arr[i] << " ";
		}
	}
	cout << endl;
}