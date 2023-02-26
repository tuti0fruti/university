import random

def test(array):
    n = len(array)
    k = 0

   #array = [0]*n

    count_ = [0]*len(array)
    number_ = [0]*len(array)

    # for i in range(n):
    #     array[i] = random.randrange(1,100)
    print(array, '\t изначальный массив')

    array.sort()

    count_[0] = 1
    number_[0] = array[0]

    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            count_[k] += 1
            number_[k] = array[i]
            continue
        else:
            k += 1
            number_[k] = array[i]
            count_[k] = 1
            continue   

    print(array,'\t отсортированный массив') 

    i = 0
    while number_[i] != 0:   
        print("Число ", number_[i], " встречается\t", 100/n*count_[i], "%")
        i += 1
        if i >= n:
            break
    else:
        print("Все элементы нулевые")   
        
        
test([1,2,3,4,5,6])
test([0,0,0,0,0,0,0,0])
test([3,3,3,3,3,3,3,3])
test([1,2,3,3,3,3,3,3,6,7,8,9,9,9,9,9,9,9,9,9,10,100])
test([9,9,9,9,9,6,5,4,7,7])