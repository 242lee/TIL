num = 456789
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10
print(c)

i = 0
triplet = 0
run = 0

while i < 10:
    # triplet 데이터 조사 후 삭제
    if c[i] >= 3: 
        c[i] -= 3
        triplet += 1
        continue
    # run 데이터 조사 후 삭제
    if c[i] >= 1 and c[i+1]>=1 and c[i+2]>= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run+=1
        continue
    i+=1

if run + triplet ==2:
    print("BabyGin")
else:
    print("Lose")