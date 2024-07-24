# Exercise : To count frequency of element in an array

def count_frequencies(arr):
    frequency_dict = {}
    for item in arr:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequencies = count_frequencies(array)
print("Frequencies:", frequencies)
