<<<<<<< HEAD
for tc in range(1, 11):
    N, fake = input().split()
    real = []

    for each in fake:
        if len(real) == 0 or each != real[-1]:
            real.append(each)
        elif each == real[-1]:
            real.pop()
=======
for tc in range(1, 11):
    N, fake = input().split()
    real = []

    for each in fake:
        if len(real) == 0 or each != real[-1]:
            real.append(each)
        elif each == real[-1]:
            real.pop()
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
    print(f'#{tc}', ''.join(real))