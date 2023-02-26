#include <iostream>
#include <cmath>
using namespace std;
/*
	18. ���� ������������ ����� ������������� ����� K (K<10^9).
������� ����� ����� ����� � ������� ���������� (��������, 546085
=>045568). ��������� � ������� ������ �� �������� �� ������������.
*/
int main()
{
	setlocale(LC_ALL, "rus");

	int k = 0, element[10] ={0};

	do
	{
		cout << "������� ����� K (���� K �� ������ ��������� 10^9 � ������ ���� ������ 0): ";
		cin >> k;
	} while (k < 0 || k > pow(10,9));
	cout << "\n\t��������� �����: " << k;

	int count = 0, tmp = 0;

	do
	{
		element[count++] = k % 10;
		k /= 10;
	} while (k);

	if (count == 1)
	{
		cout << "\n\t����� �����: ";
		for (int i = 0; i < count; i++)
			cout << element[i];
	}
	else
		for (int i = 0; i < count - 1; i++) 
			for (int j = 0; j < count - i - 1; j++) 
				if (element[j] > element[j + 1])
				{
					tmp = element[j];
					element[j] = element[j + 1];
					element[j + 1] = tmp;
				}
			
	cout << "\n\t����� �����: ";
	for (int i = 0; i < count; i++)
		cout << element[i];
	cout << endl;

	return 0;
}