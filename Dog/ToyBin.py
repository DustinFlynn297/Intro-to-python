from Toy import Toy

class ToyBin:
    def __init__(self) -> None:
        self.toys = []
        self.add_toys_to_bin()

    def add_toys_to_bin(self):
        toy1 = Toy('rope')
        toy2 = Toy('squeak')
        toy3 = Toy('ball')
        

        self.toys.append(toy1)
        self.toys.append(toy2)
        self.toys.append(toy3)


