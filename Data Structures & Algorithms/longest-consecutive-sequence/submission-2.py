class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        count=0
        for num in numset:
            if num-1 not in numset:
                curr_num=num
                curr_st=1
                while(curr_num+1) in numset:
                    curr_num+=1
                    curr_st+=1
                count=max(count,curr_st)
        return count
            