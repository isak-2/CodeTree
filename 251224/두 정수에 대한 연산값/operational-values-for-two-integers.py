a, b = map(int, input().split())

# Please write your code here.
if a > b:
    big = a + 25
    small = b * 2
else:
    big = b + 25
    small = a * 2

print(small, big)

