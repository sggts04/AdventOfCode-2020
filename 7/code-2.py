import sys

def check(colour):
    if dict[colour][0] == 'other bags.':
        return 0
    total = 0
    for col in dict[colour]:
        ans = check(col)
        ans+=1
        total += ans
    return total

dict = {}
bags = 0
for line in sys.stdin:
    line = line.rstrip()
    #path.append(line)
    col = line.split(" bags")[0]
    giv = []
    for elem in line.split(" contain ")[1].split(', '):
        elem = elem.split(' ')
        color = elem[1] + ' ' + elem[2]
        if elem[0]!='no':
            num = int(elem[0])
            for i in range(num):
                giv.append(color)
        else:
            giv.append(color)
    dict.update({col: giv})

bags = check('shiny gold')

print(bags)