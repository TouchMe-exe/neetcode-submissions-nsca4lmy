class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        arr=[0]*n
        for i in range (n):
            arr[(i+k)%n]=nums[i]

        nums[:]=arr
        

