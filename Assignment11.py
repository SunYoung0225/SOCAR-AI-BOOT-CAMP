f=open("C:/Users/82106/OneDrive/바탕 화면/py4e/regexsum.txt","r")

import re

lst = list()
for line in f:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    lst = lst + y

result = 0
for i in lst:
    value = int(i)
    result+=value
print(result)
