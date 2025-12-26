A = input()

# Please write your code here.


def judge(A):
    differ_bool = False
    for i in A:
        for j in A:
            if i != j:
                differ_bool = True
                return differ_bool
    return differ_bool


        
            
        




if judge(A):
    print('Yes')
else:
    print('No')