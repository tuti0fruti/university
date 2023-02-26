#include <iostream>
#include <cstdlib>
#include <ctime>	 
using namespace std;

/*
18. Известны места N лыжников на каждом из M стартов Кубка мира.
Определить победителя в общем зачете (с минимальной суммой мест).
Если таких несколько, то победителем считается тот, кто лучше других
претендентов на первое место выступил на последнем этапе.
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
		cout << "Места " << i + 1 << " лыжника";
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
		cout << "Сумма " << i + 1 << " лыжника = " << summa[i] << endl;
	
	int best_summa = summa[0], i_best_skier = 0;   // best_summa - лучший результат, i_best_skier - номер участника с лушим результатом
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
			
	cout << "\nПобедитель участник номер " << i_best_skier + 1 << " с результатом " << summa[i_best_skier] << endl;;


	//////////////////////////////////////////////////////
	cout << "\n\n";
	for (int i = 0; i < n; i++)
		delete[] skiers[i];
	delete[] skiers;

	return 0;
}