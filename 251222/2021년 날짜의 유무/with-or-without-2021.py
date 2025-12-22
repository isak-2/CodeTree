M, D = map(int, input().split())

month = 12 
m_result = month - M 
if M in [1,3,5,7,8,10,12]: #31일까지 있는 달 
    day1 = 31
    result = day1 - D 
elif M in [4,6,9,11]: #30일까지 있는 달 
    day2 = 30
    result = day2 - D 
else:  #28일까지 있는 달 
    day3 = 28
    result = day3 - D     

# Please write your code here.
if result >= 0 and m_result >= 0:
    print('Yes')
else:
    print('No')

