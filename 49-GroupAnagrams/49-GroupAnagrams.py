# Last updated: 6/5/2025, 3:47:10 PM
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs :
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] +=1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())     