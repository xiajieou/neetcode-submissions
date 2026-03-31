class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        my_list = []
        for i in nums * 2 :
            my_list.append(i)
        return my_list