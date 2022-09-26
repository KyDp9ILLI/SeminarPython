# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.


# inp = list(map(str, input().split()))
# ans = list()
# for i in inp:
#     if i.isdigit():
#         ans.append(i)
# print(f'Максимум в строке равен {max(ans)}, минимум в строке равен {min(ans)}')

import re #для сплита
s = str(input())
r = re.split(' ', s)
t = map(int, r)
k = map(int,r)
print(min(t))
print(max(k))