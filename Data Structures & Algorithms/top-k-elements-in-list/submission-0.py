class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map={}
        for num in nums:
            Map[num]=1+Map.get(num,0)
        
        arr=[]
        
        for num, cnt in Map.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
            
        return res
        

            