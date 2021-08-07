class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return "{name} is served from {start} to {end}".format(name=self.name, start=self.start_time, end=self.end_time)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price += self.items[item]
        return total_price

class Franchise:
    def __init__(self, address, menu):
        self.address = address
        self.menu = menu

    def __repr__(self):
        return "Located at {address}".format(address=self.address)

    def avaialable_menus(self, time):
        available_menu = []
        for menu in self.menu:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

brunch_menu =  {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }
early_bird_menu = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
dinner_menu = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
kids_menu = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
    }

brunch = Menu('Brunch', brunch_menu, 1100, 1600)
early_bird = Menu('Early Bird', early_bird_menu, 1500, 1800)
dinner = Menu('Dinner', dinner_menu, 1700, 2300)
kids = Menu('Kids', kids_menu, 1100, 2100)
arepas = Menu('Arepas', arepas_menu, 1000, 2000)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])
arepas_place = Franchise('189 Fitzgerald Avenue', arepas)

print(flagship_store.avaialable_menus(1200))
print(flagship_store.avaialable_menus(1700))

arepas_business = Business("Take a' Arepa", arepas_place)