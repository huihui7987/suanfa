#-*- coding:utf-8 -*-
'''
异或运算是常见的二进制运算，给出两个n位二进制数a，b。a异或b的运算依次考虑二进制的每一位，
若这一位相同，那么这一位的异或结果就是0，不同就是1。
例如a=1100, b=0100。执行a异或b的运算，a的最高位是1，b的最高位是0，
两个数字不同所以最高位异或结果是1；a和b次高位都是1，所以次高位异或为0；最后两位它们都是0，所以异或结果也都是0。那么a异或b的答案就是1000。
现在输入两个n位二进制数，输出它们异或结果的十进制答案。上述样例中异或的二进制结果为1000，转化成十进制就是8。
输入有三行，第一行一个数n(1<=n<=20)，接下来两行有两个n位二进制数。输入的二进制数可能有前导零。

def tmp():
    n = int(raw_input())
    m = []
    res = []
    for i in xrange(2):
        m.append(raw_input())
    num1 = m[0]
    num2 = m[1]
    for i in xrange(n):
        if num1[i] == num2[i]:
            res.append('0')
        else:
            res.append('1')
    rr = ''.join(res)
    return int(rr,2)

print(tmp())
'''
'''
第一行一个正整数 n ( 2≤N≤200 )，表示运输个的数量。
接下来n行，每行两个整数X和L(1≤X、L≤109)，表示一辆车的x轴坐标和长度。

'''
def bbb():
    n = int(raw_input())
    m = []
    res = []
    su = []
    xi = []
    mm=0
    count = 1

    for i in xrange(n):
        m.append(raw_input())

    for j in xrange(n):
        res.append(m[j].split())
        su.append(int(res[j][0]) + int(res[j][1]))#长度
        xi.append(int(res[j][0]))#首
    while mm<n:
        for k in xrange(1,n):
            if xi[k] >=xi[mm] and xi[k]<= su[mm]:
                count+=1


    return count







print(bbb())