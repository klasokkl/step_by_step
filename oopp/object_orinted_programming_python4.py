class Polygon:
    #Метод рендерингу полігону
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    #Метод рендерингу квадрата
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    #Метод рендерингу кола
    def render(self):
        print("Rendering Circle...")


#Створюємо об'єкт класу Square
s1 = Square()
s1.render()

#Створюємо об'єкт класу Circle
c1 = Circle()
c1.render()

