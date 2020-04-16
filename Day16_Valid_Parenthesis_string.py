class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        l_count = r_count = 0
        
        for i in range(n):
            l_count += 1 if s[i] in '(*' else - 1
            r_count += 1 if s[n-i-1] in ')*' else -1
            
            if l_count < 0 or r_count < 0:
                return False
            
        return True
