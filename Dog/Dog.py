from Collar import Collar
from ToyBin import ToyBin
from Collar import Collar

class Dog:
    def __init__(self, breed) -> None:
        self.breed = breed
        self.toys = ToyBin()
        self.collar = [Collar('red'), Collar('blue'), Collar('pink')]
        self.slobber = False

    def pant(self):
        pass

    def eat(self, string):
        pass

    def show_toys(self):
        #display all of the toys in our ToyBin
        for toy in self.toys.toys:
            print(f"{toy.type}")

    def play(self, dog):
        pass