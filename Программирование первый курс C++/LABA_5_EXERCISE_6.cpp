#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
/*
6. Дан одномерный массив из N случайных действительных чисел в
диапазоне от 11 до 22. Вывести в порядке невозрастания (убывания)
элементы, находящиеся в диапазоне между A и B.
*/

int main()
{
	setlocale(LC_ALL, "rus");
	srand(time(0));

	const int n = 11;
	int a = 0, b = 0, array[n] = {0}, tmp = 0;

	do
	{
		cout << "Введите число A, в диапазоне от 0 до " << n-1 << ": ";
		cin >> a;
	} while (a < 0 || a >= n);
	do
	{
		cout << "Введите число B, в диапазоне от 0 до " << n-1 << ": ";
		cin >> b;
	} while (b < 0 || b >= n);

	cout << "\tНачальный массив:\n\n";
	for (int i = 0; i < n; i++)
	{
		array[i] = rand();
		cout << "[" << i << "]= " << array[i] << " ";
	}

	for (int i = 0; i <= n-1; i++)
		for (int j = 0; j <= n - i - 1; j++) 
			if (array[j] < array[j + 1]) {
				tmp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = tmp;
			}

	cout << "\n\n\tОтсортированный массив в порядке невозрастания (убывания), в диапазоне между " << b << " элементом и " << a << " элементом.\n\n";
	if (a < b)
	{
		for (int i = a; i <= b; i++)
			cout << "[" << i << "] = " << array[i] << " ";
		cout << endl;
	}
	else
	{
		for (int i = b; i <= a; i++)
			cout << "[" << i << "] = " << array[i] << " ";
		cout << endl;
	}



	return 0;
}