T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
 
    set_str1 = set(str1)
    dict_chr_cnt = {}
    result = ''
    for set_c in set_str1:
        for c in str2:
            if set_c == c:
                if c in dict_chr_cnt:
                    dict_chr_cnt[c] += 1
                else:
                    dict_chr_cnt[c] = 1
 
    max_v = 0
 
    for cnt in dict_chr_cnt.values():
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')