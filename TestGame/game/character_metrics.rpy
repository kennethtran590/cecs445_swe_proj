init python:
    import abc
    import random

    # metric Abstract class
    class metric(abc.ABCMeta):

        def add(more):
            pass

        def sub(less):
            pass

        def get():
            pass

        def set(newAmount):
            pass


    class currency(metric):
        amount = 0

        def add(more):
            this.amount += more

        def sub(less):
            this.amount -= less

        def get():
            return this.amount

        def set(newAmount):
            this.amount = newAmount


    class stress(metric):
        amount = 0

        def add(more):
            this.amount += more

        def sub(less):
            this.amount -= less

        def get():
            return this.amount

        def set(newAmount):
            this.amount = newAmount


    class productivity(metric):
        amount = 0

        def add(more):
            this.amount += more

        def sub(less):
            this.amount -= less

        def get():
            return this.amount

        def set(newAmount):
            this.amount = newAmount


    class experience(metric):
        amount = 0

        def add(more):
            this.amount += more

        def sub(less):
            this.amount -= less

        def get():
            return this.amount

        def set(newAmount):
            this.amount = newAmount

    #character class that holds all metrics
    class character_metrics:
        def __init__(self):
            self.exp = 0
            self.money = 0
            self.stressLvl = 0
            self.product = 0
            self.level = 1
            self.skills = 0
            #item attributes
            self.keyboard = None
            self.chair = None
            self.mouse = None
            self.monitor = None

        # update metrics
        def updateExperience(self, level):
            self.exp = level
        def updateCurrency(self, level):
            self.money = level
        def updateStress(self, level):
            self.stressLvl= level
        def updateProductivity(self, level):
            self.product = level
        def updateTech(self, level):
            self.skills = level
         #return metrics
        def returnExperience():
            return self.exp
        def returnCurrency():
            return self.money
        def returnStress():
            return self.stressLvl
        def returnProductivity():
            return self.product
        def updates():

            if self.exp > 5000:
                self.exp =5000
            if self.stressLvl > 50:
                self.stressLvl += random.randint(1,20)
            if self.product > 250:
                self.product = 250
            if self.skills > 250:
                self.skills = 250

        def returnWeek():
            endOfWeek = week
            stressLvl += 5
            week= [0,0,0,0,0]
            return endOfWeek
        def checkForEnd(self):
            ending = False
            if self.exp <= 2000:
                ending = True
            if self.skills < 15:
                ending = True
            if self.product < 15:
                ending = True
            return ending
        def checkForWin(self):
            ending = False
            if self.exp <= 4000:
                ending = True
            if self.skills <= 200:
                ending = True
            if self.product <= 200:
                ending = True
            return ending
        # Returns the range of the randomly generated number that the player
        # gets every week depending on their level.
        def getLevelRange(self):
            if (self.level == 1):
                return 1, 5;
            if (self.level == 2):
                return 1, 10;
            if (self.level == 3):
                return 5, 10;
            if (self.level == 4):
                return 10, 15;
            if (self.level == 5):
                return 10, 20;

        def getMaxExpPerLevel(self):
            if (self.level == 1):
                return 1000;
            if (self.level == 2):
                return 2000;
            if (self.level == 3):
                return 3000;
            if (self.level == 4):
                return 4000;
            if (self.level == 5):
                return 5000;
            if (self.level >= 5):
                return 5000;

        #item methods
        def addProd(self, amount):
            self.product += amount
            if self.product > 250:
                self.product = 250

        def subStress(self, amount):
            self.stressLvl -= amount
            if self.stressLvl < 0:
                self.stressLvl = 0

        def addSkills(self, amount):
            self.skills += amount
            if self.skills > 250:
                self.skills = 250

        def addMoney(self, amount):
            self.money += amount

        def subMoney(self, amount):
            self.money = self.money - amount

        def equip_keyboard(self, keyboard):
            if(self.keyboard != None):
                self.unequip_keyboard()
            self.keyboard = keyboard
            self.product += keyboard.prod

        def unequip_keyboard(self):
            if (self.keyboard != None):
                self.product -= self.keyboard.prod
                self.keyboard = None

        def equip_mouse(self, mouse):
            if(self.mouse != None):
                self.unequip_mouse()
            self.mouse = mouse
            self.product += mouse.prod

        def unequip_mouse(self):
            if (self.mouse != None):
                self.product -= self.mouse.prod
                self.mouse = None

        def equip_chair(self, chair):
            if(self.chair != None):
                self.unequip_chair()
            self.chair = chair
            self.product += chair.prod

        def unequip_chair(self):
            if (self.chair != None):
                self.product -= self.chair.prod
                self.chair = None

        def equip_monitor(self, monitor):
            if(self.monitor != None):
                self.unequip_monitor()
            self.monitor = monitor
            self.product += monitor.prod

        def unequip_monitor(self):
            if (self.monitor != None):
                self.product -= self.monitor.prod
                self.monitor = None
    character = character_metrics()
