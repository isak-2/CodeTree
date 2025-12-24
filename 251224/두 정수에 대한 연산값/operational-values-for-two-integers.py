a, b = map(int, input().split())

# Please write your code here.
def swap(a,b):
    if a > b:
        big = a + 25
        small = b * 2
    else:
        big = b + 25
        small = a * 2
    return small, big

small, big = swap(a,b)
print(small, big)

