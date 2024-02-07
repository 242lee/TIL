check = [
    'abc',
    'fgh',
    'klm'
    ]
N = int(input())
inputBoard = [input() for _ in range(N)]

for i in range(N-(3-1)):
    for j in range(N-(3-1)):
        for k  in range(3):
            if inputBoard[i+k][j:j+3] != check[k]:
                for l in range(3):
                    if inputBoard[i+k][j+l] != check[k][l]:
                        print(inputBoard[i+k][j+l], end = '')
                print()
