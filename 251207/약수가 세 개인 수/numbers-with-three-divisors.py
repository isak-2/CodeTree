start, end = map(int, input().split())

# Please write your code here.
total_count = 0
for i in range(start,end+1,1):
    divisor_count = 0
    for j in range(1,i+1,1):
        if i % j == 0:
            divisor_count += 1
    if divisor_count == 3:
        total_count += 1
print(total_count)