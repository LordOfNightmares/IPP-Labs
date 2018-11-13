# Proxy with states


class Proxy:
    def __init__(self, imp):
        self.__implementation = imp

    def __getattr__(self, name):
        return getattr(self.__implementation, name)


class State(Proxy):
    def __init__(self, imp):
        super().__init__(imp)

    def changeImp(self, newImp):
        super().__init__(newImp)

    def __getattr__(self, name):
        return super().__getattr__(name)


'''
class Implementation1:
    def f(self):
        print("Fiddle de dum, Fiddle de dee,")

    def g(self):
        print("Eric the half a bee.")

    def h(self):
        print("Ho ho ho, tee hee hee,")


class Implementation2:
    def f(self):
        print("We're Knights of the Round Table.")

    def g(self):
        print("We dance whenever we're able.")

    def h(self):
        print("We do routines and chorus scenes")



def run(b):
    b.f()
    b.g()
    b.h()


print('------Proxy')
d = Proxy(Implementation1())
p = Proxy(d)
run(p)
print('\n------State Imp 1')
b = State(Implementation1())
run(b)
print('\n------State Imp 2')
b.changeImp(Implementation2())
run(b)
print('\n------State Imp 1')
b.changeImp(Implementation1())
run(b)
'''
