#include <iostream>
#include <cstdlib>
#include <ctime>	 
using namespace std;

/*
18. �������� ����� N �������� �� ������ �� M ������� ����� ����.
���������� ���������� � ����� ������ (� ����������� ������ ����).
���� ����� ���������, �� ����������� ��������� ���, ��� ����� ������
������������ �� ������ ����� �������� �� ��������� �����.
*/


int main()
{
	setlocale(LC_ALL, "rus");
	srand(time(NULL));

	int n = 5, m = 3;	

	int* *skiers = new int*[n], *summa = new int[n], tmp = 0;

	for (int i = 0; i < n; i++)
		skiers[i] = new int[m];

	for (int i = 0; i < n; i++)
	{
		cout << "����� " << i + 1 << " �������";
		for (int j = 0; j < m; j++)
		{
			skiers[i][j] = rand() % n + 1;
			cout << " " << skiers[i][j];
			tmp += skiers[i][j];
		}
		summa[i] = tmp;
		cout << "\n";
		tmp = 0;
	}
	//////////////////////////////////////////////////////
	cout << "\n";
	for (int i = 0; i < n; i++)
		cout << "����� " << i + 1 << " ������� = " << summa[i] << endl;
	
	int best_summa = summa[0], i_best_skier = 0;   // best_summa - ������ ���������, i_best_skier - ����� ��������� � ����� �����������
	for (int i = 1; i < n; i++)
		if (best_summa > summa[i])
		{
			i_best_skier = i;
			best_summa = summa[i];
		}
		else if (best_summa == summa[i] && skiers[i_best_skier][m - 1] > skiers[i][m - 1])
			{
				i_best_skier = i;
				best_summa = summa[i];
			}
			
	cout << "\n���������� �������� ����� " << i_best_skier + 1 << " � ����������� " << summa[i_best_skier] << endl;;


	//////////////////////////////////////////////////////
	cout << "\n\n";
	for (int i = 0; i < n; i++)
		delete[] skiers[i];
	delete[] skiers;

	return 0;
}