orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find(orbits):
    new = []
    for i, j in orbits:
        if i == j:
            new.append(0)
        else:
            new.append((3.14*i*j))
    maxx = 0
    maxx_ind = 0
    for i in range(len(new)):
        if new[i] > maxx:
            maxx_ind = i
            maxx = new[i]
    return orbits[maxx_ind]


print(find(orbits))