#Exercise : To find smallest number in an array
 
def find_smallest_number(arr):
    if not arr:
        return None  # Return None if the array is empty
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

array = [34, 15, 88, 2, 49, 19]
print("The smallest number in the array is:", find_smallest_number(array))
