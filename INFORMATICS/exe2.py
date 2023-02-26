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

def list_of_symbols(x):
    temp = str(x)
    i = 0
    count = "01"
    while i < len(temp)-1:
        if temp[i] == '.':
            count = "0."
            while i + 1 < len(temp)-1:
                count += '0'
                i += 1
            count += '1'        
        else:
            count = '01'
        i += 1           
    return count        

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

def input_name_error(x):
    print(f"\n\tвы ввели: {x}")
    
    tmp = checking_for_a_number(x)
      
    if (tmp == False):
        print("\tошибка - НЕ ЯВЛЯЕТСЯ ЧИСЛОМ\n") 
    elif(is_int(x) == False):
        print("\tошибка - ЧИСЛО НЕ ЦЕЛОЕ\n")
    else: 
        print("\tС этим числом все в порядке обратите внимание на друге число\n")
                 
def exercise_1 ():
    print("\n\t1.Дано положительное целое число N. Найти сумму всех четных чисел (вывести их) от 0 до N с помощью цикла while.\n")
    while True:
        N = input("Введите положительное целое число N: ")
        if (is_int(N) == True) and (checking_for_a_number(N) == True):
            N = int(N)
            if (N > 0):
                break
            else:
                print(f"\n\tвы ввели: {N}\n",
                      "\tошибка - ЧИСЛО МЕНЬШЕ НУЛЯ\n")
        else:
            input_name_error(N)
    print()
    print("\t", end="")     
    
    i = 0
    summa = 0 
    while (i!=N+1):
        i+=1
        if (i % 2 == 0):
            print(i, end=" ")
            summa += i
    
    print(f"\n\nСумма всех четных чисел (от 0 до N) равна: {summa}")    
     
def exercise_2 ():
    print("\n\n\t2.Даны два положительных целых числа K и N (K < N). Найти сумму всех нечетных чисел (вывести их) от K до N с помощью цикла while.\n")
    while True:
        K = input("Введите положительное число K: ")
        N = input(f"Введите положительное число N (большее числа K = {K}): ")
        
        k_safe = K
        
        if (is_int(K) == True) and (is_int(N) == True) and (checking_for_a_number(K) == True) and (checking_for_a_number(N) == True):
            K = float(K)
            N = float(N)
            if  (K > 0) and (N > 0) and (N > K):    
                break
            else:
                print(f"\n\t\tОшибка - ОБРАТИТЕ ВНИМАНИЕ НА УСЛОВИЕ (Числа K = {K} и N = {N} должны быть положительными и число N = {N} > числа K = {K})\n")
        else:
            input_name_error(K)
            input_name_error(N)        
    print()
    print("\t", end="")
    
    summa = 0   
    while (K <= N):
        if (K % 2 == 1):    
            print("%.0f" % K, end=" ")
            summa += K
        K += 1       
     
    print(f"\n\nСумма всех нечетных чисел (от K = {k_safe} до N = {N}) равна:", "%.0f" % summa)    
        
def exercise_3 ():
    print("\n\n3.Дано положительное целое число N. Найти факториал числа N. Факториалом числа называется произведение всех чисел от 1 до N.\n")
    while True:
        N = input("Введите положительное целое число N: ")
        if (is_int(N) == True) and (checking_for_a_number(N) == True):
            N = float(N)
            if (N > 0):
                break
            else:
                print(f"\n\tвы ввели: {N}\n",
                      "\tошибка - ЧИСЛО МЕНЬШЕ НУЛЯ\n")
        else:
            input_name_error(N)
    print()
    
    factorial = 1.
    i = 0.
    while i < N:
        i += 1
        factorial *= i
        print(f"Факториал числа", "%.0f" % i,"\t равен:" "%.0f" % factorial) 
               
def exercise_4 ():
    print(
        "\n\n4.Дано целое число N (> 0). Если оно является степенью числа 3, то вывести YES, если не является - вывести NO.\n"
    )
    while True:
        N = input("Введите положительное целое число N: ")
        if (is_int(N) == True) and (checking_for_a_number(N) == True):
            N = float(N)
            if (N > 0):
                break
            else:
                print(f"\n\tвы ввели: {N}\n",
                      "\tошибка - ЧИСЛО МЕНЬШЕ НУЛЯ\n")
        else:
            input_name_error(N)
    print()
    
    degree = 3
    i = 1.0
    while degree ** i <= N:
        print("%.0f" % degree ** i, end="\t") 
        if (N == degree ** i):
            print("\n\n\t\tYES")
            break
        i += 1       
    else:
        print("\n\n\t\tNO")

def exercise_5 ():
    print(
        "\n\n5.Дано целое число N (> 0). Найти двойной факториал N: N!! = N * (N-2) * (N-4).... \n"
    )
    while True:
        N = input("Введите положительное целое число N: ")
        if (is_int(N) == True) and (checking_for_a_number(N) == True):
            N = float(N)
            if (N > 0):
                break
            else:
                print(f"\n\tвы ввели: {N}\n",
                      "\tошибка - ЧИСЛО МЕНЬШЕ НУЛЯ\n")
        else:
            input_name_error(N)
    print()
    
    tmp = N
    factorial = 1.0
    
    while N > 0:
        factorial *= N
        N -= 2
        
    print("Двойной факториал числа", "%.0f" % tmp, "\t равен:", "%.0f" % factorial)

def EXERCISE_MAIN_(x):
    match x:
        case '1':
            exercise_1()
            return input('\n\ndo you want to continue?(y/n): ')
        case '2':
            exercise_2()
            return input('\n\ndo you want to continue?(y/n): ')  
        case '3':
            exercise_3()
            return input('\n\ndo you want to continue?(y/n): ')
        case '4':
            exercise_4()
            return input('\n\ndo you want to continue?(y/n): ')    
        case '5':
            exercise_5()
            return input('\n\ndo you want to continue?(y/n): ')
        case 'q':
            return 'n'
        case 'й':
            return 'n'
        case _:
            print('\nexercise don`t find, try again')
            return 0
        
def main ():
    while (True):
        while True:
            exercise = input("\n\t\tВведите № задания от 1 до 5 (<q> для выхода): ")
            remember = exercise
            x = EXERCISE_MAIN_(exercise) 
            if x != 0:
                break
        os.system('CLS')     
        while (x == 'r') or (x == 'R') or (x == 'к') or (x == 'К'):
            os.system('CLS')
            x = EXERCISE_MAIN_(remember)   
        if (x == 'n') or (x == 'N') or (x == 'т') or (x == 'Т'):
            break    
                   
main()     





 



