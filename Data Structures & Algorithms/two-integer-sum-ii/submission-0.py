class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(numbers):
            diff = target - n 
            if diff in visited:
                return [visited[diff] + 1, i + 1]
            visited[n] = i