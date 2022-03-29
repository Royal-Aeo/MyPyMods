def SelectionSort(array,small_to_big=True):
    for i in range(len(array)):
        hold = i
        for ie in range(i+1,len(array)):
            if array[ie] < array[hold] and small_to_big==True:
                hold = ie
            elif array[ie] > array[hold] and small_to_big==False:
                hold = ie
        array[i],array[hold] = array[hold],array[i]

def bubbleSort(array,small_to_big=True):
    for i in range(len(array) - 1):
        next = 0
        for i in range(len(array)-1):
            next += 1
            if array[next] < array[i] and small_to_big == True:
                var = array[next]
                array[next] = array[i]
                array[i] = var
            elif array[next] > array[i] and small_to_big == False:
                var = array[next]
                array[next] = array[i]
                array[i] = var

def interselectionsort(array,small_to_big=True):
    for i in range(1,len(array)):
        hold = array[i]
        back_itr = i-1
        if small_to_big == True:
            while back_itr >= 0 and hold < array[back_itr]:
                array[back_itr+1],array[back_itr] = array[back_itr],array[back_itr+1]
                back_itr-=1
        elif small_to_big == False:
            while back_itr >= 0 and hold > array[back_itr]:
                array[back_itr+1],array[back_itr] = array[back_itr],array[back_itr+1]
                back_itr-=1