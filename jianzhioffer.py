#-*- coding:utf-8 -*-
'''
from collections import deque
def replaceblock(str):

    n = len(str)
    numsofblock = 0
    for i in range(n-1,0,-1):
        if str[i] == ' ':
            numsofblock+=1
    newlen = n+2*numsofblock

    newstr = deque()

    while newlen>0 and n>0:
        if str[n-1] == ' ':
            newstr.appendleft('02%')

        else:
            newstr.appendleft(str[n-1])
        n -= 1
    return ''.join(newstr)


nums = 'hello world'
print(replaceblock(nums))


'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def create_linked_list():
    '''创建一个9个节点的链表'''

    node = Node(9)
    for i in range(8, 0, -1):
        node = Node(i, node)
    return node


def delete_node(linked_list, node_to_delete):
    '''

    :param linked_list: 给定链表
    :param node_to_delete: 要删除的节点
    :return:
    分三种情况考虑
    1.空链表或者只有一个节点，直接返回或者删除，头结点置为None
    2.要删除的节点位于表尾，遍历一遍
    3.正常情况，用后一个节点覆盖掉当前节点

    '''
    #只有一个节点
    if linked_list.next ==None and linked_list == node_to_delete:
        return None
    head = linked_list
    if node_to_delete.next == None:#要删除的节点位于最后
        while True:
            if head.next == node_to_delete:
                head.next = None
                break
            head = head.next
    else:
        pnext = node_to_delete.next
        node_to_delete.data = pnext.data
        node_to_delete.next = pnext.next
    return linked_list

def finfMidNode(listNode):
    if listNode == None:
        return None
    phead = listNode
    plast = listNode

    while phead.next:
        phead = phead.next.next
        plast = plast.next

    return plast.data

def hasCircle(listNode):
    if listNode ==  None:
        return None
    phead = listNode
    plast = listNode
    while phead.next:
        phead = phead.next.next
        plast = plast.next
        if phead == plast:
            return True
    return False
def finfLoopPort(listNode):
    '''

    :param listNode:
    :return: 环入口
    '''
    if listNode == None or listNode.next == None:
        return None
    phead = listNode
    plast = listNode
    while phead.next:
        phead = phead.next.next
        plast = plast.next
        if phead == plast:
            break
    if phead != plast:
        return None
    phead2 = listNode
    while phead2 != plast:
        phead2 = phead2.next
        plast = plast.next
    return phead2

def isIntersect(listNode1,listNode2):
    '''

    :param listNode1:
    :param listNode2:
    :return:
    '''
    if listNode1 == None or listNode2 == None:
        return None
    phead1 = listNode1
    phead2 = listNode2
    while phead1.next:
        phead1 = phead1.next
    while phead2.next:
        phead2 = phead2.next

    if phead1==phead2:
        return True
    return False

def reverseList(listNode):
     if listNode == None or listNode.next == None:
         return listNode

     phead = listNode


     while phead:
         pnext = phead.next
         if pnext == None:
             prever = phead
         phead.next = pPrev
         pPrev = phead
         phead = pnext
     return prever


def mergeNode(listNode1,listNode2):
    '''

    :param listNode1:
    :param listNode2:
    :return: 合并顺序链表
    '''
    if listNode1 == None:
        return listNode2
    if listNode2 == None:
        return listNode1
    if listNode1.data < listNode2.data:
        phead = listNode1
        phead.next = mergeNode(listNode1.next,listNode2)
    else:
        phead = listNode2
        phead.next = mergeNode(listNode1,listNode2.next)
    return phead

def reorderOddEven(nums):
    '''
    奇数放在偶数前面
    :param nums:
    :return:
    '''
    if nums == None:
        return None
    phead = 0
    plast = len(nums)-1

    while phead < plast:
        while phead< plast and nums[phead]%2 !=0:
            phead+=1
        while phead < plast and nums[plast]%2 == 0:
            plast -= 1

        if phead<plast:
            nums[phead],nums[plast] = nums[plast],nums[phead]
    return nums

def reversNode(listNode):
    '''
    非递归形式实现链表反转
    :param listNode:
    :return:
    '''
    if listNode == None or listNode.next == None:
        return listNode
    phead = listNode
    ppre = None
    pnext = None
    while phead:
        pnext = phead.next
        phead.next = ppre
        ppre = phead
        phead = pnext
    return ppre

def reversNode_s(listNode):
    '''
    递归形式实现；链表反转
    :param listNode:
    :return:
    '''
    if listNode == None or listNode.next == None:
        return listNode
    phead = reversNode_s(listNode.next)
    listNode.next.next = listNode
    listNode.next = None#
    return phead



def print_linked_list(head):
    while head is not None:
        print head.data, ' ',
        head = head.next
    print ''


if __name__ == '__main__':
    linked_list_1 = create_linked_list()
    print 'original list 1:'

    print_linked_list(linked_list_1)

    pp = finfMidNode(linked_list_1)#delete_node(linked_list_1, linked_list_1.next.next)
    print 'current list 1:',pp

    hascir = hasCircle(linked_list_1)
    print 'hascir:',hascir
    nums = [1, 2, 4, 7, 9, 5, 6]

    print reorderOddEven(nums)
    #print_linked_list(pp)
'''
    print 'delete head of list 1:'
    linked_list_1 = delete_node(linked_list_1, linked_list_1)
    print 'current list 1:'
    print_linked_list(linked_list_1)
    print 'delete tail of list 1:'
    linked_list_1 = delete_node(linked_list_1, linked_list_1.next.next.next.next.next.next)
    print 'current list 1:'
    print_linked_list(linked_list_1)

    linked_list_2 = Node(10)
    print 'original list 2:'
    print_linked_list(linked_list_2)
    linked_list_2 = delete_node(linked_list_2, linked_list_2)
    print 'current list 2:'
    print_linked_list(linked_list_2)

'''


