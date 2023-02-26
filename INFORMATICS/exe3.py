import os
import time
from decimal import *
from random import randint
from math import *

def list_of_symbols_after_dot(x):
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

def exercise_21():
    x = "Вычисление суммы всех чисел Фибоначи которые не превосходят заданное число"
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )
    
    while True:
        finally_number = input("\n\tВведите число до которого нужно найти сумму: ")
        
        if checking_for_a_number(finally_number):
            finally_number = float(finally_number)
            if finally_number > 0:
                break
            else:
                print("Ошибка вы ввели число меньше нуля, попробуйте снова")
        else:
            print("Ошибка вы ввели не число, попробуйте снова")
    print()

    fib_number_sum = 1
    fib_number = 0
    
    first = 0
    second = 1
    count = 1
    
    while fib_number <= finally_number:
        if (count == 2):
           print(f"число номер {count} равно {fib_number}")
           count += 1
           continue
        
        print(f"число номер {count} равно {fib_number}")
        count += 1 
        
        fib_number = first + second
        fib_number_sum += fib_number
        first = second
        second = fib_number 
            
    print("\n\tСумма равна",fib_number_sum)    
    
def exercise_22():
    x = "Распечатывает значения функции, пока не будет достигнуто пересечение графиков:"
    x1 = "Функция 1 - 2x^3 - x^2 + 2"
    x2 = "Функция 2 - e^(x/3) + e^(x/3)" 
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x1,"\n\t\t",x2,"\n\t\t","-"*len(x), sep="", end="\n\n" )
    
    step = 0.01
    start_coordinate = -1.0 
    count = 1
    
    
    while 2*(start_coordinate**3) - 2*(start_coordinate**2) + 2 != exp(start_coordinate/3) + exp(start_coordinate/3):
        start_coordinate =round(start_coordinate + step, 2)
        print(
            f"\tЧисло {count}:\n\t{x1}:\t", "%.2f" % (2*(start_coordinate**3) - 2*(start_coordinate**2) + 2),
            f"\n\t{x2}:\t", "%.2f" % (exp(start_coordinate/3) + exp(start_coordinate/3)),
            f"\n\tКоордината равна {start_coordinate}",
            sep="", end="\n\n" 
            )
        count += 1
       
def exercise_23():
    x = [
        "Дана последовательность целых чисел",
        "Вычислить сумму элементов последовательности, предшествующих \"особому\" элементу"]
    print("\n\t\t","-"*len(x[1]),"\n\t\t",x[0],"\n\t\t",x[1],"\n\t\t","-"*len(x[1]), sep="" )
    
    while True:
        amount_of_numbers = input("\nВведите количество элементов последовательности больше 100: ")
        if checking_for_a_number(amount_of_numbers):
            if is_int(amount_of_numbers):
                amount_of_numbers = float(amount_of_numbers)
                if amount_of_numbers > 100:
                    break
                else:
                    print("\n\t\tОшибка число меньше 100, попробуйте снова")
            else:
                print("\n\t\tОшибка число не целое, попробуйте снова")
        else:
            print("\n\t\tОшибка - введенный символ не является числом, попробуйте снова")            
               
    count = 1                  
    equal = 0
    number_one = randint(-30,70)      
    number_two = randint(-30,70)
                
    while count <= amount_of_numbers:
        print(
            f"\n\t\tnumber {count} = {number_one}",sep="", end="")
        if number_one > number_two and amount_of_numbers > count > 1:
            print("\tследующий меньше ->", f"предыдущий равен {tmp}",end="")
            equal += tmp
        tmp = number_one
        number_one = number_two 
        number_two = randint(-30,70)
        
        count += 1
        
    print (f"\n\t\tСумма элементов последовательности, предшествующих \"особому\" элементу равна {equal}")   
          
def exercise_24():
    x = "Даны положительные действительные числа A, X и E для которых должно выполнятся неравенство:"
    x1 = "y(0) = A"
    x2 = "y(i) = ( y(i-1) + x/y(i-1) )/2"
    x3 = "|y(n)^2 - y(n-1)^2| < E"    
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x1,"\n\t\t",x2,"\n\t\t",x3,"\n\t\t","-"*len(x), sep="" )
      
    while True:
        A_number = input("\n\tВведите число A: ")
        
        if checking_for_a_number(A_number):
            A_number = float(A_number)
            if A_number > 0:
                break
            else:
                print("Ошибка вы ввели число меньше нуля, попробуйте снова")
        else:
            print("Ошибка вы ввели не число, попробуйте снова")  
      
    while True:
        X_number = input("\tВведите число X: ")
        
        if checking_for_a_number(X_number):
            X_number = float(X_number)
            if X_number > 0:
                break
            else:
                print("Ошибка вы ввели число меньше нуля, попробуйте снова")
        else:
            print("Ошибка вы ввели не число, попробуйте снова")

    while True:
        E_number = input("\tВведите число E: ")
        
        if checking_for_a_number(E_number):
            E_number = float(E_number)
            if E_number > 0:
                break
            else:
                print("Ошибка вы ввели число меньше нуля, попробуйте снова")
        else:
            print("Ошибка вы ввели не число, попробуйте снова")
            
    y0 = A_number
    i = 1
        
    while True:
        y1 = (y0 + X_number/y0)/2
        print(
            f"\n\t\tЭлемент {i} = " "%.2f" % y0,sep="", end="")
        input()
        if abs(y1**2 - y0**2) < E_number:
            print("\n\tПервый элемент который удовлетворяет условию =", "%.2f" % y1,end="\n")   
            break
        y0 = y1
        i += 1    
       
def exercise_25():
    x = "Нахождение числа ПИ по формуле Грегори с минимальным количеством слагаемых с заданной точностью"
    pi_list = '3.1415926535897932384626433832795028841971'
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",pi_list,"\n\t\t","-"*len(x), sep="" ) 
    
    view_symbols = input("Сколько символов числа пи вы хотите просмотреть: ")
    
    view_symbols = int(view_symbols)
    
    tmp = ''
    for i in range(view_symbols+2):
        tmp += pi_list[i]
    pi_list = Decimal(tmp)
           
    number_pi = Decimal(0)
    number_pi_tmp = Decimal(0)
    denominator = Decimal(3)
    count = 1
    
    while True:
        if count % 2 == 1:
            number_pi_tmp -= 1/denominator
        else:
            number_pi_tmp += 1/denominator
        
        number_pi = 4*(1+number_pi_tmp)
        
        print(number_pi,"\t" ,round(number_pi,view_symbols), "\t", pi_list)
        if pi_list == round(number_pi,view_symbols):
            if (view_symbols % 10 == 1) and (view_symbols != 11) and (view_symbols != 12):
                print(f"Минимальное количество слагаемых нужное для нахождения числа ПИ с точностью {view_symbols} символ равно: {count}")
            elif (view_symbols % 10 == 2) or (view_symbols % 10 == 3) or (view_symbols % 10 == 4) and (view_symbols < 10) or (view_symbols > 14):
                print(f"Минимальное количество слагаемых нужное для нахождения числа ПИ с точностью {view_symbols} символа равно: {count}" )
            else:
                print(f"Минимальное количество слагаемых нужное для нахождения числа ПИ с точностью {view_symbols} символов равно: {count}" )
            break 
        
        denominator += 2
        count += 1
        
       
    
    
       
    
def exercise_26():
    x = "еще не реализовано"
        
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )    
    
def exercise_27():
    x = "еще не реализовано"
        
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )    
    
def exercise_28():
    x = "еще не реализовано"
        
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )    
  
def exercise_29():
    x = "Дана последовательность состоящая из дробей:"
    x1 = "1/2, 3/4 , 5/6, 7/8 ......"
    x2 = "Какое минимальное количество элементов нужно сложить, что бы сумма превысила заданное число S "    
                
    print("\n\t\t","-"*len(x2),"\n\t\t",x,"\n\t\t",x1,"\n\t\t",x2,"\n\t\t","-"*len(x2), sep="" )    
    
    while True:
        S = input("\n\tВведите число S: ")
        
        if checking_for_a_number(S):
            S = float(S)
            if S < 1:
                break
            else:
                print("Ошибка вы ввели число больше 1, попробуйте снова")
        else:
            print("Ошибка вы ввели не число, попробуйте снова")
    
    equal = 0.0
    numerator_and_denominator = 1.0
    count = 0
    
    while equal < S:
        equal = numerator_and_denominator/(numerator_and_denominator+1)
        print(f"\nЧисло {count+1}:\t",
              "%.0f" % (numerator_and_denominator), "/", "%.0f" % (numerator_and_denominator + 1),
              "равно", f"%.{len(list_of_symbols_after_dot(S))-2}f" % equal, end="")
        numerator_and_denominator += 2
        count += 1
                
    print("\n\nМинимальное количество для нахождения суммы равной ", f"%.{len(list_of_symbols_after_dot(S))-2}f" % equal, f"равно {count}")
    
def exercise_30():
    x = "еще не реализовано"
        
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )    
    
def exercise_31():
    x = "еще не реализовано"
        
    print("\n\t\t","-"*len(x),"\n\t\t",x,"\n\t\t",x,"\n\t\t","-"*len(x), sep="" )    
              
def main():
    while True:
        x = input("\n\t\tВведите номер задания 21 - 31 ддя начала (q для выхода): ")
        
        flag = True
        os.system('CLS')
        
        while flag != False:
            match x:
                case '21':
                    exercise_21()
                case '22':
                    exercise_22()   
                case '23':
                    exercise_23()
                case '24':
                    exercise_24()
                case '25':
                    exercise_25()
                case '26':
                    exercise_26()
                case '27':
                    exercise_27()   
                case '28':
                    exercise_28()
                case '29':
                    exercise_29()
                case '30':
                    exercise_30()
                case '31':
                    exercise_31()
                case 'q' :
                    return
                case _:
                    print("\n\t\t\tКоманда или номер задания не найдены, попробуйте снова\n")
                    break
            
            while True:
                y_or_n = input('\n\t\tdo you want to continue?(y/n): ')
                match y_or_n:
                    case 'y':
                        os.system('CLS')
                        flag = False
                        break   
                    case 'n' :
                        return 
                    case 'r':
                        os.system('CLS')
                        break
                    case _:
                        print("\n\t\t\tКоманда или номер задания не найдены, попробуйте снова\n")
                         
main()    
   