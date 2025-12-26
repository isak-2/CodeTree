text = input()
pattern = input()

def confrim():
    iter = len(text) - len(pattern) + 1
    for ti in range(iter):
        flag_cnt = 0
        for pi in range(len(pattern)):
            if text[ti+pi] == pattern[pi]:
                flag_cnt += 1
        if flag_cnt == len(pattern):
            return ti
    return -1
    
    
print(confrim())


