class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = 2 * nums
        n = len(nums)

        for i,num in enumerate(nums):
            ans[i] = num
            ans[i+ n] = num
        return ans