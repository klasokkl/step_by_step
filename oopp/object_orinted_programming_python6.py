class Addition:
    first = 0
    second = 0
    onswer = 0
    
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print(f"First number {self.first}")
        print(f"Second number {self.second}")
        print(f"Addition of two numbers = {self.onswer}")

    def calculate(self):
        self.onswer = self.first + self.second

obj = Addition(1000, 2000)
obj2 = Addition(10, 20)
obj.calculate()
obj2.calculate()
obj.display()
obj2.display()
