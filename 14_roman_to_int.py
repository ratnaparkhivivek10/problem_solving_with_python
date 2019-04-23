roman_int_map = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def roman_to_int(roman_str: str) -> int:
    '''
    Converts valid roman string to integer
    '''
    sum_ = 0
    size = len(roman_str) - 1

    for i, symbol in enumerate(roman_str):
        if symbol == 'I' and i < size:
            if roman_str[i+1] == 'V' or roman_str[i+1] == 'X':
                sum_ += -1
                continue
        if symbol == 'X' and i < size:
            if roman_str[i+1] == 'L' or roman_str[i+1] == 'C':
                sum_ += -10
                continue
        if symbol == 'C' and i < size:
            if roman_str[i+1] == 'D' or roman_str[i+1] == 'M':
                sum_ += -100
                continue

        sum_ += roman_int_map[symbol]
    
    return sum_


assert roman_to_int('I') == 1
assert roman_to_int('V') == 5
assert roman_to_int('III') == 3
assert roman_to_int('IV') == 4
assert roman_to_int('IX') == 9
assert roman_to_int('LVIII') == 58
assert roman_to_int('MCMXCIV') == 1994