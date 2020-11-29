init python:

    class Player:
        def __init__(self, level, exp, cash, prod, stress, skills):
            self.level = level
            self.exp = exp
            self.prod = prod
            self.stress = stress
            self.skills = skills
            self.cash = cash
            self.keyboard = None
            self.chair = None
            self.mouse = None
            self.monitor = None
            self.keyboard_equipped = False

        def addProd(self, amount):
            self.prod += amount
            if self.prod > 250:
                self.prod = 250

        def subStress(self, amount):
            self.stress -= amount
            if self.stress < 0:
                self.stress = 0

        def addSkills(self, amount):
            self.skills += amount
            if self.skills > 250:
                self.skills = 250

        def addcash(self, amount):
            self.cash += amount

        def subcash(self, amount):
            self.cash = self.cash - amount

        def equip_keyboard(self, keyboard):
            if(self.keyboard != None):
                self.unequip_keyboard()

            self.keyboard = keyboard
            self.prod += keyboard.prod
            self.keyboard_equipped = True

        def unequip_keyboard(self):
            if (self.keyboard != None):
                self.prod -= self.keyboard.prod
                self.keyboard = None
                self.keyboard_equipped = False

        def equip_mouse(self, mouse):
            if(self.mouse != None):
                self.unequip_mouse()

            self.mouse = mouse
            self.prod += mouse.prod

        def unequip_mouse(self):
            if (self.mouse != None):
                self.prod -= self.mouse.prod
                self.mouse = None

        def equip_chair(self, chair):
            if(self.chair != None):
                self.unequip_chair()

            self.chair = chair
            self.prod += chair.prod

        def unequip_chair(self):
            if (self.chair != None):
                self.prod -= self.chair.prod
                self.chair = None

        def equip_monitor(self, monitor):
            if(self.monitor != None):
                self.unequip_monitor()

            self.monitor = monitor
            self.prod += monitor.prod

        def unequip_monitor(self):
            if (self.monitor != None):
                self.prod -= self.monitor.prod
                self.monitor = None
