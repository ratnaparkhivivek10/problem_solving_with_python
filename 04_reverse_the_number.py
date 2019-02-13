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