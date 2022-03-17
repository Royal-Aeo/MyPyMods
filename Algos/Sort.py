def SelectionSort(array):
    for i in range(len(array)):
        smallest = i
        for ie in range(i+1,len(array)):
            if array[ie] < array[smallest]:
                smallest = ie
        array[i],array[smallest] = array[smallest],array[i]
