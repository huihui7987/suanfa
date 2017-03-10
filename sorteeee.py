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

def insert_sort(nums):

    for index in range(1,len(nums)):
        pos = index
        current_value = nums[index]
        while pos >0 and nums[pos-1]>current_value:
            nums[pos] = nums[pos-1]
            pos = pos - 1
        nums[pos] = current_value


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


