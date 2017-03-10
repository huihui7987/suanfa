
def loopword(nums):
    #tmp = []
    #T = 5
    #counters = 0


    for word in nums:
        for chr in range(len(word)):
            ll = word[chr:]+word[:chr]
            if ll in nums and ll != word:#与is not 区别
                nums.remove(ll)



    return len(set(nums))

'''
ast
ats
tas
tsa
sat
sta
ttt
'''
'''
T = int(raw_input())
words = []
if T <= 50 :
    for i in range(T):
        ss = raw_input()
        if len(ss)>=1 and len(ss)<=50:
            words.append(ss)
'''
words = ['ast','ats','tas','tsa','sat','sta','ttt']

print (loopword(words))