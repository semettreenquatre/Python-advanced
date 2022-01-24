from itertools import starmap

def maximize(lists, m):
    return (sum(starmap(pow, [(el, 2) for el in map(max, lists)]))) % m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print (maximize(lists, m=1000))

