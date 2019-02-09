def binary_search(data, item):
    '''
    Returns index of an item if found in data else returns -1
    '''
    assert len(data) != 0, "List should not be empty"
    data = sorted(data)
    
    low = 0
    high = len(data) - 1

    item_index = -1

    while low <= high:
        mid = (low + high)//2
        guess = data[mid]

        if guess == item:
            item_index = mid
            break
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1

    return item_index



data = [0, 1, 2, 3, 4, 5]
index = binary_search(data, 0)

print(index)

