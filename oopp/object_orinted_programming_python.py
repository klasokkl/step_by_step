class Cat:
    #атрибути дані класу
    name = ''
    age = 0

#створення об'єкта cat1
cat1 = Cat()
cat1.name = 'Blu'
cat1.age = 10

#створення іншого об'єкта - cat2
cat2 = Cat()
cat2.name = 'Woo'
cat2.age = 15

#Доступ до атрибутів класу Cat
print(f"{cat1.name} is {cat1.age}")
print(f"{cat2.name} is {cat2.age}")

