class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            s_map[c] = s_map.get(c,0)+1
        
        for c in t:
            t_map[c] = t_map.get(c,0)+1
        
        for key in s_map:
            if s_map[key] != t_map.get(key,0):
                return False
            
        return True
