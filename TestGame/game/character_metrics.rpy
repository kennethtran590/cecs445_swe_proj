init python:
    import abc

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
        week = [0,0,0,0,0] #, exp, money, stress, productivity, skills
        exp = 0
        money = 0
        stressLvl = 0
        product = 0
        level = 1
        skills = 0
        # update metrics
        def updateExperience(self, level):
            exp = level
            week[0] += level
        def updateCurrency(self, level):
            money = level
            week[1] += level
        def updateStress(self, level):
            stressLvl= level
            week[2] += level
        def updateProductivity(self, level):
            product = level
            week[3] += level
        def updateSkills(self, level):
            skills = level
            week[4] += level
         #return metrics
        def returnExperience():
            return this.exp
        def returnCurrency():
            return this.money
        def returnStress():
            return this.stressLvl
        def returnProductivity():
            return this.product
        def updates():
            if money < 0:
                stress +=0
            if exp > 0:
                exp =0
            if stress > 0:
                product +=0
            if product > 0:
                money =0
        def returnWeek():
            endOfWeek = week
            week= [0,0,0,0,0]
            return endOfWeek

        # Returns the range of the randomly generated number that the player
        # gets every week depending on their level.
        def getLevelRange(self):
            if (self.level == 1):
                return 1, 10;
            if (self.level == 2):
                return 1, 15;
            if (self.level == 3):
                return 5, 20;
            if (self.level == 4):
                return 10, 25;
            if (self.level == 5):
                return 15, 30;
            if (self.levell == 6):
                return 20, 35;
            if (self.level == 7):
                return 25, 40;
            if (self.level == 8):
                return 30, 45;
            if (self.level == 9):
                return 35, 50;
            if (self.level == 3):
                return 40, 55;

    character = character_metrics()
