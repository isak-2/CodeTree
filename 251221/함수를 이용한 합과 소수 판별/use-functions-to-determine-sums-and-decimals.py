a, b = map(int, input().split())

# Please write your code here.

def is_prime(number):
    number_ = number // 2 + 1
    for j in range(2,number_):
        if number % j == 0:
            return 0
    return 1 

def is_even(number2):
    str_n = str(number2)
    sum = 0
    for k in str_n:
        sum += int(k) % 10
    if sum % 2 == 0:
        return 1
    else:
        return 0 

        
cnt = 0
for i in range(a,b+1):
    if is_even(i) == 1 and is_prime(i) == 1:
        cnt += 1

print(cnt)