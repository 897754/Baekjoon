#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main()
{
	int n;
	cin >> n;

	string a;

	cin >> a;

	int result = 0;
	for (int i = 0; i < a.length(); i++)
	{
		result += ((int)a[i] - (int)'0');
	}

	cout << result;
}