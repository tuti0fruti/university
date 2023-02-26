#include <iostream>

using namespace std;

/*
18. Задано N четырехугольников со сторонами A, B, C, D. Определить,
сколько среди них параллелограммов и ромбов.
*/

int main()
{
	setlocale(LC_ALL, "rus");

	int N, k1 = 0, k2 = 0;
	double a, b, c, d;


	cout << "Введите количество четырехугольников: ";
	cin >> N;
	
	for (int i = 1; i <= N; i++)
	{
		cout << "Введите стороны " << i << "-го четырехугольника a, b, c, d - ";
		cin >> a >> b >> c >> d;
		if ((a == c) && (b == d) && (a == b)) k1++;
		else
			if ((a == c) && (b == d)) k2++;
		
	}
	
	cout << "\n\tРомбов - " << k1 << "\n\tПараллелограммов - " << k2 << endl;

	return 0;
}