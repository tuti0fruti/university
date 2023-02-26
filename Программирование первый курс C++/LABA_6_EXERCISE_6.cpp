#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

double final_result(int *, int);

/*	
6. Выступления N спортсменов оцениваются M судьями по одной и
той же числовой шкале. Нужно узнать конечный результат каждого
спортсмена, если он вычисляется так: из всех M оценок удаляются
максимальная и минимальная (если таких оценок несколько, то удаляется
только одна), затем из оставшихся (M-2) находится их среднее
арифметическое. Вычисление конечного результата спортсмена
оформить в подпрограмме.
*/

void delete_element(int*& array, int size, int max, int min)
{
	int* new_array = new int[size], count = 0;
	for (int i = 0; i < size; i++)
		if (i != max && i != min)
			new_array[count++] = array[i];

	delete[] array;

	array = new_array;
}

int main()
{
	setlocale(LC_ALL, "rus");
	srand(time(NULL));
	
	int n = 2, m = 6;	// n - количество спортсменнов, m - количество судей которые ставят оценки
					    // можно мказать что m это количество оценок
	int** sport = new int* [n]; 

	for (int i = 0; i < n; i++) 
		sport[i] = new int[m];
	/////////////////////////////////
	for (int i = 0; i < n; i++)
	{
		cout << i+1 <<" cпортсмен: ";
		for (int j = 0; j < m; j++)
		{
			sport[i][j] = rand() % 30;
			cout << "|\t" << sport[i][j] << "\t |";
		}
		cout << "\n";
	}

	int minimum = 0, maximum = 0;

	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < m; j++)
		{
			if (sport[i][minimum] > sport[i][j])
				minimum = j;
			if (sport[i][maximum] < sport[i][j])
				maximum = j;
		}
		delete_element(sport[i],m,maximum,minimum);
		//cout << "\ntmax = " << maximum + 1<< " min = " << minimum + 1 << endl;
	}
	
	m -= 2;
	cout << "\n\tНовый массив, без максимального и минимального результатов\n";
	for (int i = 0; i < n; i++)
	{
		cout << i + 1 << " cпортсмен: ";
		for (int j = 0; j < m; j++)
			cout << "|\t" << sport[i][j] << "\t |";
		cout << "\n";
	}
	///////////////////////////////
	for (int i = 0; i < n; i++)
	{
		cout << "\nКонечный результат спортсмена " << i + 1 << ", равен = " << final_result(sport[i], m) << endl;
		delete[] sport[i];
	}
	delete[]sport;
	return 0;
}

double final_result(int *arrray, int size)
{
	double suma = 0;

	for (int i = 0; i < size; i++)
		suma += arrray[i];

	return suma/size;
}




