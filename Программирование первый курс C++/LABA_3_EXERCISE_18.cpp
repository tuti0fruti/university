#include <iostream>

using namespace std;

/*
18. ������ N ����������������� �� ��������� A, B, C, D. ����������,
������� ����� ��� ���������������� � ������.
*/

int main()
{
	setlocale(LC_ALL, "rus");

	int N, k1 = 0, k2 = 0;
	double a, b, c, d;


	cout << "������� ���������� �����������������: ";
	cin >> N;
	
	for (int i = 1; i <= N; i++)
	{
		cout << "������� ������� " << i << "-�� ���������������� a, b, c, d - ";
		cin >> a >> b >> c >> d;
		if ((a == c) && (b == d) && (a == b)) k1++;
		else
			if ((a == c) && (b == d)) k2++;
		
	}
	
	cout << "\n\t������ - " << k1 << "\n\t���������������� - " << k2 << endl;

	return 0;
}