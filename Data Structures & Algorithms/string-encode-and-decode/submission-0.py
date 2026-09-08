class Solution:

    def encode(self, strs: List[str]) -> str:
        sa=""
        for s in strs:
            n=len(s)
            sa=sa+"#"+str(n)+"#"+s
        return sa

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0;
        while i<len(s):
            j=i+1
            while s[j]!='#':
                j+=1
            n=int(s[i+1:j])
            start=j+1
            word=s[start:start+n]
            ans.append(word)
            i=start+n
        return ans

