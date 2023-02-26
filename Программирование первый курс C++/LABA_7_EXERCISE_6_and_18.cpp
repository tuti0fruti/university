#include <iostream>
#include <iomanip>
using namespace std;
const int symbol = 15, count_age = 3, count_mark = 3;
int count_students = 3;
void print_students();
void vvod_keybords();
/*
Задания по теме «Структуры»:
Составить список учебной группы, включающий N (N=3) человек.
Для каждого студента указать: фамилию и имя, дату рождения (год,
месяц и число) оценки за сессию (от 3 до 5 экзаменов). Информацию о
каждом студенте оформить в виде структуры, а совокупность структур
объединить в массив. Составить программу, которая обеспечивает ввод
полученной информации, ее просмотр в виде таблицы (рис. 1), а также
вывод информации на экран монитора согласно конкретному варианту. 
В случае если в группе нет студентов с требуемыми данными, выдать
соответствующее сообщение.

6. Вывести анкетные данные студентов, получивших по одному из
предметов оценку «хорошо», а по всем другим – «отлично».

18. Вывести список студентов, упорядоченный по месяцу рождения.

setfill(%) - установить символ % как заполнитель
setw(n)	- определяет ширину поля вывода в n символов
left	Выравнивание по левой границе (по умолчанию)
right	Выравнивание по правой границе (по умолчанию)
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
	
	//vvod_keybords(); //ввод с клавиатуры
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
				cout << "\nСтуденты, получившие по одному из предметов оценку «хорошо», а по всем другим – «отлично»" << endl << setw(10) << right <<"Surname" << setw(8) << right << "Name" << setw(16) << right << "Berthday" << setw(30) << right << "Mark <fis, math, inf>\n";;
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
		cout << "\n\tНет студентов, получивших по одному из предметов оценку «хорошо», а по всем другим – «отлично»\n";
	/*exercise 18*/
	cout << "\nСписок студентов отсортированных по месяцу рождения.\n";
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