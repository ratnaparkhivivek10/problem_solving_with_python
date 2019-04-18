def two_sum(nums, target):
    d = {}
    for i, item in enumerate(nums):
        c = target - item
        if c in d:
            return [d[c], i]
        else:
            d[item] = i


assert two_sum([1, 2, 3, 4, 5], 8) == [2, 4]

