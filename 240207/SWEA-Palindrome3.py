for testcase in range(1,11):
    N = int(input())
    wordList = [input() for _ in range(8)]
 
    cnt =0
    for i in range(8):
        for j in range(8-N+1):
            result = wordList[i][j:j+N]
            if result == result[::-1]:
                cnt += 1

    for j in range(8):  # Iterate over columns
        for i in range(8-N+1):  # Iterate over rows with enough space for substring
            result = ''.join(wordList[i+k][j] for k in range(N))  # Extract substring vertically
            if result == result[::-1]:  # Check if substring is a palindrome
                cnt += 1
    print(f'#{testcase} {cnt}')

    print(f'#{testcase} {cnt}')