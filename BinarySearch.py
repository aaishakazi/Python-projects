def binarysearch(arr, target):
    middle = 0
    start = 0 
    end = len(arr) 
    steps = 0
    
    while start <= end:
        print("Step " + str(steps) + ": " + str(arr[start:end+1]))
        steps += 1
        middle = start + (end - start) // 2
        
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
            
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2

binarysearch(my_list, target)