a = [1, 2, 3]
b = [1, 2]
c = [1, 2, 3, 4]
d = [a, b, c]
assert d[0][2] == 3
assert d[1][0] == 1
assert d[2][2] == 3