def isIsomorphic(s: str, t: str) -> bool:
    zip_set = set(zip(s,t))
    return len(zip_set) == len(set(s)) == len(set(t))

s = "paper"
t = "title"
print(isIsomorphic(s,t))
