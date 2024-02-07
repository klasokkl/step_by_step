cmd = 'right'
cmd = 111

match cmd:
    case 'top':
        print('вверх')
    case 'left':
        print('влево')
    case  'right':
        print('вправо')
    case 'sok' | 'ldd' | 'rcc':
        print('any')
    #case _:
        print('другое')
    case command:
        print(f'команда {command}')

#print('проверки завершини')

match cmd:
    case str() as command:
        print(f'строковая команда: {command}')
    case int() as command if 0 <= command <= 9:
        print('целочисленний тип')
