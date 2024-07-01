class Dog:
    name = None
    bread = None

    def __init__(self, name, bread):
        self.name = name
        self.bread =  bread


chow = Dog(name="Chow", bread= "begal")
print(chow.bread)