class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}

        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1

        for j in t:
            if j in t_hash:
                t_hash[j] += 1
            else:
                t_hash[j] = 1
        

        if s_hash != t_hash:
            return False
        
        return True
