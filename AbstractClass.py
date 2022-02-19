from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self) :print("vehicle can go")
class cycle(vehicle):
    def go(self) : print("cycle can go")
class car(vehicle):
    def go(self) : print(" car can go")
class bike(vehicle):
    def go(self) : print("bike can go")

class animal:
    def go(self) : print("animal can go")

animal().go()
print()
cycle().go()
