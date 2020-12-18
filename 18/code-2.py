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

            i=0
            while i<len(solve):
                if solve[i] != '+':
                    i+=1
                else:
                    a = int(solve[i-1])
                    b = int(solve[i+1])
                    c = a+b
                    solve.pop(i-1)
                    solve.pop(i-1)
                    solve.pop(i-1)
                    solve.insert(i-1, c)
                    i=0

            ans = 0
            opr = '-'
            for c in solve:
                if c=='*':
                    opr = c
                else:
                    if opr=='-':
                        ans = int(c)
                    else:
                        ans = ans*int(c)
            stack.append(str(ans))

    sum += int(stack[0])

print(sum)
