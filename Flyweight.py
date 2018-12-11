"""
Flyweight - Use sharing to support large numbers of fine-grained objects
efficiently.
"""

import abc


class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def operation(self, *extrinsic_state):
        return self, extrinsic_state


def printing(val, flyweight_factory):
    concrete_flyweight = flyweight_factory.get_flyweight(val)
    return concrete_flyweight.operation("hello", val)


def flyweight_main():
    flyweight_factory = FlyweightFactory()
    print(printing("hey", flyweight_factory))
    print(printing("hey", flyweight_factory))
    print(printing("key", flyweight_factory))
    print(printing("key", flyweight_factory))
    print(printing(50, flyweight_factory))
    print(printing(50, flyweight_factory))
    for i in range(3):
        print(printing(i, flyweight_factory))





if __name__ == "__main__":
     flyweight_main()
     #combinations()
