# Abstract factory class
from Singleton import Singleton

class ServiceFactory:
    def getHumanResources(self): pass

    def getApplications(self): pass

    def getDelivery(self): pass


class MicrosoftServiceFactory(ServiceFactory):
    def getHumanResources(self):
        return MicrosoftHumanResources()

    def getApplications(self):
        return MicrosoftApplications()

    def getDelivery(self):
        return MicrosoftDelivery()


class AppleServiceFactory(ServiceFactory):
    def getHumanResources(self):
        return AppleHumanResources()

    def getApplications(self):
        return AppleApplications()

    def getDelivery(self):
        return AppleDelivery()


class Service:
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getToolkit(self):
        return self.__toolkit

    def getType(self):
        return self.__purpose

class MicrosoftHumanResources(Service):
    def __init__(self):
        Service.__init__(self, "Microsoft", "HumanResources")


class MicrosoftApplications(Service, metaclass=Singleton):
    def __init__(self):
        Service.__init__(self, "Microsoft", "Applications")


class MicrosoftDelivery(Service, metaclass=Singleton):
    def __init__(self):
        Service.__init__(self, "Microsoft", "Delivery")


class AppleHumanResources(Service):
    def __init__(self):
        Service.__init__(self, "Apple", "HumanResources")


class AppleApplications(Service):
    def __init__(self):
        Service.__init__(self, "Apple", "Applications")


class AppleDelivery(Service):
    def __init__(self):
        Service.__init__(self, "Apple", "Delivery")


if __name__ == "__main__":
    apple = bool(input("val:"))
    microsoft = not apple

    if apple:
        infrastructure = MicrosoftServiceFactory()
    elif microsoft:
        infrastructure = AppleServiceFactory()

    human_resources = infrastructure.getHumanResources()
    applications = infrastructure.getApplications()
    delivery = infrastructure.getDelivery()
    print("%s:%s" % (human_resources.getToolkit(), human_resources.getType()), human_resources)
    print("%s:%s" % (applications.getToolkit(), applications.getType()), applications)
    print("%s:%s" % (delivery.getToolkit(), delivery.getType()), delivery)
    print()
    human_resources = infrastructure.getHumanResources()
    applications = infrastructure.getApplications()
    delivery = infrastructure.getDelivery()
    print("%s:%s" % (human_resources.getToolkit(), human_resources.getType()), human_resources)
    print("%s:%s" % (applications.getToolkit(), applications.getType()), applications)
    print("%s:%s" % (delivery.getToolkit(), delivery.getType()), delivery)
    print()
    human_resources = infrastructure.getHumanResources()
    applications = infrastructure.getApplications()
    delivery = infrastructure.getDelivery()
    print("%s:%s" % (human_resources.getToolkit(), human_resources.getType()), human_resources)
    print("%s:%s" % (applications.getToolkit(), applications.getType()), applications)
    print("%s:%s" % (delivery.getToolkit(), delivery.getType()), delivery)
