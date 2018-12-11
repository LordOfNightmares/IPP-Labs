import copy


class Prototype:
    """ Object, that can be cloned.
    This is just a base class, so the clone() method
    is not implemented. But all subclasses have to
    override it.
    """

    _type = None
    _value = None

    def clone(self):
        pass
    def getType(self):
        return self._type

    def getValue(self):
        return self._value


class ProductType1(Prototype):
    """ Concrete prototype.

    Implementation of Prototype. Important part is the
    clone() method.
    """

    def __init__(self, number):
        self._type = self
        self._value = number

    def clone(self):
        return copy.copy(self)


class ProductType2(Prototype):
    """ Concrete prototype. """

    def __init__(self, number):
        self._type = self
        self._value = number

    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    p = []
    p.append(ProductType1(1))
    p.append(p[0].clone())
    p.append(ProductType2(2))
    p.append(p[2].clone())
    for i in range(len(p)):
        print(p[i], p[i].getType(), p[i].getValue())
