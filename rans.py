class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        for letter in ransomNote:
            if letter not in magazine or ransomNote.count(letter) > magazine.count(letter):
                return False
        return True