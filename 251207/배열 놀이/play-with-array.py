N,Q = map(int, input().split()) #N개의 원소와 Q개의 질의 입력
N_lst = list(map(int, input().split())) # N개의 원소 리스트 입력 
q_lst = [[int(i) for i in input().split()] # Q개의 질의를 2차원 리스트로 입력 
    for _ in range(Q)
]

def search_b(x): # 2번 질의 함수 
    for i in range(N):
        if N_lst[i] == x: 
            break # index가 제일 작은 원소를 찾기 위해 앞에서부터 찾음
    return i+1 

'''
(n 번째는 인덱스에선 n-1 )
1 번째는 인덱스 0
2 번째는 인덱스 1 
'''

for q_st in q_lst: #질의 리스트의 원소인 각 질의를 순회 
   if q_st[0] == 1: # 1번 질의를 받을 경우 
        print(N_lst[q_st[1]-1]) # a번째 원소를 출력합니다. (n번째는 인덱스에선 n-1 )
   elif q_st[0] == 2: # 2번 질의를 받을 경우 
        if q_st[1] in N_lst: # 원소가 리스트에 있다면 
            print(search_b(q_st[1])) # 몇 번째 원소인지 찾기 
        else:
            print(0) # 원소가 없다면 0을 출력합니다. 
   elif q_st[0] == 3: # 3번 질의를 받을 경우
        s = q_st[1] - 1 #(n번째는 인덱스에선 n-1 )
        e = q_st[2] #(n번째는 인덱스에선 n-1 )
        for n_st in N_lst[s:e]:
            print(n_st, end=' ') #s부터 e번 원소까지 출력 
        print( )
        