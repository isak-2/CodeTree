a, b = map(int, input().split())

# Please write your code here.


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



cnt = 0
for num in range(a,b+1):
    if is_prime(num):
        cnt += num

print(cnt)