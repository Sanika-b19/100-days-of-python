# Exrcise : To find second smallest and second largest element in an array

def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None  
    
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None

    return second_smallest, second_largest

array = [34, 15, 88, 2, 49, 19]
second_smallest, second_largest = find_second_smallest_largest(array)
print("The second smallest number in the array is:", second_smallest)
print("The second largest number in the array is:", second_largest)
