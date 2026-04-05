class Solution:
    def trap(self, h: List[int]) -> int:
        leftmax=[0]*len(h)
        rightmax=[0]*len(h)

        n=len(h)-1
        leftmax[0]=h[0]
        for i in range (1,len(h)):
            leftmax[i]=max(leftmax[i-1],h[i])

        rightmax[n]=h[n]
        for i in range(n-1,-1,-1):
            rightmax[i]=max(rightmax[i+1],h[i])
        
        trap=0
        for i in range (len(h)):
            trap+=min(leftmax[i],rightmax[i])-h[i]

        return trap
            
        
            
        


         




            
                
