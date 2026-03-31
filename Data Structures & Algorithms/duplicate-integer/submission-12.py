class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            count = {}
            for i in nums:
                if i not in count:
                    count[i] = 0
                count[i] += 1 
            
            for i in count.values():
                if i > 1:
                    return True 
            return False