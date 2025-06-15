class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        s1=s.split()
        if len(pattern)!=len(s1):
            return False
        for i in range(0,len(pattern)):
            if pattern[i] not in d.keys() and s1[i] not in d.values():
                d[pattern[i]]=s1[i] 
            elif pattern[i] in d.keys():
                if d[pattern[i]] == s1[i]:
                  continue
                elif d[pattern[i]]!=s1[i]: 
                  return False 
            else:
                return False        
        return True

            
        