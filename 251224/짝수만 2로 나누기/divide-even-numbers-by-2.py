n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def divide_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

divide_even(arr)

for j in arr:
    print(j, end=' ')
