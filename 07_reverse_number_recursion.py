'''
Reverse a number using recursion
'''
def reverse_number(num, rev):
    if num == 0:
        return rev
    else:
        rev = reverse_number(num//10, rev*10+num%10)
    
    return rev

assert reverse_number(12345, 0) == 54321
assert reverse_number(12305, 0) == 50321
assert reverse_number(11111, 0) == 11111
assert reverse_number(10000, 0) == 1
assert reverse_number(42374, 0) == 47324
assert reverse_number(10001, 0) == 10001