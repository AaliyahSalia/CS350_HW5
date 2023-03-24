# In an algebraic expression, such as "x – (y + z)", generate a function/method based
# on stack operations to rewrite it without parenthesis, like "x – y – z", ONLY
# considering + and – operators in this expression. If an expression is "x – (y – z –
# (u+v) ) – w", the new format should be "x – y + z + u + v – w" after
# function/method call

def rewrite_expression(expr):
    stack = []
    result = ""
    sign = 1

    for i in range(len(expr)):
        if expr[i] == '+':
            result += sign * '+'
        elif expr[i] == '-':
            result += sign * '-'
        elif expr[i] == '(':
            stack.append(sign)
            sign = 1
        elif expr[i] == ')':
            stack.pop()
        else:
            result += sign * expr[i]
            if len(stack) > 0:
                sign = stack[-1]
    
    return result

expr = "x - (y - z - (u+v)) - w"
rewritten_expr = rewrite_expression(expr)

print("Original expression: ", expr)
print("Rewritten expression:", rewritten_expr)
