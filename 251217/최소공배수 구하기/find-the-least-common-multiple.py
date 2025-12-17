n, m = map(int, input().split())


# 최소 공배수를 구하고 
for i in range(1, min(m,n)+1):
    if m % i == 0 and n % i == 0:
        gcd = i 

# 점화식을 쓴다. 
lcm = (m * n) // gcd 

print(lcm)