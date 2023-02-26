#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

double final_result(int *, int);

/*	
6. ����������� N ����������� ����������� M ������� �� ����� �
��� �� �������� �����. ����� ������ �������� ��������� �������
����������, ���� �� ����������� ���: �� ���� M ������ ���������
������������ � ����������� (���� ����� ������ ���������, �� ���������
������ ����), ����� �� ���������� (M-2) ��������� �� �������
��������������. ���������� ��������� ���������� ����������
�������� � ������������.
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
	
	int n = 2, m = 6;	// n - ���������� ������������, m - ���������� ����� ������� ������ ������
					    // ����� ������� ��� m ��� ���������� ������
	int** sport = new int* [n]; 

	for (int i = 0; i < n; i++) 
		sport[i] = new int[m];
	/////////////////////////////////
	for (int i = 0; i < n; i++)
	{
		cout << i+1 <<" c��������: ";
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
	cout << "\n\t����� ������, ��� ������������� � ������������ �����������\n";
	for (int i = 0; i < n; i++)
	{
		cout << i + 1 << " c��������: ";
		for (int j = 0; j < m; j++)
			cout << "|\t" << sport[i][j] << "\t |";
		cout << "\n";
	}
	///////////////////////////////
	for (int i = 0; i < n; i++)
	{
		cout << "\n�������� ��������� ���������� " << i + 1 << ", ����� = " << final_result(sport[i], m) << endl;
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




