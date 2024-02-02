h_list = [int(input()) for _ in range(9)]
fake_h_sum = sum(h_list) - 100

real_h_list = []
fake_h_list = []
for i in range(len(h_list)):
    fake_h = fake_h_sum - h_list[i]
    if fake_h != h_list[i] and fake_h in h_list and len(fake_h_list) < 2:
        fake_h_list.append(h_list[i])
        fake_h_list.append(fake_h)
    elif h_list[i] not in fake_h_list:
        real_h_list.append(h_list[i])

real_h_list.sort()

for h in real_h_list:
    print(h)