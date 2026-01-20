n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
for i in nums:
    print(i, end=' ')
print()

for i in nums[::-1]:
    print(i, end=' ')


