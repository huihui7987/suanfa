# -*- coding:utf-8 -*-
from scipy import stats
import numpy as np



def emsingle(priors,observations):
    '''
    author:ghh

    :param priors: 初始化ThetaA，ThetaB,假设为[0.6,0.4]
    :param obversions:初始化观察值，H为1，T为0
    :return:newThetaA,newThetaB
    '''

    thetaA = priors[0]
    thetaB = priors[1]
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}

    for observation in observations:
        len_observation = len(observation)

        count_H = observation.sum()
        count_T = len_observation - count_H

        contribution_A = stats.binom.pmf(count_H, len_observation, thetaA)
        contribution_B = stats.binom.pmf(count_H, len_observation, thetaB)

        #归一化概率

        weight_A = contribution_A / (contribution_A + contribution_B)
        weight_B = contribution_B / (contribution_A + contribution_B)

        counts['A']['H'] += weight_A * count_H
        counts['A']['T'] += weight_A * count_T
        counts['B']['H'] += weight_B * count_H
        counts['B']['T'] += weight_B * count_T

    newThetaA = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    newThetaB = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])

    return [newThetaA,newThetaB]



def emMain(priors,observations,tol=1e-6, iterations=10000):
    '''

    :param priors:
    :param observations:
    :param tol: 变化阈值
    :param iterations: 迭代次数
    :return:
    '''

    iteration = 0
    while iteration < iterations:
        new_theta = emsingle(priors , observations)
        delta_change = np.abs(new_theta[0] - priors[0])

        if delta_change < tol:
            break
        else:
            priors = new_theta
            iteration += 1
    return [new_theta,iteration]


observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                         [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])
'''
priors = [0.6,0.5]
ss = emMain(priors,observations)
print(ss)

'''


# -*- coding:utf-8 -*-
def maxnumsOne(num):
    binNum = bin(num)

    tmp = 1
    count = 0

    for i in range(2,len(binNum) - 1):
        if binNum[i] == binNum[i + 1]:
            tmp += 1
        if tmp > count and tmp >= 2:
            count = tmp
            tmp = 1

    return count
'''
try:
    while True:
        num = input()
        s = str(bin(num))
        temp =''
        result =''
        for c in s[2:]:
            if c == '1':
                temp += '1'
                if len(temp)>len(result):
                    result = temp
            else:
                temp  = ''
        print (len(result))
except:
    pass
'''
#print(maxnumsOne(11111))

def duplicate(numbers, duplication):
    # write code here


    for i in numbers:
        if numbers.count(i) > 1:
            duplication[0] = i
            return True

        else:
            return False

dd = [2,1,3,1,4]
print(duplicate(dd,[]))

