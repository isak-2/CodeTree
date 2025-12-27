sum_age = 0
cnt = 0
while True:
    age = int(input())
    if age >= 30 or age <= 19:
        break
    sum_age += age
    cnt += 1


if sum_age != 0:
    print(f'{sum_age/cnt:.2f}')
else:
    print('-nan')