def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        midpoint = left + (right - 1) // 2
        current = sorted_array[midpoint]
        if current == target:
            return midpoint
        else:
            if target < current:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return "Key not in array"

arr=[1,2,3,4,5,6,7,8,9]
key=8
print(binary_search(arr,key))