def binaryS(e,array):
    #It will note previous val of mid(for check item not in)
    prev_m = None
    left = 0
    right = len(array) -1
    while True:
        mid = (left+right) // 2
        #if it unable to find that item
        if prev_m == mid:
            break
        prev_m = mid
        if array[mid] == e:
            return mid
        elif array[mid] < e:
            left = mid +1
        elif array[mid] > e:
            right = mid -1
    
def linearS(e,array):
    for i in array:
        if i == e:
            return array[i]