# count overlapping substrings using built-in find function
def overlapping_substr(string, substr):
    count = 0
    start = 0

    while True:
        i = string.find(substr, start)

        if i < 0:
            break
        else:
            count += 1

        start = i + 1

    return count


string = 'ababababa'
substr = 'aba'

# the builtin count function counts only non-overlapping substrings.
non_overlapping_count = string.count(substr)
print(non_overlapping_count)

# count overlapping substrings
overlapping_count = overlapping_substr(string, substr)
print(overlapping_count)


