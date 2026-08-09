class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if(n!=m): return False
        mp={}
        

        for i in range(n):
            mp[s[i]]=mp.get(s[i],0)+1
        for j in range(m):
            if(t[j] in mp):
                mp[t[j]]=mp.get(t[j],0)-1
            else:
                return False
        for key,value in mp.items():
            if(value>0):
                return False
        return True
            
        
        