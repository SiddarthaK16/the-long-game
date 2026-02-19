def bubble_sort(arr):
    n=len(arr)

    for passes in range(n):
        for j in range(n-passes-1):
            if (arr[j]>arr[j+1]):
                 arr[j] , arr[j+1] = arr[j+1],arr[j]

    return arr


arr=[23,44,12,2,43,456,1000,11]
print(bubble_sort(arr))

    
           
         
         

   


    


        