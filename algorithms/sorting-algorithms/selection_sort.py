def selection_sort(lst):
    n = len(lst)

    for j in range(n):
        min_idx = j

        for i in range(j + 1, n):
            if lst[i] < lst[min_idx]:
                min_idx = i

        lst[j], lst[min_idx] = lst[min_idx], lst[j]

    return lst






unsorted=[12,25,11,34,90,22]
print(selection_sort(unsorted))