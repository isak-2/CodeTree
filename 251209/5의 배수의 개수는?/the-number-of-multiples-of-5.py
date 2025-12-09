lst = [[int(x) for x in input().split()]
for _ in range(4)
]
fives_count = 0
for row in lst:
    for i in row:
        if i % 5 == 0:
            fives_count += 1

print(fives_count)
