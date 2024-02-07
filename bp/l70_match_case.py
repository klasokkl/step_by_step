cmd = ('Anton', 'python', 2000.87 )
cmd = (1, 'Anton', 'python', 2000.87, 3023 )

match cmd:
   # case tuple() as book:
   #     print(f'кортеж {book}')
    #case str() as author, str() as title, float() | int() as price, *_ if len(cmd) < 6:
    #    print(f'{author}, {title}, {price}')
    case [author, title, price] | [ _, author, title, price, _]:
        print(f'книга 1 {price}, {title}, {price}')
    case _:
        print('непонятний формат')

