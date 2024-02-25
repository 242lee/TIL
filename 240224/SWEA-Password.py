for tc in range(1, 11):
    N, fake = input().split()
    real = []

    for each in fake:
        if len(real) == 0 or each != real[-1]:
            real.append(each)
        elif each == real[-1]:
            real.pop()
    print(f'#{tc}', ''.join(real))