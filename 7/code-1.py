import sys

def check(colour):
    if dict[colour][0] == 'other bags.':
        return 0
    if 'shiny gold' in dict[colour]:
        return 1
    else:
        for col in dict[colour]:
            ans = check(col)
            if ans==1:
                return 1
    return 0

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
        giv.append(color)
    dict.update({col: giv})

for col in dict:
    bags += check(col)

print(bags)