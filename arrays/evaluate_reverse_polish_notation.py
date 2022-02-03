# Time: O(n); Space: O(n)
def eval_rpn(tokens):
    stack = []

    for t in tokens:
        if t.isdigit() or t[1:].isdigit():
            stack.append(int(t))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if t == '+':
                stack.append(num1 + num2)
            elif t == '-':
                stack.append(num2 - num1)
            elif t == '*':
                stack.append(num1 * num2)
            elif t == '/':
                stack.append(int(num2 / num1))

    return stack[0]


# Test cases:
print(eval_rpn(["2", "1", "+", "3", "*"]))
print(eval_rpn(["4", "13", "5", "/", "+"]))
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(eval_rpn(["3", "11", "+", "5", "-"]))
print(eval_rpn(["4", "3", "-"]))
print(eval_rpn(["4"]))
