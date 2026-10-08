class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # 1. find '#'
            while s[j] != '#':
                j += 1

            # 2. extract length
            length = int(s[i:j])

            # 3. extract string
            word = s[j+1 : j+1+length]
            res.append(word)

            # 4. move pointer
            i = j + 1 + length

        return res
            
