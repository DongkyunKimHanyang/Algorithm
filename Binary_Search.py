import sys


def binary_search_recur(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recur(array,target,start,mid - 1)
    elif array[mid] < target:
        return binary_search_recur(array,target,mid + 1, end)

def binary_search_loop(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1

#Count range
from bisect import bisect_left,bisect_right
def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

#LIS
array = [1,3,5,2,4,5]
lis_list = [sys.maxsize] * len(array)
lis_idx_list=[]
for i, element in enumerate(array):
    idx = bisect_left(lis_list, element)
    lis_list[idx] = element
    lis_idx_list.append(idx)
print(bisect_left(lis_list,sys.maxsize))

result = []
end = max(lis_idx_list)
for i in range(len(lis_idx_list)-1,-1,-1):
    if lis_idx_list[i] == end:
        result.append(array[i])
        end -= 1
result.reverse()
print(result)