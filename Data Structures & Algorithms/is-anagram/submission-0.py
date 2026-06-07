class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            charset1 = {}
            charset2 = {}
            for char in s:
                charset1[char] = charset1.get(char, 0)+1
            
            for char in t:
                charset2[char] = charset2.get(char, 0)+1
            
            return charset1 == charset2
        