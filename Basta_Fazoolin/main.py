class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {menu} menu is available between {start:.2f} and {end:.2f}".format(menu = self.name, start=self.start_time, end=self.end_time)

    def calculate_bill(self, purchased_items):
        return sum(self.items[item] for item in purchased_items)


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Located at {address}".format(address=self.address)

    def available_menus(self, time):
        avail_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                avail_menus.append(menu.name)

        return avail_menus


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises



# All Menu related stuff.
brunch = Menu('brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11.00, 16.00)

early_bird = Menu('early bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15.00, 18.00)

dinner = Menu('dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17.00, 23.00)

kids = Menu('kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11.00, 21.00)

arepas_menu = Menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10.00, 20.00)

all_menus = [brunch, early_bird, dinner, kids, arepas_menu]

# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# All Franchise related stuff.
flagship_store = Franchise('1232 West End Road', all_menus)
new_installment = Franchise('12 East Mulberry Street', all_menus)
arepas_place = Franchise('189 Fitzgerald Avenue', all_menus)

print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


# All Business related stuff.
business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas = Business("Take a' Arepa", arepas_place)