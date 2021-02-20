lst = [1, 2]
other = lst
other = other.copy()
other[1] = 0
print(other, lst, sep="\n")