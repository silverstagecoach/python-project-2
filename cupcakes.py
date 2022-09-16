from abc import ABC, abstractmethod
from pprint import pprint
import csv



class Cupcake(ABC):
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)
        
class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = None
        self.sprinkles = []

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Texan(Cupcake):
    size = "jumbo"

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)


j_cupcake = Regular("Key Lime Tango", 3.99, "Vanilla", "Lime", "Lime Crema")
my_cupcake = Texan("Cookies and Cream", 5.99, "Chocolate", "Oreo", "Vanilla")
r_cupcake = Regular("Everything Nice", 2.99, "Spice", "Cream Cheese", "Cake Whip")
h_cupcake = Mini("Neapolitan", 1.99, "Angel Food", "Chocolate")

my_cupcake.frosting = "Chocolate"
my_cupcake.filling = "Chocolate"
my_cupcake.name = "Triple Chocolate"
my_cupcake.add_sprinkles("Chocolate", "Brown Sugar Crystals")
h_cupcake.add_sprinkles("Strawberries")
print(my_cupcake.size)
print(my_cupcake.sprinkles)
print(h_cupcake.name)
print(h_cupcake.price)
print(h_cupcake.size)

bakery_list = [
    my_cupcake,
    j_cupcake,
    r_cupcake,
    h_cupcake
]

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def write_new_csv(file, cupcakes):
    with open(file, mode= "w", newline= "\n") as csvfile:
        
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:

            if hasattr(cupcake, "filling"):

                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:

                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


write_new_csv("sample.csv", bakery_list)

def add_cupcake(file, cupcake):
    with open(file, mode= "a", newline= "\n") as csvfile:
        
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})

        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
        
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

if __name__ == "__main__":
    pass