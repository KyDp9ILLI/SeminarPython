# НОД двух чисел

# НОД1
# def NOD(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return NOD(b, a % b)


# a = int(input())
# b = int(input())
# print(NOD(a, b))

#НОД2
# a=20
# b=58

# if a < b :
#     a, b = b, a

# while b!=0:
#     a, b = b, a % b

# print(a)

#НОД3

while a != b:
if a > b:
a -= b
else:
b -= a

print(a)