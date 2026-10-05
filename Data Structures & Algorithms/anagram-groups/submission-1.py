class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for i in strs:
            word = list(i)
            word.sort()
            sorted_word = "".join(word)

            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = [i]
            else:
                anagram_map[sorted_word].append(i)
        
        return list(anagram_map.values())
