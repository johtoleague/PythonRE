
def wordPattern( pattern: str, s: str) -> bool:
    words = s.split()
    words_to_patter_map = {}

    if len(pattern) != len(words):
        return False
    
    if len(set(pattern)) != len(set(words)):
        return False

    for i in range(len(words)):
        if words[i] not in words_to_patter_map:
            words_to_patter_map[words[i]] = pattern[i]
        elif words_to_patter_map[words[i]] != pattern[i]:
            return False
    return True

pattern = "aaaa"
s ="dog cat cat dog"
print(wordPattern(pattern,s))