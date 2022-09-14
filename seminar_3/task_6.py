# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

spisok = ['строка1', 'строка2', 'строка3', 'строка1']
find_str = 'строка1'
if spisok.count(find_str) < 2:
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:
    spisok1 = spisok[spisok.index(find_str) + 1:]  # отрезаем первой вхождение
# ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали
    print(spisok1.index(find_str) + (len(spisok) - len(spisok1)))

b = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# count = 0
# for i in range(len(b)):
#     if b[0] == b[i]:
#         count += 1
#     if count == 2:
#     print(i+1)
#     break