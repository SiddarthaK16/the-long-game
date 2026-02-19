# In BS , array is sorted.. so sort if not bfr applying

def binary_search(arr,target):
    
    start=0
    end=len(arr)-1

    while start <=end:
        middle = (end+start) // 2

        if target>arr[middle]:
            start=middle+1

        elif target<arr[middle]:
            end=middle-1

        else:
            return middle

    return -1

    



s=[10,23,35,45,59,70,85]
target=50

print(binary_search(s,85))

