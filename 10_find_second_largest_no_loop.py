def find_second_largest(array, i, max_, second_max):
    if i == len(array)-1:
        if array[i] > max_:
            return max_
        else:
            if array[i] > second_max:
                return array[i]
    else:
        if array[i] > max_:
            second_max = max_
            max_ = array[i]
        else:
            if array[i] > second_max:
                second_max = array[i]
        second_max = find_second_largest(array, i+1, max_, second_max)

    return second_max

input_1 = [1, 2, 3, 4, 5]
input_2 = [5, 2, 3, 4, 1]
input_3 = [1, 2, 5, 4, 3]
input_4 = [3, 5]
input_5 = [5, 3]

print(find_second_largest(input_1, 0, 0, 0))
assert find_second_largest(input_1, 0, 0, 0) == 4
assert find_second_largest(input_2, 0, 0, 0) == 4
assert find_second_largest(input_3, 0, 0, 0) == 4
assert find_second_largest(input_4, 0, 0, 0) == 3
assert find_second_largest(input_5, 0, 0, 0) == 3


