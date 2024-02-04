#1, 방향키를 선언한다.
dc = [1,0,-1,0]
dr = [0,1,0,-1]

#2. N * N 배열판을 만든다
N = int(input())
Snail = [[0]* N for _ in range(N)]
#3. r,c 그리고 direction 초기값을 설정한다.
r, c = 0, 0
direction = 0

#4. n번째 자리에 n으로 채우는 배열을 만든다
for n in range(1, N*N+1):
    Snail[r][c] = n
    r += dr[direction]
    c += dc[direction]

 #5. 배열판을 벗어났거나, 이미 값이 채워진 경우를 생각한다.
    if r < 0 or N <= r or c < 0 or N <= c or Snail[r][c] != 0:
        #그렇다면 뒤로 한 발 물러나기
        r -= dr[direction]
        c -= dc[direction]
        direction = (direction+1) % 4

        #6. 다시 채우기
        r += dr[direction]
        c += dc[direction]

for row in Snail:
    print(*row)
