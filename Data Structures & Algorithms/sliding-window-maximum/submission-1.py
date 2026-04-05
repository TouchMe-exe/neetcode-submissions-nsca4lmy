class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        output=[]
        l=r=0

        while r<len(nums):

            while q and q[-1][1]<nums[r]:
                q.pop()
            q.append([r,nums[r]])

            if l>q[0][0]:
                q.popleft()

            if r+1>=k:
                output.append(q[0][1])
                l+=1
            r+=1
        
        return output
            






            
        


            

