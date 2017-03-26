def getExpectation():
    nums = []
    n = int(raw_input())
    tmpsum = 0


    for i in range(n):
        tmp = raw_input().strip().split()
        tmp = map(int,tmp)
        nums.append(tmp)
        tmpsum += nums[i][0] * float(nums[i][1]/100.0)
    rr = '%.3f' % tmpsum
    return rr




print(getExpectation())