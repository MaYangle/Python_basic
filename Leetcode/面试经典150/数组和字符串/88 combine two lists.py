# 合并两个有序数组
# 给两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
# 其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#

class solution:
    def  merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
        """
        #第一种思路 直接将nums2的值赋给nums1空出来的，然后排序
        nums1[m:] = nums2
        nums1.sort()

        #第二种思路，双指针
        # l,r 分别代表nums1，nums2对应的索引
        l,r,index = m-1,n-1,len(nums1)-1
        #哪一个大 哪一个先排进去
        while l>=0 and r>=0:
            if nums1[l]<=nums2[r]:
                nums1[index] = nums2[r]
                r -= 1
            else:
                nums1[index] = nums1[l]
                l -= 1
            index -= 1
        while r>=0:
            nums1[index] = nums2[r]
            r -= 1
            index -= 1
