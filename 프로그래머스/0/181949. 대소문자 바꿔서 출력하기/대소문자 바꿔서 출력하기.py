import sys

string = sys.stdin.readline()
list(string)
str = []

for i in string:
    if i == i.upper():
        i = i.lower()
        str.append(i)
    elif i == i.lower():
        i = i.upper()
        str.append(i)
        
for j in str:
    print(j, end="")
        
        