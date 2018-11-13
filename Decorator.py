# decorators
import ProxyState


class DrinkComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Espresso(DrinkComponent):
    cost = 0.75


class EspressoConPanna(DrinkComponent):
    cost = 1.0


class Cappuccino(DrinkComponent):
    cost = 1.0


class CafeLatte(DrinkComponent):
    cost = 1.0


class CafeMocha(DrinkComponent):
    cost = 1.25


class Decorator(DrinkComponent):
    def __init__(self, drinkComponent):
        self.component = drinkComponent

        print(self.component.getDescription() + ' ' + DrinkComponent.getDescription(self), ":",
              self.component.getTotalCost(), DrinkComponent.getTotalCost(self), "=",
              self.component.getTotalCost() + DrinkComponent.getTotalCost(self))

    def getTotalCost(self):
        return self.component.getTotalCost() + DrinkComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + DrinkComponent.getDescription(self)


class ExtraEspresso(Decorator):
    cost = 0.75

    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Whipped(Decorator):
    cost = 0.50

    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Decaf(Decorator):
    cost = 3.4

    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Dry(Decorator):
    cost = 0.5

    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Wet(Decorator):
    cost = 0.0

    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


print('----------Process----------proxy cappuccino')
cappuccino = ProxyState.State(Cappuccino())
print(cappuccino.getDescription(), ": $", cappuccino.getTotalCost())
print(cappuccino.__repr__())
print()
print('----------Process----------proxy cappuccino')
cappuccino.changeImp(Whipped(Decaf(Cappuccino())))
print(cappuccino.getDescription(), ": $", cappuccino.getTotalCost())
print(cappuccino.__repr__())
print()
print('----------Process----------proxy cappuccino')
cappuccino.changeImp(Decaf(Whipped(Cappuccino())))
print(cappuccino.getDescription(), ": $", cappuccino.getTotalCost())
print(cappuccino.__repr__())
print()
print('----------Process----------proxy test cappuccino')
test = Decaf(Whipped(Cappuccino()))
print(test.getDescription(), ": $", test.getTotalCost())
print(test.__repr__())
print()
print('----------Process----------')
Hyper = ExtraEspresso(Decaf(Dry(EspressoConPanna())))
print(Hyper.getDescription(), ": $", Hyper.getTotalCost())
print(Hyper.__repr__())
