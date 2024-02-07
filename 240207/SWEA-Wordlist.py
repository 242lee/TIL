T = int(input())
for testcase in range(1, T+1):
    wordList = input()
    result = []
    for word in wordList:
        for char in word:
            if len(result) == 0 or char != result[-1]:
                result.append(char)
            elif char == result[-1]:
                result.pop()

    print(f'#{testcase} {len(result)}')