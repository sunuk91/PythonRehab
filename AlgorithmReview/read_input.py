import sys

# T = int(input()) #Test case
# a = int(sys.stdin.readline())
# print(a)

T = int(sys.stdin.readline())

# 1. 정해진 개수의 정수를 한줄에 입력 받을
index = []
for i in range(T):
        a,b = map(int, sys.stdin.readline().split(','))
        index.append([a,b])
print(index)

# 2. 임의의 개수의 정수를 한줄에 입력 받아 리스트에 저장할때
index2 = []
for i in range(T):
    index2.append(list(map(int,sys.stdin.readline().split(','))))

print(index2)

# 3. 문자열 n줄을 입력 받아 리스트에 저장할떄
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
print(data)