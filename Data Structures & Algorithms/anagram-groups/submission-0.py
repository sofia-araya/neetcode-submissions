class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for str in strs:
            sorted_key = "".join(sorted(str))
            anagram_map[sorted_key].append(str)
    
        return list(anagram_map.values())
