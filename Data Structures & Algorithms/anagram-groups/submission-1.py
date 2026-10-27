class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord('a')] +=1

            str_key = tuple(count)
            anagram_map[str_key].append(str)

        return list(anagram_map.values())    
