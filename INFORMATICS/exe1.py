import random
import getpass
import stdiomask
import os

def is_int(x):
    temp = str(x)
    i = 0 
    while i < len(temp):
        if temp[i] == '.':           
            while i + 1 < len(temp): 
                if temp[i + 1] != '0':
                    return False
                i += 1 
            else:
                return True
        i += 1
    else:
        return True 

def checking_for_a_number(x):
    number = ['1','2','3','4','5','6','7','8','9','0','.','-']
    x = str(x)
    i = 0
    if (len(x) == 0):
        return False
    else:
        while (i < len(x)):
            if (x[i] not in number):
               return False
            i += 1
        else:
            return True 

def main_screen():
        print(
        "\t\t-----------------------------------"
        "\n\t\tЗдравствуйте!",
        "\n\t\tВам предоставлены две игры:",
        "\n\t\tУгадайка и Проверка строки",
        "\n\t\t-----------------------------------"
        )
        input("\n\t\t\tНажмите Enter что бы продолжить")
        os.system('CLS')

def exe_1():
    print("\n\t\tВведите в каких пределах вы хотите играть\n")
    while True:
        limit_down = input("\tВведите нижний предел: ")
        if checking_for_a_number(limit_down):
            limit_down = int(limit_down)
            break
        else:
            print("\n\t\tERROR - это не число, попробуйте еще раз\n")
    while True:
        limit_up = input("\tВведите верхний предел: ")
        if checking_for_a_number(limit_up):
            limit_up = int(limit_up)
            if limit_up > limit_down:
                break
            else:
                print(f"\n\t\tВведите пожалуйста число, больше нижнего предела\n")
                print(f"\tНижний предел равен {limit_down}")
        else:
            print("\n\t\tERROR - это не число, попробуйте еще раз\n")
            print(f"\tНижний предел равен {limit_down}")    

    os.system('CLS')

    ran = random.randint(limit_down,limit_up)
    
    print (
        f"\n\t я загадал число в пределах от {limit_down} до {limit_up} попробуй отгадай ))))))))))\n", ran)
    
    while True:
        your_number = input("\tВаш вариант: ")
        if checking_for_a_number(your_number):
            your_number = int(your_number)
            break
        else:
            print("\n\t\tОшибка ввода, это не число попробуйте еще раз\n")    
    
    count = 1
    
    while True:
        if (ran == your_number):
            print(
                "\n\t\t-------WIN-------\n",
                )
            if (count % 10 == 1) and (count != 11) and (count != 12):
                print(f"\tдля победы вам потребовалось {count} попытка\n")
            elif (count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4) and (count < 10) and (count > 14):
                print(f"\tдля победы вам потребовалось {count} попытки\n") 
            else:
                print(f"\tдля победы вам потребовалось {count} попыток\n") 
                
            break
        elif (ran < your_number): 
            print("\tНе угадал ГЛУПЫЙ ЧЕДОВЕК")
            count += 1
            while True:
                your_number = input("\tПопробуй поменьше: ")
                if checking_for_a_number(your_number):
                    your_number = int(your_number)
                    break
                else:
                    print("\n\t\tОшибка ввода, это не число попробуйте еще раз\n")
        elif (ran > your_number):
            print("\tНе угадал ГЛУПЫЙ ЧЕДОВЕК")
            count += 1
            while True:
                your_number = input("\tПопробуй побольше: ")
                if checking_for_a_number(your_number):
                    your_number = int(your_number)
                    break
                else:
                    print("\n\t\tОшибка ввода, это не число попробуйте еще раз\n")
    
    input("\n\t\t\tНажмите Enter что бы продолжить")
    os.system('CLS')
            
def exe_2():           
      
    while True:
        my_number = stdiomask.getpass(prompt="\tЗагадайте число: ", mask='X')
        if checking_for_a_number(my_number):
            break
        else:
            print("\n\t\tERROR - это не число, попробуйте еще раз\n")
            
    while True:
        your_number = input("\tПопробуйте отгадать загаданное число: ")
        if checking_for_a_number(your_number):
            break
        else:
            print("\n\t\tERROR - это не число, попробуйте еще раз\n")
      
    count = 1
      
    while True:
        if (my_number == your_number):  
            print(
            "\n\t\t-------WIN-------\n",
            )
            if (count % 10 == 1) and (count != 11) and (count != 12):
                print(f"\tдля победы вам потребовалось {count} попытка\n")
            elif (count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4) and (count < 10) and (count > 14):
                print(f"\tдля победы вам потребовалось {count} попытки\n") 
            else:
                print(f"\tдля победы вам потребовалось {count} попыток\n") 
                
            break
        elif (my_number < your_number):
            count += 1
            while True:
                your_number = input('Введите меньше: ')
                if checking_for_a_number(your_number):
                    break
                else:
                    print("\n\t\tERROR - это не число, попробуйте еще раз\n")
        elif (my_number > your_number):
            count += 1
            while True:
                your_number = input('Введите больше: ')
                if checking_for_a_number(your_number):
                    break
                else:
                    print("\n\t\tERROR - это не число, попробуйте еще раз\n")
    
    input("\n\t\t\tНажмите Enter что бы продолжить")
    os.system('CLS')

def _game_1():
    while True:
        print(
        "\t1. Программа по угадыванию числа.\n\n",
        "\tСуществует 2 варианта игры:\n\n",
        "\t\t1 - Компьютер загадывает, пользователь отгадывает.\n",
        "\t\t2 - Пользователь загадывает, другой пользователь отгадывает.\n",
        "\n\tq - для выхода на экран выбора игр\n"
        )
    
        x = input("Введите вариант игры: ")
        os.system('CLS')
        match x:
            case '1':
                exe_1()
                break
            case '2':
                exe_2()
                break
            case 'q':
                return
            case _:
                print('Такого варианта не существует попробуйте снова\n')    

def proverka(N):
    
    count = 1
    
    for i in range(len(N)-1):
        if (N[i] < N[i+1]):
            print("последовательность цифр числа при просмотре справа налево не упорядоченна по неубыванию.")
            return
        elif (N[i] == N[i+1]):
            count += 1  
   
    if count == len(N):
        print("цифры числа равны")
    else:
        print("последовательность цифр числа при просмотре справа налево упорядоченна по неубыванию")  

def stroka():
    print(
    "\n\t\t2. Введите натуральное число.",
    "\n\t\tИ программа определит, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию."
    )  
    
    while True:
        N = input("Введите натуральное число N содержащее как минимум два символа: ")
        if checking_for_a_number(N):
            if is_int(N):
                if float(N) > 9:
                    int_N = ''
                    for i in range(len(N)):
                        if N[i] == '.':
                            break
                        int_N += N[i]
                    break
                else:
                    print("\n\t\tERROR - введено менее двух символов попробуйте снова\n")
            else:
                print("\n\t\tERROR - число не натуральное попробуйте снова\n")
        else:
            print("\n\t\tERROR - не является числом попробуйте снова\n")
        
        
    print("Изначальное число:", int_N)        
    proverka(int_N)
    
    input("\n\t\t\tНажмите Enter что бы продолжить")
    os.system('CLS')
      
main_screen()
while True:
    print(
        "\n\t1 - Угадайка",
        "\n\t2 - Проверка строки",
        "\n\tmain - начальный экран ",
        "\n\tq - выход"
    )
    x = input("\nВведите во что вы хотите сыграть: ")
    os.system('CLS')
    match x:
        case '1': 
            _game_1()
        case '2':
             stroka()
        case 'main':
            main_screen()
        case 'q':
            break    
        case _:
            print('Error try again')

