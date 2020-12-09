from src.features.build_features import build_features
from src.models import model_utils
import mlflow
import json
import pickle5 as pickle
import pandas as pd

with open('config.json') as json_data_file:
    cfgload = json.load(json_data_file)

with open(cfgload['data']['random-forest']['filename'], 'rb') as pickle_file:
    rf = pickle.load(pickle_file)

def predict_model(url):
    """
    Retuns a list containing the result of the prediction
    The list shows the url, model, precition score, and confidence score.

    Args:
        url: A string

    Retuns:
        A list with 4 keys: url, model, prediction_score, confidence_score
    """

    df = ['' + url]
    df = pd.DataFrame(df, columns=['url'])

    dataframe = build_features(df, False)
    domain = dataframe['domain'][0]
    features = dataframe.to_dict(orient="records")[0]
    dataframe = model_utils.load_data(dataframe)

    # Find the prediction score and condience score of the model
    random_forest_pred_score = rf.predict(dataframe).tolist()[0]
    random_forest_confidence_score = round(rf.predict_proba(dataframe)[0][random_forest_pred_score], 2)

    result = {'url': url,
              'domain': domain,
              'model': 'Random Forest',
              'prediction_score': random_forest_pred_score,
              'confidence_score': random_forest_confidence_score,
              'features': features
              }
    print(result)

    metric_logger(url, result)

    return result


def metric_logger(url, data):

    with mlflow.start_run():
        mlflow.log_param("url", url)
        mlflow.log_param("Model", data['model'])
        mlflow.log_metric("Prediction Score", data['prediction_score'])
        mlflow.log_metric("Confidence Score", data['confidence_score'])
