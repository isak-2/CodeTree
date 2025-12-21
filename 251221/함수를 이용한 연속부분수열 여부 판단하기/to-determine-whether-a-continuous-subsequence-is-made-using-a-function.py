n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def part_seq():
    #map의 새로운 사용법 
    str_a = map(str,a)
    str_aa = "".join(str_a)
    str_b = map(str,b)
    str_bb = "".join(str_b)
    # in연산자로 파이썬에서 부분수열 쉽게 풀기 
    if str_bb in str_aa:
        
        return True
    else:
        return False 





if part_seq():
    print('Yes')
else:
    print('No')