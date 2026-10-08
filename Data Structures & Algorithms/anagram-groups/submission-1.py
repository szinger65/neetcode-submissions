class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-97] += 1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())
