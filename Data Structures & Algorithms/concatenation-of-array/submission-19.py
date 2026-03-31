class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2

        for i, num in enumerate(nums):
            ans[i] = num
            ans[len(nums) + i] = num
        return ans