class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}

        for i in range(len(s)):
            s_set[s[i]] = s_set.get(s[i],0)+1
        
        for j in range(len(t)):
            t_set[t[j]] = t_set.get(t[j],0)+1

        if s_set == t_set and len(s_set) == len(t_set):
            return True
        else:
            return False 


  