import sys
input = sys.stdin.readline

n = int(input())
number = []

for i in range(n):
    num = int(input())
    number.append(num)

number.sort()

for j in number:
    print(j)