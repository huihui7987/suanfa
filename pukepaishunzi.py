def IsContinuous(numbers):
    # write code here

    if not numbers:
        return False

    ll = numbers
    ll.sort()
    i = 0
    count0 = 0

    while 1:#统计0的个数
        if ll[i] == 0 and i <= 4:
            count0 += 1
        else:
            break
        i += 1

    countN = 0#统计中间需要用0填补的个数，
    for j in range(count0, len(ll) - 1):
        countN += ll[j + 1] - ll[j] - 1

    if count0 >= countN and countN >= 0:#如果0的个数大于需要的填补个数，则可以构成，否则，False
        
        return True
    return False

print IsContinuous(numbers=[1,3,2,5,0])