import this
import abc
# metric Abstract class
class metric(metaclass=abc.ABCMeta):
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
class character:
    exp= experience
    money = currency
    stressLvl = stress
    product = productivity
    level =1
    skills =0
    # update metrics
    def updateExperience(level ):
      this.exp = level
    def updateCurrency(level ):
      this.exp = level
    def updateStress(level ):
      this.exp = level
    def updateProductivity(level ):
      this.exp = level
     #return metrics
    def returnExperience():
      return this.exp
    def returnCurrency():
      return this.money
    def returnStress():
      return this.stressLvl
    def returnProductivity():
      return this.product
