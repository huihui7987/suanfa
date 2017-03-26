'''
def pinghenshu(nums):

    list_n = []
    if nums // 10 == 0:
        return 'No'
    while nums:
        tmp = nums % 10
        nums = nums // 10
        list_n.append(tmp)
    leftmul = 1

    for i in range(len(list_n)-1):
        rimul = 1
        leftmul *= list_n[i]
        for j in range(i+1,len(list_n)):

            rimul *= list_n[j]
        if rimul == leftmul:
            return 'YES'
    return 'No'





res = pinghenshu(nums=int(input()))
print(res)




def reOrderArray(array):
    # write code here
    ji = []
    ou = []
    for i in array:
        if i % 2 == 1:
            ji.append(i)
        else:
            ou.append(i)

    ji.extend(ou)


    return ji

array = [1,2,3,4,5,6]
print(reOrderArray(array))
'''
import random
def selectSong(songs):
    '''

    :param songs:
    2015年百度笔试题目
    假设张三的mp3里有1000首歌，现在希望设计一种随机算法来随机播放。与普通随机模式不同的是，
    张三希望每首歌被随机到的概率是与一首歌的豆瓣评分（0~10分）成正比的，如朴树的《平凡之路》评分为8.9分，
    逃跑计划的《夜空中最亮的星》评分为9.5分，则希望听《平凡之路》的概率与《夜空中最亮的星》的概率比为89:95,。
    现在我们已知这1000首歌的豆瓣评分：

    （1）请设计一种随机算法来满足张三的需求。（10分）
    （2）请写代码实现自己的算法。（10分）
    设定：
    songs = [['A',3],['F',8],['G',9.5]]的格式存储
    首先随机从所有歌曲中等概率选取一首，然后取出其评分，换算成百分制，再随机在1-100之间取数，如果落在
    0-scores区间中，则播放，否则循环
    :return:
    '''

    while 1:
        i = random.randint(0,len(songs)-1)
        song_i_name = songs[i][0]
        song_i_score = songs[i][1]

        p_score = song_i_score * 10
        p = random.randint(0,100)
        if p <= p_score:
            return 'PLAY:'+song_i_name+'概率'+str(p_score/100)

print(selectSong(songs=[['A',3],['F',8],['G',9.5]]))