
using namespace std;

/*
6. Дана последовательность, состоящая из дробей: 1/1, 4/2, 9/4, 16/8,...
Какое минимальное количество элементов последовательности нужно
сложить, чтобы сумма превысила заданное число S > 1?

Работает до 12, толи я дурак толи после 11.99999999 уже идет слишком маленькое суммирование
*/

int main()
{
	setlocale(LC_ALL, "rus");

	double s = 0;
	do
	{
		cout << "Введиет число S (число S > 1): ";
		cin >> s;
	} while (s <= 1);

	long double numerator = 1, denominator = 1, summma = 1;
	int counter = 1;

	do
	{
		counter++;
		numerator = counter*counter;
		denominator *= 2;
		summma += numerator / denominator;		
		//cout << numerator << " " << denominator << " " << numerator / denominator << endl << "\tСчетчик " << counter << " Сумма " << summma << endl;
	} while (summma < s);


	cout << "\nНужно " << counter  << " элементов что бы сумма " << summma << " превысила значение " << s << endl;

	return 0;
}