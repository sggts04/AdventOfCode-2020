import sys

path = []
dict = {}
valid = 0
for line in sys.stdin:
    line = line.rstrip()
    if line=='':
        if len(dict.keys())==7:
            valid+=1
        dict = {}
        continue
    ex = line.split(" ")
    for cred in ex:
        k = cred.split(":")[0]
        v = cred.split(":")[1]
        if k=='byr' and len(v)==4 and int(v)<=2002 and int(v)>=1920:
            dict.update({k: v})
        if k=='iyr' and len(v)==4 and int(v)<=2020 and int(v)>=2010:
            dict.update({k: v})
        if k=='eyr' and len(v)==4 and int(v)<=2030 and int(v)>=2020:
            dict.update({k: v})
        if k=='pid' and len(v)==9:
            try:
                lkd = int(v)
                dict.update({k: v})
            except ValueError:
                continue
        if k=='ecl' and (v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
            dict.update({k: v})
        if k=='hcl' and v[0]=='#' and len(v)==7:
            b = True
            for c in v[1:]:
                if c not in {'0', '1', '2', '3', '4', '5','6', '7' , '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}:
                    b = False
            if b:
                dict.update({k: v})
        if k=='hgt':
            if v[-2:]=='cm':
                ds = v.split("cm")[0]
                try:
                    lkd = int(ds)
                    if lkd<=193 and lkd>=150:
                        dict.update({k: v})
                except ValueError:
                    continue
            if v[-2:]=='in':
                ds = v.split("in")[0]
                try:
                    lkd = int(ds)
                    if lkd<=76 and lkd>=59:
                        dict.update({k: v})
                except ValueError:
                    continue

if len(dict.keys())==7:
    valid+=1
dict = {}

print(valid)
