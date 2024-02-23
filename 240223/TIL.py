print(bin(10))
print(hex(10))

# print(int('1011', 2))
# print(int('b', 16))

KEY = 1004
def en_de(N):
    return N ^ KEY
print(en_de(1000))
print(en_de(4))

print(bin(0b1101 << 2))
#0b110100
print(bin(0b1101 >> 2))
#0b11

t = 1
for i in range(5):
    print(bin(t), t)
    t = t << 1
'''
0b1 1
0b10 2
0b100 4
0b1000 8
0b10000 16
'''

print(~4) # -5


# 도전과제 SWEA 10726 번
N, M = map(int, input().split())
print(bin(M))
cnt = 0
for i in range((len(bin(M))-N),len(bin(M))):
    if bin(M)[i] == '1':
        cnt += 1
if cnt == N:
    print('ON')
else:
    print('OFF')
#-----------------------------------
N, M = map(int, input().split())
def Test():
    target = M
    for i in range(N):
        if target & 0x1 == 0:
            return False
        target = target >> 1
    return True
print(Test())

# 근삿값
print(f'{0.1:.20f}')
# 0.10000000000000000555

# 연습 문제