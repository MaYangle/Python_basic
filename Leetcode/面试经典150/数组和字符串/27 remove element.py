# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Solution 1
        a = 0
        # 直接遍历 把不相同的拿出来放到新的数组中
        for i in range(len(nums)):
            if val != nums[i]:
                nums[j] = nums[i]
                a+=1
        return a

        # Solution 2
        # 也可以用 try except
        while 1:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)