
try:
    #file = open("my_file.txt", encoding="utf-8")
    with open("my_file.txt", encoding="utf-8") as f:
        s = f.readlines()
        print(s)
    #try:
    #    s = file.readlines()
    #    print(s)
    #finally:
    #    file.close()
except FileNotFoundError:
    print('файл не найден')
except:
    print("ощыбка при работе с файлом")
