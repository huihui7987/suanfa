# -*- coding:utf-8 -*-
'''
def upstairs():

	n = int(input())
	for i in range(n):
        m = int(input())

        if m <= 0:
        	return 0
        elif m==1:
        	return 1
        elif m>=2:
          a = 0
          b = 1
          a,b = b,a+b
    return b



def jump(n):
#递归
  if n <= 3:
    return n-1
  else:
    return jump(n-1) + jump(n-2)
num = int(input())
for i in range(num):
  n = int(input())
  print(jump(n))


def upstairs(m):

    if m <= 3:
        return m-1
    else:
        a = 1
        b = 2
        for i in range(4,m+1):
            a,b = b,a+b
        return b

print(upstairs(6))
'''

#!/usr/bin/env python
#coding=utf-8

def finddes(list, n):
    s, e = 0, 0
    for i in range(0,n-1):
        if(list[i+1]<list[i]):
            s = i
            break
    for i in range(s+1, n):
        if(i==n-1):
            e = n-1
            break
        elif(list[i+1]>list[i]):
            e = i
            break
    return s,e+1

def testasc(list, s, e):
    if(e-s<2):
        return True
    else:
        for t in range(s, e-1):
            if(list[t+1]<list[t]):
                return False
        return True

def testbound(list, n, s, e):
    if(s==0):
        if(e==1):
            return False
        elif(e==n):
            return True
        else:
            return list[s]<=list[e]
    else:
        if(e==n):
            return list[e-1]>=list[s-1]
        else:
            return list[s]<=list[e] and list[e-1]>=list[s-1]

n = 5#int(raw_input())
#slist = raw_input().split()
list = [1,4,3,2,5] #[int(str) for str in slist]

s, e = finddes(list, n)
if(testasc(list, e, n) and testbound(list, n, s, e)):
    print "yes"
else:
    print "no"
