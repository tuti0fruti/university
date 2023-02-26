import os
import time
# 1. Создайте список целых чисел от -20 до 30.
# 2. Создайте список из 20 пятерок.
# 3. Создайте список целых чисел от -10 до 10 с шагом 2.
# 4. Заполнить список квадратами чисел от 0 до 9, используя генератор списка.
# 5. Создайте список из сумм троек чисел от 0 до 10, используя генератор списка (0 + 1 + 2, 1 + 2 + 3, …).
# 6. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.

def exercise_1():
    print("\n\t\tЗадание 1\n\tСоздайте список целых чисел от -20 до 30.\n")
    array = [i for i in range(-20,31)]

    for i in range(len(array)):
        print(array[i], end = " ")    

    print()
    
def exercise_2():
    print("\n\t\tЗадание 2\n\t Создайте список из 20 пятерок.\n")

    array = [5 for i in range(20)]

    for i in range(len(array)):
        print(array[i], end = " ")
        
    print("\n\n\tКоличество пятерок: ",len(array))   

def exercise_3():    
    print("\n\n\t\tЗадание 3\n\tСоздайте список целых чисел от -10 до 10 с шагом 2.\n")

    array = [i for i in range(-10,11,2)]

    for i in range(len(array)):
        print(array[i], end = " ")
        
    print()
        
def exercise_4():    
    print("\n\n\t\tЗадание 4\n\tЗаполнить список квадратами чисел от 0 до 9, используя генератор списка.\n")

    array = [i ** 2 for i in range(0,10)]    

    for i in range(len(array)):
        print(array[i], end = " ")
    print()
    
def exercise_5():    
    print("\n\n\t\tЗадание 5\n\tСоздайте список из сумм троек чисел от 0 до 10, используя генератор списка (0 + 1 + 2, 1 + 2 + 3, …).\n")

    array = [i for i in range(7)]

    for i in range(7):
        for j in range(i,i+3):
            array[i] += j
            
    for i in range(len(array)):
        print(array[i], end = " ")
    print()
    
def exercise_6():    
    print("\n\n\t\tЗадание 6\n\tЗаполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.\n")   
        
    a1 = int(input("Введите первый элемент арифметической прогрессии "))
    b = int(input("Введите разность арифметической прогрессии "))
    count_ = int(input("Введите количество элементов арифметической прогрессии "))    
    print()
    a_count = a1
    for i in range(1,count_):
        a_count += b

    array = [i for i in range(a1,a_count+1,b)]

    for i in range(len(array)):
        print(i+1,"-й элемент равен: ",array[i], end = "\n")
        time.sleep(0.2)
        
    

def main():
    while True:
        x = input("\n\t\tВведите номер задания 1 - 6 ддя начала (q для выхода): ")
        
        flag = True
        os.system('CLS')
        
        while flag != False:
            match x:
                case "1":
                    exercise_1()
                case "2":
                    exercise_2()
                case "3":
                    exercise_3()
                case "4":
                    exercise_4()
                case "5":
                    exercise_5()
                case "6":
                    exercise_6()    
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
                        os.system('CLS')
                        print("\n Goodbye \n программа завершиться через: 3", end=" ")
                        time.sleep(1)
                        print("2", end=" ") 
                        time.sleep(1)
                        print("1", end=" ")
                        time.sleep(1)
                        return 
                    case 'r':
                        os.system('CLS')
                        break
                    case _:
                        print("\n\t\t\tКоманда или номер задания не найдены, попробуйте снова\n")
                         
main()    
   