A = input()

# Please write your code here.
def palindrome(sentence):
    B=""
    length = len(sentence)
    for i in range(length-1,-1,-1):
        B += sentence[i]
    return B

B = palindrome(A)

if A == B:
    print('Yes')
else:
    print('No')