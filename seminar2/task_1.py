# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# a = '0000a0000n00t00000o000000n'

# if 'a' in a:
#     a = a[a.find('a'):]
#     if 'n' in a:
#         a = a[a.find('n'):]
#         if 't' in a:
#             a = a[a.find('t'):]
#             if 'o' in a:
#                 a = a[a.find('o'):]
#                 if 'n' in a:
#                     a = a[a.find('n'):]
# print(a)
print("Введите количество холодильников")
n = int(input())
list1 = []
print("Введите имена холодильников")
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)
print(*list1)
