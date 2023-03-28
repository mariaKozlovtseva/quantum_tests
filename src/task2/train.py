import click
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from typing import Optional
from utils.config import DATA_DIR, MODELS_DIR, RANDOM_STATE
from utils.data_loader import load_data


@click.command()
@click.option('--val-size', type=float, default=0.2, help='Proportion of validation size.')
@click.option('--n-estimators', type=int, default=10, help='The number of trees in the forest.')
@click.option('--max-depth', type=int, default=None, help='The maximum depth of the tree.')
@click.option('--use-all-feats', is_flag=True,
              help='Whether to use all feature set or select only best features (from research).')
def train(
        val_size: float,
        n_estimators: int,
        max_depth: Optional[int],
        use_all_feats: bool):
    """
    Trains RandomForestRegressor with given params.
    :param val_size: Proportion of validation size
    :param n_estimators: The number of trees in the forest
    :param max_depth: The maximum depth of the tree
    :param use_all_feats: Whether to use all feature set or select only best features (from research)
    :return: None
    """
    print(f'Params: val_size {val_size}, n_estimators {n_estimators}, '
          f'max_depth {max_depth}, use_all_feats = {use_all_feats}')
    df = load_data(DATA_DIR / 'task2/train.csv')
    y = df['target']
    x = df.iloc[:, :-1] if use_all_feats else df[['6', '7']]

    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=val_size, random_state=RANDOM_STATE)

    reg = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=RANDOM_STATE)
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_val)
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))
    print(f'Val RMSE is: {round(rmse, 5)}')
    with open(MODELS_DIR / 'task2/random_forest_model.pkl', 'wb') as f:
        pickle.dump(reg, f)


if __name__ == '__main__':
    train()
