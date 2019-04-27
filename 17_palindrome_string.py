def check_palindrome(s1):
    assert len(s1) >= 3
    
    i = 0
    j = len(s1)-1

    while i < j:
        if s1[i] != s1[j]:
            return False
        i += 1
        j -= 1
    
    return True

assert check_palindrome('abc') == False
assert check_palindrome('aba') == True
assert check_palindrome('abba') == True
assert check_palindrome('nitin') == True

# The same can be easily acheived using Python's builtin function like below.

def check_palindrome_easy(s):
    assert len(s) >= 3
    return s == s[::-1]

assert check_palindrome('abc') == False
assert check_palindrome('aba') == True
assert check_palindrome('abba') == True
assert check_palindrome('nitin') == True