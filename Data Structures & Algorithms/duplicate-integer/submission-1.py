class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            seen[num] = 1+seen.get(num,0)

        duplicate=[]
        for num,count in seen.items():
            if count > 1:
                duplicate.append(num)
        
        print(duplicate)
        if duplicate:
            return True
        else:
            return False

            


