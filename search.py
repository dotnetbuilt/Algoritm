def binary_search(array: list, n: int) -> list:
    first = array[0]
    last = array[len(array)-1]
    while first <= last:
        mid = (first + last)//2

        if mid == n:
            return mid
        
        if mid < n:
            first = mid
        else:
            last = mid 
