'''
모든 키의 합을 구해
그리고 100을 빼
남은 수가 가짜 2명 키의 합

list의 전체를 돌면서 합이 될 수 있는 조합을 찾아
'''

inputList = [20, 7, 23, 19, 10, 15, 25, 8, 13]
fakesum = sum(inputList) - 100 #가짜키의 합 
realheightList = []

for i in range(len(inputList)):
    fakeheight = fakesum - inputList[i]
    
    if fakeheight in inputList:
        fakeheightList = [inputList[i], fakeheight]
    else:
        realheightList.append(inputList[i])

realheightList.sort()
for realheight in realheightList:
    print(realheight)
