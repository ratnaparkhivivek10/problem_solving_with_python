def find_second_largest(array):
   max_ = 0 
   second_max = 0
   for item in array:
      if item > max_:
         second_max = max_
         max_ = item
      elif item > second_max:
         second_max = item

   return second_max


input_1 = [1, 2, 3, 4, 5]
input_2 = [5, 2, 3, 4, 1]
input_3 = [1, 2, 5, 4, 3]
input_4 = [3, 5]
input_5 = [5, 3]

assert find_second_largest(input_1) == 4
assert find_second_largest(input_2) == 4
assert find_second_largest(input_3) == 4
assert find_second_largest(input_4) == 3
assert find_second_largest(input_5) == 3