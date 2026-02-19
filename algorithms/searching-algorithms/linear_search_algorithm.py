#Linear Search = start from the beginning, compare every element until you find the target (or run out of hope).

def linear_search_algo(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
