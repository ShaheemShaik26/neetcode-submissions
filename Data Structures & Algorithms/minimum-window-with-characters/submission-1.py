from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        t_freq=Counter(t)
        req=len(t_freq)
        window={}
        match=0
        ans=(float('inf'),None,None)
        left=0
        for right in range(len(s)):
            char=s[right]
            window[s[right]]=window.get(s[right],0)+1
            if char in t_freq and window[char]==t_freq[char]:
                match+=1
            while left<=right and match==req:
                char=s[left]
                if right-left+1<ans[0]:
                    ans=(right-left+1,left,right)
                window[char]-=1
                if char in t_freq and window[char]<t_freq[char]:
                    match-=1
                left+=1
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

            