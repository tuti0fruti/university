#include <iostream>
#include <cmath>
using namespace std;

double length(double a1, double  a2, double b1, double b2);

/*
6. ������ N ������������� ������������ �� ������. ����������,
������� � ���� ������ ������������ ������������� � ����������
������ ��������� ����� �.
*/

int main()
{
	setlocale(LC_ALL, "rus");
	double x1, x2, x3, y1, y2, y3, a, b, c, per; // kordinaty vershin
	int N,P, K=0;

	cout << "������� ����� �������������: ";
	cin >> N;
	cout << "������� ����� P: "; 
	cin >> P;

	for (int i = 0; i < N; i++)
	{
		cout << "���������� ������ ������� x1 y1: ������������ ����� " << i + 1 << ": ";
		cin >> x1 >> y1;
		cout << "���������� ������ ������� x2 y2: ������������ ����� " << i + 1 << ": ";
		cin >> x2 >> y2;
		cout << "���������� ������� ������� x3 y3: ������������ ����� " << i + 1 << ": ";
		cin >> x3 >> y3;

		a = length(x1, y1, x2, y2);
		b = length(x1, y2, x3, y3);
		c = length(x3, y3, x2, y2);
		per = a + b + c;

		if ((((a * a + b * b) > c * c) || ((a * a + c * c) > b * b) || ((c * c + b * b) > a * a)) && (per > P)) K = K + 1;
	}

	cout << "\n\t���������� ������������ ������������� � ���������� ������ ��������� ����� � = " << K << endl;
	
	return 0;
}

double length(double a1,double  a2, double b1,double b2)
{

	double coordinates = sqrt((a1 - a2) * (a1 - a2) + (b1 - b2) * (b1 - b2));

	return coordinates;
}