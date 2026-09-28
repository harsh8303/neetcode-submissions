class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        longest_length=0
        for x in nums_set:
            if x-1 not in nums_set:
                current=x
                length=1
                while current+1 in nums_set:
                   current+=1
                   length+=1
                longest_length=max(length,longest_length)
        return longest_length
