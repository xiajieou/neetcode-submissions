class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0 
        for i in nums:
            if count == 0:
                res = i
            count = count + (1 if i == res else -1)
        return res
