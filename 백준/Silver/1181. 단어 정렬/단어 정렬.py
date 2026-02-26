n = int(input())
string = []

for i in range(n):
    s = input()
    string.append(s)

a_list = list(set(string))
a_list.sort(key=lambda x: (len(x), x))

for j in a_list:
    print(j)