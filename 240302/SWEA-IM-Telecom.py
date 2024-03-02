'''
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX

3
XXX
XAX
XXX
'''
N = int(input())
Map = [list(input())for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 'A':
            pass
