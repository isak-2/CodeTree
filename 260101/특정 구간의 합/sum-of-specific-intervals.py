n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

'''
1. m 만큼 반복한다. 
    1-1. 총합을 초기화 한다. 
    1-2. queries의 a1값을 인덱스로 하는 arr값부터 a2값을 인덱스로 하는 arr합까지 총합을 구한다.
    1-3. 총합을 출력한다. 
    1-4. m이 1 감소한다. 
'''

for i in range(m):
    sum = 0
    for j in range(queries[i][0], queries[i][1]+1):
        sum += arr[j-1] 
    print(sum)
