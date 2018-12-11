import abc
import Prototype as P
from Strategy import *


def prnt(proto):
    for i in range(len(proto)):
        print()
        print(proto[i])
        print(proto[i].getType())
        print(proto[i].getValue())


def clone(proto, length):
    for i in range(length):
        proto.append(proto[i].clone())


def upfly(v, flyweight_factory):
    this = P.ProductType1(F.printing("flyweight2", flyweight_factory))
    this2 = P.ProductType2(F.printing("flyweight1", flyweight_factory))
    return v and this or this2


def upstr(v, str, flyweight_factory):
    this = P.ProductType1(str.execute(flyweight_factory))
    this2 = P.ProductType2(str.execute(flyweight_factory))
    return v and this or this2


def combinations():
    flyweight_factory = F.FlyweightFactory()
    proto = []
    proto.append(upfly(True, flyweight_factory))
    proto.append(upfly(False, flyweight_factory))
    clone(proto, 2)
    prnt(proto)

    print("\n-------------New strategy-------------")
    strategy = []
    strategy.append(StrategyExample())
    strategy.append(StrategyExample(replace1))
    strategy.append(StrategyExample(replace2))
    strategy[1].name = 'Strategy Example 1'
    strategy[2].name = 'Strategy Example 2'

    testex = upstr(True, strategy[0], flyweight_factory)
    print(testex.getType())
    print(testex.getValue())
    proto[0] = upstr(True, strategy[1], flyweight_factory)
    proto[1] = upstr(False, strategy[2], flyweight_factory)
    prnt(proto)


if __name__ == "__main__":
    combinations()
