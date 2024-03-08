#Батьківський клас
class Animal:

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

#Дочірній клас
class Dog(Animal):

    def bark(self):
        print("I can bark! Woof woof!!")

#Створюємо об'єкт класу Dog 
dog1 = Dog()

#Викликаємо методи батьківського класу
dog1.eat()
dog1.sleep()

#Викликаємо методи дочірнього класу
dog1.bark()
