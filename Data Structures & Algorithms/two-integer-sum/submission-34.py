class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # list of nums  target : int 
        # return indices i and j but they cant be the same 
        # guranteed theres going to be a solution 
        # return the smaller index first

        visited = {} 

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in visited:
                return [visited[diff], i]
            visited[n] = i
        