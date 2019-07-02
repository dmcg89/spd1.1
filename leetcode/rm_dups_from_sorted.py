class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i+1]:
                nums.pop(i)
        return len(nums)