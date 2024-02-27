def perm(i, energysum):
    global min_energy
    if min_energy <= energysum:
        return
    if i == N:
        energysum += e[P[i-1]][P[i]]
        if min_energy > energysum:
            min_energy = energysum
        return
    for j in range(i, N):
        P[i], P[j] = P[j], P[i]
        perm(i+1, energysum + e[P[i-1]][P[i]])
        P[i], P[j] = P[j], P[i]

N = int(input())
e = [list(map(int, input().split())) for _ in range(N)]
P = list(range(N)) + [0]
print(P)
min_energy = 50 ** 3
perm(1,0)
print(min_energy)