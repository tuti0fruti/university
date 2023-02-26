#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
/*
18. Даны два одномерных массива из действительных чисел. Первый
массив состоит из N элементов, а второй из M элементов. Сформировать
третий массив, записав в его начало элементы первого массива с четными
индексами, а в конец элементы второго массива с нечетными индексами.
Перестановка элементов не допускается.
*/

int main()
{
	setlocale(LC_ALL, "rus");
	srand(time(0));

	const int n = 4, m = 5, big = ceill((float)(n + m) / 2);		
	int array_1[n] = { 0 }, array_2[m] = { 0 }, *collector = new int [big], counter = 0;

	cout << "\tПервый массив\n\n";
	for (int i = 0; i < n; i++)
	{
		array_1[i] = rand();
		cout << "[" << i+1 << "] = " << array_1[i] << " ";
		if ((i+1)%2 == 0)
		{
			collector[counter] = array_1[i];
			counter++;
		}
	}
	cout << "\n\tВторой массив\n\n";
	for (int i = 0; i < m; i++)
	{
		array_2[i] = rand();
		cout << "[" << i+1 << "] = " << array_2[i] << " ";
		if ((i+1) % 2 == 1)
		{
			collector[counter] = array_2[i];
			counter++;
		}
	}

	cout << "\n\tСобранный массив\n\n";
	for (int i = 0; i < big; i++)
		cout << "[" << i+1 << "] = " << collector[i] << " ";
	cout << endl;


	delete [] collector;
	return 0;
}


