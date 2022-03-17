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