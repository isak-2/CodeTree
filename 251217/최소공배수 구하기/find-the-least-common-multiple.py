n, m = map(int, input().split())

# Please write your code here.
m,n  = max(m,n), min(m,n)
if m % n == 0:
    lcm = m 
else: 
    for i in range(1,n+1):
        if m % i == 0 and n % i == 0:
            gcd = i

    
    for i in range(1,m):
        if m == gcd * i:
            lcm_s1 = i 
        if n == gcd * i:
            lcm_s2 = i
    lcm = gcd * lcm_s1 * lcm_s2 

print(lcm)