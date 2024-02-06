T = int(input())
for testcase in range(1, T+1):
    wordList = list(input())
    ListReverse = []

    for i in wordList[::-1]:
        ListReverse.append(i)
    
    a = ''.join(wordList)
    b = ''.join(ListReverse)

    if a == b:         
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')
