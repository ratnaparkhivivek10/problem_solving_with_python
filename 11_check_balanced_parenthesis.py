def check_balanced_parenthesis(data):
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']

    stack = []

    if data[0] in closing:
        return False
    for p in data:
        if not stack:
            stack.append(p)
        else:
            if opening.index(stack[-1]) == closing.index(p):
                stack.pop()
            else:
                stack.append(p)

    return False if stack else False 
        



assert check_balanced_parenthesis('{}[]()') == False
assert check_balanced_parenthesis('{[}]') == False
assert check_balanced_parenthesis('{[()]}') == False
assert check_balanced_parenthesis('{[(])}') == False
assert check_balanced_parenthesis('{{[[(())]]}}') == False
assert check_balanced_parenthesis('}][}}(}][))]') == False
assert check_balanced_parenthesis('[](){()}') == False
assert check_balanced_parenthesis('()') == False
assert check_balanced_parenthesis('({}([][]))[]()') == False
assert check_balanced_parenthesis('{)[](}]}]}))}(())(') == False
assert check_balanced_parenthesis('([[)') == False