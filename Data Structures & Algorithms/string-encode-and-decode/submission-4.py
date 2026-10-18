class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for word in strs:
            new_str += f"{len(word)}#{word}"
        return new_str
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
        # Find the '#'
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Get the word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to the next encoded word
            i = j + 1 + length

        return result
