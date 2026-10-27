class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += f"{len(st)}#{st}"
        return s
    def decode(self, s: str) -> List[str]:
        op = []
        i = 0

        while i < len(s):
            n = s.find("#",i)
            l = int(s[i:n])

            op.append(s[n+1: n+1+l])
            i=n+1+l
        return op   

        

        
