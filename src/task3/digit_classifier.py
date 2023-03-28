import click
import numpy as np
import torch
import torchvision
from torchvision.transforms import transforms
from torchvision.transforms.functional import center_crop
from typing import Optional
from models.random import RandomClassifier
from models.cnn import CNNClassifier
from models.rf import RFClassifier
from utils.config import DATA_DIR

MODEL_MAP = {
    'rand': RandomClassifier(),
    'cnn': CNNClassifier(),
    'rf': RFClassifier()
}


def load_image(path: str, image_id: Optional[int] = None):
    dataset = torchvision.datasets.MNIST(
        path, train=False, transform=transforms.ToTensor(), download=True)
    if image_id is None:
        image_id = np.random.randint(0, len(dataset))
    print(f'Predicting digit for an image {image_id}')
    data, target = dataset[image_id]
    target = torch.tensor([target])
    return data, target


class DigitClassifier:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = MODEL_MAP[model_name]

    def train(self):
        self.model.train()

    def preprocess_image(self, image):
        if self.model_name == 'rand':
            # shape will be 10 x 10
            image = center_crop(image, [10, 10])[0].numpy()
        elif self.model_name == 'rf':
            # shape will be 1 x 784
            image = torch.reshape(image, (1, -1)).numpy()
        # else shape is 1 x 28 x 28
        return image

    def predict(self, image_id: Optional[int] = None):
        image, target = load_image(DATA_DIR / 'task3', image_id)
        image = self.preprocess_image(image)
        pred = self.model.predict(image)
        print(f'Target: {target[0]}, prediction: {pred} (by {self.model_name} model)')


@click.command()
@click.option('--model-name', type=click.Choice(['cnn', 'rand', 'rf']),
              default='rand', help='Model to use for image classification.')
@click.option('--image-id', type=click.IntRange(0, 9999, clamp=True),
              default=None, help='Model to use for image classification.')
def classify(model_name: str, image_id: Optional[int] = None):
    """
    Given chosen model predicts digit for a random image
    :param model_name: Model to use for image classification: cnn, rand (by default), rf
    :param image_id: For which image ID (from 0 to 10000) make prediction, if None - take random image
    :return: None
    """
    clf = DigitClassifier(model_name=model_name)
    clf.predict(image_id)


if __name__ == '__main__':
    classify()
