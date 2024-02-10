def palin(wordList):
    reversed = ''
    for i in wordList[::-1]:
        reversed += i
    
    if wordList == reversed:
        return 1
    else:
        return 0

T = int(input())
for testcase in range(1, T+1):
    target = input()    
    print(f'#{testcase} {palin(target)}')