def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while(indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += len(line)


try:
    with open('exampl.txt', encoding='utf-8') as file:
        a = find_word(file, "world")
        print(list(a))
except FileNotFoundError:
    print("файл не найден")
except:
    print('ошибка обработки файла')
