from random import randrange
def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        left = [i for i in array if i <= pivot]
        right = [i for i in array if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)