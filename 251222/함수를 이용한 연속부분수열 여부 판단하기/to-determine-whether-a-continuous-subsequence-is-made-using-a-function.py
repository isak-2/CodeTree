n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# Please write your code here.
def part_seq():
    for i in range(n1-n2+1): #a리스트에서서 b리스트를 뺀 것에 1을 더하면 b를 한칸씩 옮겨 a와 비교한 회수가 됨
        flag = 0 # b리스트 길이만큼 flag가 채워지면 부분수열이 있음. 
        for j in range(n2):
            if a[i+j] == b[j]:
                flag += 1
        if flag == n2:
            return True
        
    return False


if part_seq():
    print('Yes')
else:
    print('No')