#include <iostream>
#include <cmath>
using namespace std;
/*
	18. Дано произвольное целое положительное число K (K<10^9).
Вывести цифры этого числа в порядке неубывания (например, 546085
=>045568). Процедуры и функции работы со строками не использовать.
*/
int main()
{
	setlocale(LC_ALL, "rus");

	int k = 0, element[10] ={0};

	do
	{
		cout << "Введите число K (чило K не должно превышать 10^9 и должно быть больше 0): ";
		cin >> k;
	} while (k < 0 || k > pow(10,9));
	cout << "\n\tНачальное число: " << k;

	int count = 0, tmp = 0;

	do
	{
		element[count++] = k % 10;
		k /= 10;
	} while (k);

	if (count == 1)
	{
		cout << "\n\tНовое число: ";
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
			
	cout << "\n\tНовое число: ";
	for (int i = 0; i < count; i++)
		cout << element[i];
	cout << endl;

	return 0;
}