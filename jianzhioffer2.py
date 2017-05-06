#-*-coding:utf-8 -*-
class Tree:
    def __init__(self, data, leftchild,rightchild):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

def hasSubTree(binTree1,binTree2):
    res = False
    while binTree1!=None and binTree2 != None:
        if binTree1.data == binTree2.data:
            res = DoesSubTree(binTree1,binTree1)
        if not res:
            hasSubTree(binTree1.left,binTree2)
        if not res:
            hasSubTree(binTree1.right,binTree2)
    return res


def DoesSubTree(binTree1,binTree2):
    if binTree1 == None:
        return False
    if binTree2 == None:
        return True
    if binTree1.data != binTree2.data:
        return False
    return DoesSubTree(binTree1.left,binTree2.left) and DoesSubTree(binTree1.right,binTree2.left)#root 相等下，左右叶节点是否相等

def IsPopOrde(pushV,popV):#[1,2,3,4,5],[4,5,3,2,1]
    #if pushV == None or popV == None:
    #    return
    if pushV.sort() != popV.sort():
        return False

    indexV = []
    res = False
    for i in popV:
        indexV.append(pushV.index(i))


    for j in range(len(indexV)-1):
        tmp = []
        tmpN = indexV[j]
        for h in range(j,len(indexV)):
            if indexV[h]<=tmpN:
                tmp.append(indexV[h])
        res = isReverOrder(tmp)

        if not res:
            return False

    return True

def isReverOrder(listV):

    for i in range(len(listV)-1):
        if listV[i]<listV[i+1]:
            return False

    return True

#print (IsPopOrde([1],[2]))

def VerifySquenceOfBST(sequence):
    # write code here
    if sequence == None:
        return False
    root = sequence[len(sequence)-1]
    leftsubseq = []
    rightsubseq = []
    leftsubseq.append([x for x in sequence if x < root])
    rightsubseq.append([x for x in sequence if x > root])

    left = True
    right = True
    while len(leftsubseq) >1 and len(rightsubseq)>1:
        left = VerifySquenceOfBST(leftsubseq[0])
        right = VerifySquenceOfBST(rightsubseq[0])

    return left and right

#print(VerifySquenceOfBST([4,8,6,12,16,14,10]))


def Permutation(ss):
    # write code here
    if not ss:
        return []

    if len(ss) == 1:
        return [ss]

    else:
        result = []
        a = ss[-1]
        for ii in Permutation(ss[:-1]):
            for j in range(len(ii) + 1):
                result.append(ii[:j] + a + ii[j:])

        result = list(set(result))
        result.sort()
        return result
#print(Permutation('abc'))

def MoreThanHalfNum_Solution(numbers):
    # write code here

    res = []
    n = len(numbers)
    for i in numbers:
        tmp = numbers.count(i)
        if tmp > 0.5 * n:
            break
    return i


#print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))

def FirstNotRepeatingChar(s):
    # write code here
    if s == None:
        return -1
    while s:
        for ss in s:
            d = s.count(ss)
            if d == 1:
                break
        break
    return ss

#print(FirstNotRepeatingChar('adsfawsf'))


def getNumsOfK(nums,k):
    if nums==None:
        return None
    if nums:
        firstK = getFirK(nums,k)
        lastK = getLastK(nums,k)
        if firstK > -1 and lastK > -1:
            number = lastK-firstK+1
    return number

def getFirK(nums,k):
    low = 0
    high = len(nums)-1
    mid = round(0.5 * (high-low))-1

    if low > high:
        return False
    if nums[mid] == k:
        if (mid >=0 and nums[mid-1] !=k ) or mid == 0:
            return mid
        else:
            high = mid- 1
    else:
        if nums[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return getFirK(nums[0:high],k)


def getLastK(nums,k):
    low = 0
    high = len(nums) - 1
    mid = round(0.5 * (high - low))-1

    if low > high:
        return False
    if nums[mid] == k:
        if (mid <high and nums[mid - 1] != k) or mid == high:
            return mid
        else:
            low = mid + 1
    else:
        if nums[mid] > k:
            low = mid + 1
        else:
            high = mid - 1
    return getLastK(nums[low::],k)

#nums = [1,2,3,4,4,4,4,4,4,5,6,7]
#k=4
#print(getNumsOfK(nums,k))


def FindNumbersWithSum(array, tsum):
    # write code here
    if array == None:
        return []
    start = 0
    end = len(array) - 1

    while start < end:

        if array[start] + array[end] > tsum:
            end -= 1
        if array[start] + array[end] < tsum:
            start += 1
        if array[start] + array[end] == tsum:
            return array[start], array[end]

    return []

#print(FindNumbersWithSum(array=[1,2,4,7,11,16],tsum=10))

def FindContinNumberWithSum(tsum):
    if tsum == None:
        return []
    start = 1
    end = 3
    res = []
    while start < end-1:
        tmp = sum(range(start, end))

        if tmp < tsum:
            end += 1
            tmp = sum(range(start, end))

        if tmp > tsum:
            start += 1
            tmp = sum(range(start, end))
        if tmp == tsum:
            res.append(range(start, end))
            start += 1
    return res

#print(FindContinNumberWithSum(tsum=3))

def LastRemaining_Solution(n, m):
    # write code here
    if n < 1 or m < 1:
        return None
    last = 0
    for i in range(1, n+1):#最后一个为n,range()函数取不到最后一个
        last = (last + m) % i

    return last

#print(LastRemaining_Solution(5,3))
def duplicate(numbers):
    # write code here

    duplication = []
    for i in numbers:
        if numbers.count(i) > 1:
            duplication.append([i])

    if duplication is not None:
        return True,duplication[0]


    return False,duplication

#print(duplicate([2,1,3,1,4]))


def duplicate(numbers):
    # write code here
    # duplication = []
    '''


    for i in numbers:
        if numbers.count(i) > 1:
            duplication[0] = i
            return True
    return False
    '''
    app = []
    numbers.append("NA")
    numbers.append("NA")
    if not numbers or len(numbers) <= 1:
        return False
    for i in range(0, len(numbers)):
        while numbers[i] != i:
            if numbers[i]=="NA":
                ind = i
                break
            if numbers[i] != numbers[numbers[i]]:
                tmp = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = tmp



                #app.append(numbers[i])
                #break


    return [numbers.index('NA'),ind]
#print(duplicate([0,2,4,1,6]))

import types


def SumEmulator(num):  # num = '35499'

    i = len(num) - 1
    flag = 0
    lastNum = ''

    while True:
        if i == -1:
            return '1' + lastNum
        elif num[i] == '9':
            lastNum = '0' + lastNum
            i -= 1
        else:
            lastNum = str(int(num[i]) + 1) + lastNum
            return num[:i] + lastNum


def Print1ToMaxOfNDigits(num):  # num = '35499'

    if num == '':
        return False
    else:
        i = 0
        while i <= int(num) - 1:
            print (SumEmulator(str(i)))
            i += 1
    return 0


#Print1ToMaxOfNDigits('334')

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists)/2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result+= left[l:]
    return result
#print (MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))

def findTopNMinOf2DArray(arr,k):
    '''
    二维数组，行列递增，求topN 小
    对整个数组进行k次扫描
    每一次扫描都包每一行的最小元素进行比较，找出这次比较中的最小值 min，
    如果这次找出的元素师在第i行第j列，那么第i行下一次比较就从j+1开始 ,
    (譬如说第一次扫描的最小值是0行的0列元素，那么第二次扫描第0行第0列元素就会被排除，
    第0行从第1列开始比较）
    当第K次扫描后，所得的min就是整个数组的
    :param arr:
    :param k:
    :return:
    '''
    minN = arr[0][0]
    rows = len(arr)
    cols = len(arr[0])


    minOfRows = [0 for i in range(rows)]
    minOfRows[0]=1
    res = []
    res.append(minN)

    for i in range(k-1):
        minN = 1000
        for j in range(rows):
            if minOfRows[j]<cols:
                if arr[j][minOfRows[j]]<minN:
                    minN = arr[j][minOfRows[j]]
                    r=j
        minOfRows[r]+=1
        res.append(minN)
    return res
arr = [[1,2,3,4],[2,3,4,5],[4,5,6,7],[7,8,9,99]]
print(findTopNMinOf2DArray(arr,4))


def findTopNMaxOf2DArray(arr,k):
    '''
    二维数组，行列递增，求topN 大

    :param arr:
    :param k:
    :return:
    '''

    rows = len(arr)
    cols = len(arr[0])
    maxN = arr[rows-1][cols-1]

    maxOfRows = [rows-1 for i in range(rows)]
    maxOfRows[-1] = rows-2

    res = []
    res.append(maxN)
    for i in range (k-1):
        maxN=0
        for j in range(rows-1,-1,-1):
            if arr[j][maxOfRows[j]]>maxN:
                maxN = arr[j][maxOfRows[j]]
                r=j
        maxOfRows[r] -= 1
        res.append(maxN)
    return res

arr = [[1,2,3,4],[2,3,4,5],[4,5,6,7],[5,6,9,10]]
print(findTopNMaxOf2DArray(arr,4))



















