class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n=len(nums)
        # mp={}
        # for i in range(n):
        #     mp[i]=nums[i]
        # for i in range(n):
        #     new_target=target-nums[i]
        #     for key,value in mp.items():
        #         if value==new_target and key!=i:
        #           return [i,key]

        # return [-1,-1]
        n=len(nums)
        mp={}
        for i in range(n):
            need=target-nums[i]
            if(need in mp):
                return [mp[need],i]
            else:
                mp[nums[i]]=i
        return [-1,-1]