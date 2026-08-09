class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        n=len(nums)
        for i in range(n):
            mp[nums[i]]=mp.get(nums[i],0)+1
        
        for key,value in mp.items():
            if(value>1):
                return True
        return False
        