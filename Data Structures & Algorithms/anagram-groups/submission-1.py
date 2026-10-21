from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for s in strs:
            sort_map="".join(sorted(s))
            if sort_map not in hashmap:
                hashmap[sort_map]=[]
            hashmap[sort_map].append(s)
        return list(hashmap.values())