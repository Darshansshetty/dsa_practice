def find_max(arr):
    max_value=arr[0]
    for num in arr:
        if num>max_value:
            max_value=num
    return max_value
arr=[6,34,21,56]
print("the largest element is:",find_max(arr))