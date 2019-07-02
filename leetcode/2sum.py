class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        hash_table = {}
        
        for i in range(len(nums) - 1):
            sum_minus_elem = target - nums[i]
            if hash_table