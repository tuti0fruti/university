
using namespace std;

/*
6. ���� ������������������, ��������� �� ������: 1/1, 4/2, 9/4, 16/8,...
����� ����������� ���������� ��������� ������������������ �����
�������, ����� ����� ��������� �������� ����� S > 1?

�������� �� 12, ���� � ����� ���� ����� 11.99999999 ��� ���� ������� ��������� ������������
*/

int main()
{
	setlocale(LC_ALL, "rus");

	double s = 0;
	do
	{
		cout << "������� ����� S (����� S > 1): ";
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
		//cout << numerator << " " << denominator << " " << numerator / denominator << endl << "\t������� " << counter << " ����� " << summma << endl;
	} while (summma < s);


	cout << "\n����� " << counter  << " ��������� ��� �� ����� " << summma << " ��������� �������� " << s << endl;

	return 0;
}