import pickle

books = [ 
         ('книга 1', 200),
         ('book 2', 300),
         ('book 3', 500)]

file = open('out.bin', 'rb')
#pickle.dump(books, file)
bs = pickle.load(file)
print(bs)
file.close()

