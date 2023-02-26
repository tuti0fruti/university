#include <iostream>
#include <iomanip>
using namespace std;
const int symbol = 15, count_age = 3, count_mark = 3;
int count_students = 3;
void print_students();
void vvod_keybords();
/*
������� �� ���� �����������:
��������� ������ ������� ������, ���������� N (N=3) �������.
��� ������� �������� �������: ������� � ���, ���� �������� (���,
����� � �����) ������ �� ������ (�� 3 �� 5 ���������). ���������� �
������ �������� �������� � ���� ���������, � ������������ ��������
���������� � ������. ��������� ���������, ������� ������������ ����
���������� ����������, �� �������� � ���� ������� (���. 1), � �����
����� ���������� �� ����� �������� �������� ����������� ��������. 
� ������ ���� � ������ ��� ��������� � ���������� �������, ������
��������������� ���������.

6. ������� �������� ������ ���������, ���������� �� ������ ��
��������� ������ �������, � �� ���� ������ � ��������.

18. ������� ������ ���������, ������������� �� ������ ��������.

setfill(%) - ���������� ������ % ��� �����������
setw(n)	- ���������� ������ ���� ������ � n ��������
left	������������ �� ����� ������� (�� ���������)
right	������������ �� ������ ������� (�� ���������)
*/
struct People
{
	char firstname[symbol];
	char secondname[symbol];
	short age[count_age];
	short mark[count_mark];

}*students = new People[count_students], tmp;
int main()
{
	setlocale(LC_ALL, "rus");
	students[0] = { "Ivanov", "Ivan", {1, 7, 1990}, {3, 4, 5} };
	students[1] = { "Petrov", "Petr", {23, 7, 1989}, {4, 5, 4} };
	students[2] = { "Sidorov", "Maksim", {5, 5, 1988}, {5, 5, 4}};
	
	//vvod_keybords(); //���� � ����������
	print_students();
	/*exercise 6*/
	bool flag = true, flag_no_peple = true;
	for (int i = 0; i < count_students; i++)
	{
		for (int j = 0; j < count_mark; j++)
			if (students[i].mark[j] == 4 && flag)
				flag = false;
			else if (students[i].mark[j] != 5)
			{
				flag = true;
				break;
			}
		if (flag == false)
		{
			if (flag_no_peple)
				cout << "\n��������, ���������� �� ������ �� ��������� ������ �������, � �� ���� ������ � ��������" << endl << setw(10) << right <<"Surname" << setw(8) << right << "Name" << setw(16) << right << "Berthday" << setw(30) << right << "Mark <fis, math, inf>\n";;
			cout << setw(10) << right << students[i].firstname << setw(8) << right << students[i].secondname << "\t";
			for (int j = 0; j < count_age - 1; j++)
				cout << setw(2) << setfill('0') << students[i].age[j] << "/" << setfill(' ');
			cout << right << students[i].age[count_age - 1];
			cout << setw(25);
			for (int k = 0; k < count_mark; k++)
				cout << students[i].mark[k] << " ";
			cout << endl;
			flag = true;
			flag_no_peple = false;
		}
	}
	
	if (flag_no_peple)
		cout << "\n\t��� ���������, ���������� �� ������ �� ��������� ������ �������, � �� ���� ������ � ��������\n";
	/*exercise 18*/
	cout << "\n������ ��������� ��������������� �� ������ ��������.\n";
	for(int i = 0; i < count_students - 1; i++)
		for (int j = 0; j < count_students - i - 1; j++)
			if (students[j].age[1] > students[j+1].age[1])
			{
				tmp = students[j];
				students[j] = students[j+1];
				students[j+1] = tmp;
			}
	print_students();
	
	
	return 0;
}
void print_students()
{
	cout << setw(10) << right <<"Surname" << setw(8) << right << "Name" << setw(16) << right << "Berthday" << setw(30) << right << "Mark <fis, math, inf>\n";
	for (int i = 0; i < count_students; i++)
	{
		cout << setw(10) << right << students[i].firstname << setw(8) << right << students[i].secondname <<"\t";
		for (int j = 0; j < count_age - 1; j++)
			cout<< setw(2) << setfill('0') << students[i].age[j] << "/" << setfill(' ');
		cout << right << students[i].age[count_age - 1];
		cout << setw(25);
		for (int k = 0; k < count_mark; k++)
			cout << students[i].mark[k] << " ";
		cout << endl;
	}
}

void vvod_keybords()
{
	do
	{
		cout << "Enter count students:(>3) ";
		cin >> count_students;
	} while (count_students < 3);

	for (int i = 0; i < count_students; i++)
	{
		cout << "Enter information about " << i + 1 << " - student\n";
		cout << "Surname: " ;
		cin >> students[i].firstname;
		cout << "Name: ";
		cin >> students[i].secondname;
		cout << "Birthday <Day, Month, Year> ";
		for (int j = 0; j < count_age; j++)
		{
			cin >> students[i].age[j];
		}
		cout << "Ball <Fisica, Mathematika, Informathika> ";
		for (int k = 0; k < count_mark; k++)
		{
			cin >> students[i].mark[k];
		}
	}


}