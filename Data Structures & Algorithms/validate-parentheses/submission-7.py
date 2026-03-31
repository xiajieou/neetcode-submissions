class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        final_array = []

        for i in s:
            if i in closeToOpen:
                if final_array and final_array[-1] == closeToOpen[i]:
                    final_array.pop()
                else:
                    return False

            else:
                final_array.append(i)
        return True if not final_array else False