
arr1 = [1,3,5,7,9]
arr2 = [2,3,10,20,30]
arr3 = [1,1,1,1,1]
all_arr = [arr1, arr2, arr3]

def minMax(arr):
    ordered_array = sorted(arr)
    min = sum(ordered_array[:len(arr)-1])
    max = sum(ordered_array[1:])
    print(min, max)
minMax(arr1)

for i in(all_arr):
    minMax(i)