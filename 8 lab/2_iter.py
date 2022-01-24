from itertools import permutations

def get_permutations(s, n):
    return sorted(list(map(''.join, permutations(s, n))))

print (get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"] )


    

