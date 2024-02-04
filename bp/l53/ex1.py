try:
    with open('out.txt', 'a') as file:
        file.seek(0)
        file.write('hello\n ')
except:
    print('Ошибка при работе с файлом')

