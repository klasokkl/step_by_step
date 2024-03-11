class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized construcrot called with name", self.name)

    def method(self):
        if hasattr(self, "name"):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")

#Создаем объект класса с помощью конструктора по умолчанию
obj1 = MyClass()

#Вызываем метод класса через объект obj1
obj1.method()

#Создаем объект класса с помощью параметризованного конструктора
obj2 = MyClass("John")

#Вызываем метод класса через объект obj2
obj2.method()

