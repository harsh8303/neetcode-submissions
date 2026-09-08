class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        pq=[]
        for element, frequency in freq.items():
            heapq.heappush(pq,(-frequency,element))
        arr=[]
        cnt=0
        while pq and cnt!=k: 
            frequency,element=heapq.heappop(pq)
            arr.append(element)
            cnt=cnt+1
        return arr
