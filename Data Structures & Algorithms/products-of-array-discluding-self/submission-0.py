class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        mul=1
        for i in range(n):
            output[i]=mul
            mul*=nums[i]
        mul1=1
        for i in range(n-1,-1,-1):
            output[i]*=mul1
            mul1*=nums[i]
        return output
            