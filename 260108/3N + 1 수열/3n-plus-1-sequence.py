N = int(input())

cnt = 0

while True:
    if N == 1:
        break
    if N % 2 == 0: 
        N /= 2
    else:
        N *= 3
        N += 1
    
    cnt += 1
    
   

print(cnt)