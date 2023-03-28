import pickle
import pandas as pd
from utils.config import DATA_DIR, MODELS_DIR
from utils.data_loader import load_data


def predict():
    """
    Loads last trained model and applies it to test df
    :return: None
    """
    try:
        with open(MODELS_DIR / 'task2/random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        print('Model wasn\'t found. Please call task2/train.py first')
        return
    test_df = load_data(DATA_DIR / 'task2/hidden_test.csv')
    test_df = test_df[model.feature_names_in_]
    y_pred = model.predict(test_df)
    pd.DataFrame(y_pred, columns=['y_pred']).to_csv(DATA_DIR / 'task2/hidden_test_preds.csv', index=False)


if __name__ == '__main__':
    predict()
