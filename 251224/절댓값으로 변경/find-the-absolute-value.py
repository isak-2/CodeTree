n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
brr = []
for i in arr:
    brr.append(abs(i))

for j in brr:
    print(j, end=' ')