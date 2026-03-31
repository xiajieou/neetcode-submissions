class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
            count = count + (1 if res == nums[i] else -1)
        return res