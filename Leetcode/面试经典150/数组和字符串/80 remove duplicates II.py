# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        # 假如一个例子 [1 1 1 3 4 5 5]
        #快慢指针先都在0位，然后都到1位
        #然后到2位的时候 nums[2] 和 nums[slow-2] 是相同的 slow就不动了 用这样的方法来确定几位是重复的
        for fast in range(len(nums)):
            if slow<2 or nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow