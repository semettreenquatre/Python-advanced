from itertools import combinations_with_replacement

def get_combinations_with_r(s, n):
    return sorted(list(map(''.join, map(sorted, combinations_with_replacement(s, n)))))

print (get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"])

