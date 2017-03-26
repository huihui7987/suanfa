'''
def FindGreatestSumOfSubArray(array):
    # write code here
    if not array:
        return 0
    maxsum = array[0]
    presentsum = 0
    maxsumlist = []
    for presentindex in range(0, len(array)):
        if presentsum <= 0:
            presentsum = array[presentindex]
        else:
            presentsum = presentsum + array[presentindex]
        if presentsum > maxsum:
            maxsum = presentsum
            maxsumlist.append(maxsum)
    return maxsum,maxsumlist

def FindGreatestSumIndexOfSubArray(sum_max):

    mm = 0
    for i in sum_max:
        if i > mm:
            mm = i
    return sum_max.index(mm)#返回最大元素下角标



array = [1,-2,3,10,-4,7,2,-5]
maxsum,maxsumlist = FindGreatestSumOfSubArray(array)
res = FindGreatestSumIndexOfSubArray(maxsumlist)
print(res)


# -*- coding:utf-8 -*-

def jumpFloor(number):
    # write code here
    if number == 0:
        return 1
    if number == 1:
        return 1

    elif number >= 2:
        b = 1

        # return self.jumpFloor(number-1) + self.jumpFloor(number-2)
        for i in range(2,number+1):

            b = b*2
    return b
            #return self.jumpFloor(self,number-1) + self.jumpFloor(self, number - 2)
print(jumpFloor(5))

def base(x, m):#32位
    ms = []
    while x:
        ms.append(x%m)
        x //= m
                    # python 3
                    # //：表示整除，保留整数部分
                    #// /：得float类型
    ms.reverse()
    return ms

x = 15
m = 2

hhh = base(x,m)
for i in range(32-len(hhh)):
    hhh.insert(0,'0')
print(hhh)
ms_sre = ''.join(list(map(lambda x:str(x),hhh)))

print(ms_sre)


def NumberOf1(n):
    # write code here
    return sum([(n >> i & 1) for i in range(0, 32)])

print(NumberOf1(7))


def PrintMinNumber(numbers):
    mixN = 0
    for number in numbers:
        lenN = len(str(number))
        qq = 10 ** (lenN-1)
        frenum = int(number / (qq))
        if frenum < mixN:
            maxN = frenum



        #endnum = number % qq
        #print(endnum)
    return frenum

ll = [231,45,23,5678,2]
PrintMinNumber(ll)



def PrintMinNumber(numbers):
    # write code here
    if not numbers:
        return ""

    array = sorted(numbers, key=lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1)))
    return ''.join([str(i) for i in array])


ll = [231, 45, 23, 5678, 2]
print(PrintMinNumber(ll))
'''
'''
def arrSumOfthree(numSet):

    m = len(numSet)  # 行
    n = len(numSet[0])#列

    sumN = 0
    maxsum = 0
    for i in range(m):#行
        for j in range(n - 2):
            sumN = numSet[i][j] + numSet[i][j + 1] + numSet[i][j + 2]
            #print(sumN)
            if sumN > maxsum:
                maxsum = sumN

    for i in range(n):#列
        for j in range(m - 2):
            sumN = numSet[j][i] + numSet[j + 1][i] + numSet[j + 2][i]
            #print(sumN)
            if sumN > maxsum:
                maxsum = sumN
    for i in range(2, n):
        for j in range(m - 2):
            sumN = numSet[j][i] + numSet[j + 1][i - 1] + numSet[j + 2][i - 2]
            #print(sumN)
            if sumN > maxsum:
                maxsum = sumN

    for i in range(n - 2):
        for j in range(m - 2):
            sumN = numSet[j][i] + numSet[j + 1][i + 1] + numSet[j + 2][i + 2]
            #print(sumN)
            if sumN > maxsum:
                maxsum = sumN
    return maxsum


numSet = [[1,2,3,4],[4,5,6,8],[7,8,9,9]]
print(arrSumOfthree(numSet))

'''


def countPath(map, n, m):
    loc_1 = [0, 0]
    loc_2 = [0, 0]
    loc_wrong = []
    for i in range(n):
        for j in range(m):
            if map[i][j] == 1:
                loc_1 = [i, j]
            elif map[i][j] == 2:
                loc_2 = [i, j]
            elif map[i][j] == -1:
                loc_wrong.append([i, j])
    x = abs(loc_1[0] - loc_2[0])
    y = abs(loc_1[1] - loc_2[1])
    res = 1
    for i in range(x):
        res *= ((x + y - i) / float(i + 1))
    return int(res)


map,n,m = [[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0]],3,8
print(countPath(map,n,m))