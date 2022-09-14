# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

fine = open('seminar_3/file.txt', 'w')

while True:
    s = input()
    if s == '':
        break
    fine.write(s+'\n')

fine.close()

fine = open('seminar_3/file.txt', 'r')
count = 0
# count1 = 1
for line in fine:
    count+=1
    print(f'количество символов в {line} строке равно: {len(line)}')
    print(f'количество слов в {line} строке равно {len(line.split())}')
    # if ' ' in line:
    #     count1 += 1
print(f'количество строк в файле:{count}')
# print(count1)
