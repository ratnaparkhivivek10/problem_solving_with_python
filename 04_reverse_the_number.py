# Iterative solution
def reverse_number(num):
    rev = 0
    while num:
        r = num % 10
        rev = rev * 10 + r
        num = num // 10

    return rev


num = 123043
num_rev = reverse_number(num)

print(num_rev)

# You can reverse the number by using Python language features. However, this is not the right way. For example, see below code.
# We can call it language hack.

# Convert the number in string and reverse it
print(str(num)[::-1])