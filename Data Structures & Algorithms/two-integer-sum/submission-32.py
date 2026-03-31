class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previous = {} # val : idx

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in previous:
                return [previous[diff], i]
            previous[n] = i 