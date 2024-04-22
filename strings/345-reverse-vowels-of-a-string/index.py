class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', "I", "O", "U", "a", "e", "i", "o", "u"]
        i = 0
        j = len(s) - 1
        r = list(s)
        while i < j:
            if r[i] in vowels:
                while i < j:
                    if r[j] in vowels:
                        r[i], r[j] = r[j], r[i]
                        j -= 1
                        break
                    else:
                        j -= 1
            i += 1
        return "".join(r)