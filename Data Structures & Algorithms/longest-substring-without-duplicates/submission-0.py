class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        left=0
        max_sub=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            max_sub=max(max_sub,right-left+1)
        return max_sub