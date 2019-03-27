'''
Find largest element in an array without using loops and builtin function.
'''
def find_largest(array, i):
    if i == len(array)-1:
        return array[i]
    else:
        ele = find_largest(array, i+1)

    if ele > array[i]:
        return ele
    else:
        return array[i]


input_1 = [1, 2, 3, 4, 5]
input_2 = [5, 2, 3, 4, 1]
input_3 = [1, 2, 5, 4, 3]
input_4 = [3, 5]
input_5 = [5, 3]

assert find_largest(input_1, -1) == 5
assert find_largest(input_2, -1) == 5
assert find_largest(input_3, -1) == 5
assert find_largest(input_4, -1) == 5
assert find_largest(input_5, -1) == 5