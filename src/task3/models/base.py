from abc import abstractmethod, ABC


class DigitClassificationInterface(ABC):
    @abstractmethod
    def train(self, x, y):
        pass

    @abstractmethod
    def predict(self, x):
        pass
