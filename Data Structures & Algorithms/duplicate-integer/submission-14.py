class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()

        for num in nums:
            if num in count:
                return True
            count.add(num)
        return False