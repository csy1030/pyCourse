"""
    二分法查找有序数列
"""

# class Search:
#     def __init__(self):
#     def bi_search()

def bi_search(target,key):
    low = 0
    high = len(target)-1
    while low <= high:
        mid = (low + high) // 2
        if target[mid] < key:
            low = mid + 1
        elif target[mid] > key:
            high = mid -1
        else:
            return mid
    return

print(bi_search([1,3,4,5,6,7,8,9],1))