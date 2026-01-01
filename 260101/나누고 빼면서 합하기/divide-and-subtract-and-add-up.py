n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
sum = 0
#1. m이 1보다 크거나 같은 동안 반복한다.
while(m >= 1):
    #1-1. m 위치의 a값을 sum에 더한다. 
    sum += A[m-1]
    #1-2. m이 짝수이면 2로 나눈다.
    if m % 2 == 0:
        m //= 2 
    #1-3. mdl 홀수이면 1을 뺀다. 
    else:
        m -= 1 

print(sum)