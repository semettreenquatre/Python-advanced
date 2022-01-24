from itertools import combinations

def get_combinations(s, n):
    output = []
    for i in range(1, n + 1):
        output += sorted(list(map(''.join, map(sorted, combinations(s, i)))))
    return output

print (get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"])

