//Дан массив, содержащий 2014 вещественных чисел.
//Напишите на одном из языков программирования программу,
//находящую в этом массиве два соседних элемента, значения которых наименее близки,
//то есть абсолютная величина их разности максимальна.
//Если таких пар несколько, можно взять любую из них.
//Программа должна вывести найденные элементы.


#include <iostream>
#include <ctime>

int main()
{
    const int N = 10;
    srand(time(NULL));
    setlocale(LC_ALL, "rus");

    double numbers[N] = {};
    
    std::cout << "Исзодный массив:" << std::endl;
    for (int i = 0; i < N; i++)
    {
        numbers[i] = rand()*0.2;
        std :: cout << numbers[i] << std :: endl;
    }

    double max_diference = numbers[1] - numbers[0];
    double max_number_1 = 0, max_number_2 = 0;

    for (int i = 1; i < N-1; i++)
    {
        if (max_diference < numbers[i+1] - numbers[i])
        {
            max_number_1 = numbers[i];
            max_number_2 = numbers[i+1];
            max_diference = numbers[i + 1] - numbers[i];
        }
    }


    std::cout << "\nМаксимальная величина разности равна: " << max_diference << std::endl;
    std::cout << "Элемент 1 равен: " << max_number_1 << "\nЭлемент 2 равен: " << max_number_2 << std::endl;

    return 0;
}

