class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def price(self):
        pass

class Water(Beverage):
    def __init__(self):
        super().__init__(['water'])

    def price(self):
        return 50

class Soda(Beverage): # No encontre la manera de heredar de Water, si heredo no puedo declarar la lista de ingredientes
    def __init__(self):
        super().__init__(['sugar', 'water', 'carbon dioxide'])

    def price(self):
        return Water().price() * 3

class Cortado(Beverage):
    def __init__(self):
        super().__init__(['coffee', 'milk'])

    def price(self):
        return 250

class CreamyCoffeeGranita(Beverage):
    def __init__(self):
        super().__init__(['milk', 'coffee', 'brown sugar', 'cinnamon'])

    def price(self):
        return 50 * len(self.ingredients)

class Machine:
    def __init__(self, beverages):
        self.beverages = beverages
        self.revenue = 0

    def prepare_beverage(self, Beverage):
        self.revenue += Beverage.price()
        return Beverage

    def total_revenue(self):
        return self.revenue

    def most_expensive_beverage(self):
        return max(self.beverages, key=lambda beverage: beverage.price())



# Create some beverages
water = Water()
soda = Soda()
cortado = Cortado()
creamy_coffee_granita = CreamyCoffeeGranita()

# Create a machine with these beverages
machine = Machine([water, soda, cortado, creamy_coffee_granita])

# Prepare a soda and a creamy coffee granita
machine.prepare_beverage(soda)
machine.prepare_beverage(creamy_coffee_granita)

# Print the total revenue of the machine
print(machine.total_revenue())

# Print the most expensive beverage the machine can offer
print(type(machine.most_expensive_beverage()).__name__)