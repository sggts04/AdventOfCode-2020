import sys

path = []
dict = {}
valid = 0
for line in sys.stdin:
    line = line.rstrip()
    if line=='':
        if len(dict.keys())==8:
            print(dict)
            valid+=1
        elif len(dict.keys())==7 and ('cid' not in dict):
            print(dict)
            valid+=1
        dict = {}
        continue
    ex = line.split(" ")
    for cred in ex:
        k = cred.split(":")[0]
        v = cred.split(":")[1]
        dict.update({k: v})
    

print(valid)
