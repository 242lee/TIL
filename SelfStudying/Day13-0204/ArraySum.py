arr = [[1,3,6,7,3], [7,3,1,2,5], [3,5,7,2,3], [4,6,7,2,2], [8,7,6,5,1]]

# -> 합
for i in range(5):
    sum = 0
    for down in range(5):
        sum += arr[i][down]
    print(sum)
print()
#아래로 합
for i in range(5):
    sum = 0
    for side in range(5):
        sum += arr[side][i]
    print(sum)
print()
sum = 0
for down in range(5):
    for side in range(5):
        if side == down:
            sum += arr[side][down]
print(sum)
sum = 0
for down in range(5):
    for side in range(5):
        if side + down == 5-1:
            sum += arr[side][down]
print(sum)