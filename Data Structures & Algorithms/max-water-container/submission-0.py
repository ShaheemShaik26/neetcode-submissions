class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        while left<right:
            width=right-left
            curr_height=min(height[left],height[right])
            curr_water=width*curr_height
            water=max(water,curr_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1 
        return water

            