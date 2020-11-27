init python:
    class Item:
        def __init__(self, img, name, desc, buy, sell):
            self.img = img
            self.name = name
            self.desc = desc
            self.buy = buy
            self.sell = sell

    class Consumable(Item):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Item.__init__(self, img, name, desc, buy, sell)
            self.prod = prod
            self.stress = stress
            self.skills = skills

        def use(self, target):
            inventory.remove(self)
            target.addProd(self.prod)
            target.subStress(self.stress)
            target.addSkills(self.skills)
            global selected_item
            selected_item = None

    class Book(Consumable):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Consumable.__init__(self, img, name, desc, buy, sell, prod, stress, skills)

        def use(self, target):
            inventory.remove(self)
            target.addProd(self.prod)
            target.subStress(self.stress)
            target.addSkills(self.skills)
            global selected_item
            selected_item = None

    class Equipment(Item):
        def __init__(self, img, name, desc, buy, sell):
            Item.__init__(self, img, name, desc, buy, sell)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equipped = False
            self.equipped_to = None

    class Keyboard(Equipment):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Equipment.__init__(self, img, name, desc, buy, sell)
            self.prod = prod
            self.stress = stress
            self.skills = skills

        def equip(self, target):
            Equipment.equip(self, target)
            target.equip_keyboard(self)

        def unequip(self):
            self.equipped_to.unequip_keyboard()
            Equipment.unequip(self)

    class Mouse(Equipment):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Equipment.__init__(self, img, name, desc, buy, sell)
            self.prod = prod
            self.stress = stress
            self.skills = skills

        def equip(self, target):
            Equipment.equip(self, target)
            target.equip_mouse(self)

        def unequip(self):
            self.equipped_to.unequip_mouse()
            Equipment.unequip(self)

    class Chair(Equipment):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Equipment.__init__(self, img, name, desc, buy, sell)
            self.prod = prod
            self.stress = stress
            self.skills = skills

        def equip(self, target):
            Equipment.equip(self, target)
            target.equip_chair(self)

        def unequip(self):
            self.equipped_to.unequip_chair()
            Equipment.unequip(self)

    class Monitor(Equipment):
        def __init__(self, img, name, desc, buy, sell, prod, stress, skills):
            Equipment.__init__(self, img, name, desc, buy, sell)
            self.prod = prod
            self.stress = stress
            self.skills = skills

        def equip(self, target):
            Equipment.equip(self, target)
            target.equip_monitor(self)

        def unequip(self):
            self.equipped_to.unequip_monitor()
            Equipment.unequip(self)
