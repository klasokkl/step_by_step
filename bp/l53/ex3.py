import pickle

book1 = ['name book1', 100]
book2 = ['name book2', 200]
book3 = ['name book3', 300]
book4 = ['name book4', 400]

try:
    with open('out.bin', 'rb') as file:
        #pickle.dump(book1, file)
        #pickle.dump(book2, file)
        #pickle.dump(book3, file)
        #pickle.dump(book4, file)

        bs1 = pickle.load(file)
        bs2 = pickle.load(file)
        bs3 = pickle.load(file)
        bs4 = pickle.load(file)
except:
    print('ошибка файла')

print(bs1, bs2, bs3, bs4, sep='\n')
