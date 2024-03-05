'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''
N = int(input())
wordList = []
for _ in range(N):
    wordList.append(str(input()))
wordList = sorted(set(wordList))
wordList.sort(key = lambda x : len(x))
for each in wordList:
    print(each)