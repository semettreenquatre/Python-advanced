from itertools import groupby

def compress_string(s):
    output = []
    for symbol, count in groupby(s):
        output.append((len(list(count)), int(symbol)))
    return output

print(compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)])

