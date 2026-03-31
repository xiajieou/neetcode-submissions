class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # input:  length n <= 1000 [1,2,3,4]
        # output: [1,2,3,4,1,2,3,4]
        ans = []
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans 