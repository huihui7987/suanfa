#-*- coding:utf-8 -*-
def bubble_sort(nums):
    flag = True
    passnum = len(nums) - 1

    while passnum > 0 and flag:
        flag = False
        for i in range(passnum):
            if nums[i] > nums[i+1]:
                flag = True
                nums[i],nums[i+1] = nums[i+1],nums[i]
        passnum -= 1


def select_sort(nums):
    for i in range(0,len(nums)):
        min = i
        for j in range(i+1,len(nums)):
            if nums[min] > nums[j]:
                min = j

        nums[min],nums[i] = nums[i],nums[min]
    return nums

#不好理解
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        # temp = a_list[fill_slot]
        # a_list[fill_slot] = a_list[pos_of_max]
        # a_list[pos_of_max] = temp
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

###############################
#####      插入排序        #####
###############################
def insert_sort(nums):

    for index in range(1,len(nums)):
        pos = index
        current_value = nums[index]
        while pos >0 and nums[pos-1]>current_value:
            nums[pos] = nums[pos-1]
            pos = pos - 1
        nums[pos] = current_value
    return nums
def insert_sort_py(nums):
    n = len(nums)
    if n == 1:
        return nums

    for i in range(1,n):
        for j in range(i,0,-1 ):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
    return nums

def binsert_sort(nums):
    '''
    折半插入排序
    :param nums:
    :return:
    '''
    n = len(nums)
    for i in range(1,n):
        tmp = nums[i]
        j = i

        low = 0
        high = i-1

        while low <= high:
            mid = round((low+high)/2)#此处注意必须取整数，可以使用round or //2
            if nums[mid] > tmp:
                high = mid - 1
            else:
                low = mid + 1

        #统一后移元素，插入空位置
        while j>low:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = tmp
    return nums


def shell_sort(nums):
    '''
    shell sort,借鉴直接插入排序在基本正序时候以及较短时候执行效率高的优点，
    将nums分为几段，每段进行插入排序，最后整体一次插入排序
    时间复杂度：N^1.3~N^1.5
    :param nums:
    :return:
    '''
    n = len(nums)
    gap = round(n/2)
    while gap:
        for i in range(gap,n):
            tmp = nums[i]
            j = i
            while j>=gap and nums[j-gap]>tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp
        gap = round(gap/2)
        print (nums)
    return nums


#import random
#nums=random.sample(range(1,100),50)
#print(insert_sort_py(nums=random.sample(range(1,100),50)))
#print(shell_sort(nums))
#print(binsert_sort(nums))



def loopword(nums):
    tmp = []
    T = 5
    counters = 0


    for word in nums:
        for chr in range(len(word)):
            ll = word[chr:]+word[:chr]
            if ll in nums and ll is not word:
                nums.remove(ll)


    return len(nums)



'''

if __name__ == '__main__':
    nums = [3,1,5,8,9,2,5,7,4]
    #bubble_sort(nums)
    #select_sort(nums)
    #selection_sort(nums)
    #insert_sort(nums)
    T = int(input())
    words = []
    for i in range(T):
        words.append(input())
    #words = ['picture','turepic','icturep','word','ordw']
    oop = loopword(words)
    print(oop)

'''
def shell_so(listN):
    n = len(listN)
    gap = 4#round(n/2)
    while gap>0:
        for i in range(gap,n):
            tmp = listN[i]
            j=i
            while j>=gap and listN[j-gap]>tmp:
                listN[j] = listN[j-gap]
                j-=gap
            listN[j]=tmp
        gap = round(gap/2)
        print(listN)
    return listN


def insert_sort_new(nums):
    n = len(nums)
    for i in range(1,n):
        for j in range(i,0,-1):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
        print(nums)
    return nums
import random

def bubble_sort_new(nums):
    n = len(nums)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if nums[j+1]<nums[j]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
    return nums


nums=[8,9,10,4,5,6,20,1,2]#random.sample(range(1,50),20)
#print(nums)
#shell_so(nums)
#bubble_sort_new(nums)
# -*- coding: utf-8 -*-
"""通过数组交换的快速排序"""
import random


def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)



def partition(arr, left, right):
    """找到基准位置, 并返回"""
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    # 将基准值移动到正确的位置
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    return pivot_index

'''
if __name__ == '__main__':
    arr = []
    for i in range(10):
         arr.append(random.randint(1, 100))
    #print (arr)
    quicksort(arr, 0, len(arr)-1)
    #print (arr)
'''


def get_partition(arr,low,high):
    pivot_index = low
    pivot = arr[low]

    for i in range(low+1,high+1):
        if arr[i]<pivot:
            pivot_index += 1
            if pivot_index != i:
                arr[i],arr[pivot_index] = arr[pivot_index],arr[i]

    arr[pivot_index],arr[low] = arr[low],arr[pivot_index]
    return pivot_index
def quicksort_self(arr,low,high):
    if low<high:
        pivot_index = get_partition(arr,low,high)
        quicksort_self(arr,low,pivot_index-1)
        #print(arr)
        quicksort_self(arr,pivot_index+1,high)
        print(arr)

arr = [5,6,12,2]
#quicksort_self(arr,low=0,high=len(arr)-1)
#print(arr)

def get_partindex(arr,low,high):
    '''
    严蔚敏版
    :param arr:
    :param low:
    :param high:
    :return:
    '''
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        if low < high:
            arr[low] = arr[high]
        while low < high and arr[low] < key:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = key
    return low

def quick_sort_yan(arr,low,high):
    '''
    严蔚敏版
    :param arr:
    :param low:
    :param high:
    :return:
    '''
    if low < high:
        key_index = get_partindex(arr,low,high)
        quick_sort_yan(arr,0,key_index-1)
        quick_sort_yan(arr,key_index+1,high)


# !/usr/bin/envpython
# -*-coding:utf-8-*-

def heap_sort(lst):
    #调整序列的前半部分元素，调整完之后第一个元素是序列的最大的元素

    #创建最大堆
    for start in range((len(lst) - 2) / 2, -1, -1):
        sift_down(lst, start, len(lst) - 1)

    #//从最后一个元素开始对序列进行调整，不断的缩小调整的范围直到第一个元素

    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(lst, 0, end - 1)
    return lst


def sift_down(lst, start, end):
    root = start


    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break



l = [9, 2, 1, 7, 6, 8, 5, 3, 4]


print heap_sort(l)
