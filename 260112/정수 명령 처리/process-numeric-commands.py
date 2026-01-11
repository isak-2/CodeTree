N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.


# 클래스 정의
class Stack:
    def __init__(self):
        self.items = []
    
    # 1. push: 스택에 값을 추가
    def push(self, item):
        self.items.append(item)
    
    # 2. pop: 가장 위의 값을 제거하고 출력 (비어있으면 문제 조건에 맞게 처리)
    def pop(self):
        if self.empty() == 1:
            return -1 # 보통 스택이 비어있을 때 pop을 하면 -1을 반환하도록 설계됩니다.
        return self.items.pop()

    # 3. size: 스택의 요소 개수 반환
    def size(self):
        return len(self.items)
    
    # 4. empty: 비어있으면 1, 아니면 0 반환
    def empty(self):
        return 1 if not self.items else 0

    # 5. top: 가장 위의 값을 반환 (제거하지 않음)
    def top(self):
        if self.empty() == 1:
            return -1
        return self.items[-1]


s = Stack()
for i in range(N):
    cmd = command[i]
    
    if cmd == "push":
        s.push(value[i])
    elif cmd == "pop":
        print(s.pop())
    elif cmd == "size":
        print(s.size())
    elif cmd == "empty":
        print(s.empty())
    elif cmd == "top":
        print(s.top())