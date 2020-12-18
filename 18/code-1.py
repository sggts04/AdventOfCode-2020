import sys

sum = 0

for line in sys.stdin:
    line = line.rstrip()
    expr = []
    for elem in line:
        if elem!=' ':
            expr.append(elem)
    expr.append(')')
    stack = ['(']
    for exp in expr:
        if exp != ')':
            stack.append(exp)
        else:
            solve = []
            a = stack.pop()
            while a != '(':
                solve.append(a)
                a = stack.pop()
            solve = solve[::-1]
            ans = 0
            opr = '-'
            for c in solve:
                if c=='+':
                    opr = c
                elif c=='*':
                    opr = c
                else:
                    if opr=='-':
                        ans = int(c)
                    elif opr=='+':
                        ans = ans + int(c)
                    else:
                        ans = ans*int(c)
            stack.append(str(ans))
    sum += int(stack[0])

print(sum)
