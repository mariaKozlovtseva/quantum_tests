import numpy as np
from .base import DigitClassificationInterface
from utils.config import RANDOM_STATE

# np.random.seed(RANDOM_STATE)


class RandomClassifier(DigitClassificationInterface):
    def train(self, x, y):
        raise NotImplementedError

    def predict(self, x) -> int:
        return np.random.randint(0, 10, 1)[0]
