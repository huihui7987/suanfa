def tt():
    coun = 0
    ss = 'abbccbb'


    substr = []
    for i in range(len(ss)):
        s2 = ""
        for j in range(i ,len(ss)):


            s2 += ss[j]
            substr.append(s2)


    for k in substr:
        counter = []
        dicK = set(k)
        for h in dicK:
            cou = k.count(h)
            counter.append(cou)
            counter.sort()
            counter = list(set(counter))

        for o in counter:

            if o % 2 != 0:
                break
            coun += 1

    return coun



print(tt())