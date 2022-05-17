a = [1,1,3,2,1]

def countingSort(arr):
    lst = [0] * 100
    for i in arr:
        lst[i] = lst[i] + 1
    return lst

print(countingSort(a))


