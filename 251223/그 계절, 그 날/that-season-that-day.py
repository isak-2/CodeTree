Y, M, D = map(int, input().split())

# Please write your code here.
def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False 
        else: 
            return True
    return False  


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
    if leap_year(Y):
        day3 += 1
    result = day3 - D    

if m_result >= 0 and result >= 0:
    if M in [3,4,5]:
        print('Spring')
    elif M in [6,7,8]:
        print('Summer')
    elif M in [9,10,11]:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)