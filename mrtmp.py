import os
filepathA = '/Users/ghuihui/PycharmProjects/suanfa/a.txt'
filepathB = '/Users/ghuihui/PycharmProjects/suanfa/b.txt'

def readA(filepath):
    with open(filepath) as file:
        lineread = file.readlines()
    for line in lineread[1::]:
        line = line.strip().split("\\t")
        sno = line[0]
        statyear = line[1]
        num = line[2]
        # 下面的数字'0'就是为数据源1加上的统一标记
        print('\t'.join((sno, 'a', statyear,num)))
        #print(line)


def readB(filepath):
    with open(filepath) as file:
        lineread = file.readlines()
    for line in lineread[1::]:
        line = line.strip().split("\\t")
        sno = line[0]
        name = line[1]
        statyear = line[2]
        num = line[3]
        # 下面的数字'0'就是为数据源1加上的统一标记
        print('\t'.join((sno,'b',name,statyear,num)))
        #print(line)


readA(filepathA)
readB(filepathB)






