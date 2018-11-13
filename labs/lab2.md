
## Structural design patterns & Behavioral design patterns
- Proxy
- State
- Decorator

## Proxy with States

Here i incapsulate the implementation and return a proxy of that implementatioon.
```python3
class Proxy:
    def __init__(self, imp):
        self.__implementation = imp

    def __getattr__(self, name):
        return getattr(self.__implementation, name)

```
After what, i take the implementation from proxy and change the implementation without losing the object memory allocation in another sense we just change the *state*.
```python3
class State(Proxy):
    def __init__(self, imp):
        super().__init__(imp)

    def changeImp(self, newImp):
        super().__init__(newImp)

    def __getattr__(self, name):
        return super().__getattr__(name)
```
## Decorator
In the following diagram i try to describe a coffee and the variations that can be applied to it also i will add the implemented object in a proxy:

![ScreenShot](screens/3.png)

```python3
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
```
- The first 3 outputs show how i put the decorated object in a proxy the first one contains the declaration of proxy and the rest 2 i just change the objects in state of the same proxy.*The proof of this concept is that proxy object is using the same address.*
- In the rest 2 outputs i just demonstrate how the decorator works.

![ScreenShot](screens/4.png)