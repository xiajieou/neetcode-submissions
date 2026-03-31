class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)-1,-1, -1):
            
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i

            
            
            


