     def backspaceCompare(self, S: str, T: str) -> bool:
        s = ""
        t = ""
        
        for c in S:
            if c == "#":
                s = s[:-1]
            else:
                s += c
        
        for c in T:
            if c == "#":
                t = t[:-1]
            else:
                t += c
        
        return s == t
