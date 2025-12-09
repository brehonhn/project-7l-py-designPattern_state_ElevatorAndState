# states/base_state.py
from abc import ABC, abstractmethod



class ElevatorState(ABC):
    @abstractmethod
    def request_up(self, elevator: "Elevator"):
        pass

    @abstractmethod
    def request_down(self, elevator: "Elevator"):
        pass

    @abstractmethod
    def step(self, elevator: "Elevator"):
        pass

    def __str__(self):
        return self.__class__.__name__
