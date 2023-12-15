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

class Soda(Beverage):
    def __init__(self):
        super().__init__(['water', 'flavoring', 'gas'])

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



