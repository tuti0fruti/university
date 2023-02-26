import random

n = 4
k = 6

array = [[0]*n for i in range(k)]
average_score_all = 0
count_string_equal = 0
count_string_more = 0

for i in range(k):
    average_score = 0
    print("Оценки студента ", i+1, end="\n")
    for j in range(n):
        array[i][j] = random.randint(1,5)
        average_score += array[i][j] 
        average_score_all += array[i][j]
        print("%.0f" % array[i][j] , end='\t')
    print(f"\tСредний балл {average_score/n}")    
    
print ("\nОбщий средний балл равен ", "%.2f" % (average_score_all/(n*k)), "\n")       
    
for i in range(k):
    average_score = 0
    for j in range(n):
        average_score += array[i][j]  
    if average_score/n == average_score_all/(k*n):
        print(f"Средний балл студента {i+1} равный общему среднему баллу и равен {average_score/n}")
        count_string_equal += 1
    elif average_score/n > average_score_all/(k*n):
        print(f"Средний балл студента {i+1} больше общего среднего балла и равен {average_score/n}")
        count_string_more += 1     
        
print(f"\nКоличество студентов получивших средний балл равный общему среднему баллу равно: {count_string_equal}")
print(f"Количество студентов получивших средний балл больше общего среднего балла равно: {count_string_more}")

input()