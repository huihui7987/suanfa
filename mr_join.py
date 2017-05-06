# -*- coding: utf-8 -*-
# Mapper.py




import os

import sys


# mapper脚本
def mapper():
    # 获取当前正在处理的文件的名字，这里我们有两个输入文件
    # 所以要加以区分
    filepath = os.environ["map_input_file"]

    filename = os.path.split(filepath)[-1]

    for line in sys.stdin:
        if line.strip() == "":
            continue

        fields = line[:-1].split("\t")
        sno = fields[0]

        # 以下判断filename的目的是不同的文件有不同的字段，并且需加上不同的标记
        if filename == 'a.txt':
            name = fields[1]
                # 下面的数字'0'就是为数据源1加上的统一标记
            print('\t'.join((sno,'0',name)))
        elif filename == 'db.txt':
            courseno = fields[1]
            grade = fields[2]

            # 下面的数字'1'就是为数据源1加上的统一标记
            print('\t'.join((sno,'1',courseno,grade)))



def reducer():
    lastsno = ""
    for line in sys.stdin:
        if line .strip() == " ":
            continue
        fields = line[:-1].split('\t')
        sno = fields[0]
        '''
        处理思路： 遇见当前key与上一条key不同并且label=0，就记录下来name值，
        当前key与上一条key相同并且label==1，则将本条数据的courseno、
        grade联通上一条记录的name一起输出成最终结果
        '''
        if sno != lastsno:
            name = ""
            '''
            没有判断label==1的情况，因为sno != lastno ,且label=1标红
            该key没有数据源1 的数据

            '''
            if fields[1] == '0':
                name = fields[2]
        elif sno == lastsno:
            if fields[1] == "1":
                courseno = fields[2]
                grade = fields[3]

            if name:
                print('\t'.join((lastsno,name,courseno,grade)))
                lastsno = sno




if __name__ == '__main__':
    mapper()
    reducer()
