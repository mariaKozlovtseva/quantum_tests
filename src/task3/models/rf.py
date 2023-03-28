import numpy as np
from sklearn.ensemble import RandomForestClassifier
from .base import DigitClassificationInterface
from utils.config import RANDOM_STATE

# np.random.seed(RANDOM_STATE)


class RFClassifier(DigitClassificationInterface):
    def __init__(self):
        self.clf = RandomForestClassifier(n_estimators=10, random_state=RANDOM_STATE)

    def train(self, x, y):
        # it was said in task not to implement train function
        raise NotImplementedError

    def predict(self, x: np.ndarray) -> int:
        """
        Given image X (as flattened array), predict its digit
        :param x: np.ndarray of shape 1x784
        :return: predicted digit
        """
        # as we can't use RF as "untrained" model, I decided to fit it on random data
        self.clf.fit(np.random.randn(*x.shape), np.random.randint(0, 10, 1))
        pred = self.clf.predict(x)[0]
        return pred
