'''
Count number of bits that are set to 1 in positive integer
'''
def count_bits(num):
    bit_count = 0

    while num:
        bit_count += num & 1
        num = num >> 1

    return bit_count


assert count_bits(0) == 0
assert count_bits(1) == 1
assert count_bits(2) == 1
assert count_bits(3) == 2
assert count_bits(4) == 1
assert count_bits(5) == 2
assert count_bits(6) == 2
assert count_bits(7) == 3
assert count_bits(8) == 1
assert count_bits(9) == 2


# Not sophisticated solution, it gives correct result but its not correct way to solve it. How will you solve it C?
def count_bits_not_sophisticated(num):
    return bin(num).count('1')


assert count_bits_not_sophisticated(0) == 0
assert count_bits_not_sophisticated(1) == 1
assert count_bits_not_sophisticated(2) == 1
assert count_bits_not_sophisticated(3) == 2
assert count_bits_not_sophisticated(4) == 1
assert count_bits_not_sophisticated(5) == 2
assert count_bits_not_sophisticated(6) == 2
assert count_bits_not_sophisticated(7) == 3
assert count_bits_not_sophisticated(8) == 1
assert count_bits_not_sophisticated(9) == 2