import pytest
import pandas as pd
import src.models.model_utils as models
import json
from src.data.make_dataset import make_dataset
from src.features.build_features import build_features
from src.models.train_model import execute_models
from src.models.predict_model import predict_model
from api import app


@pytest.fixture(scope='session')
def config():
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
    return config

@pytest.fixture(scope='session')
def preprocessed_data():
    df = make_dataset()
    return df

@pytest.fixture(scope='session')
def preprocessed_dataset_path(config):
    return config['data']['data_loc']

@pytest.fixture(scope='session')
def dataset_with_features(preprocessed_data):
    df_with_features = build_features(preprocessed_data, True)
    return df_with_features

@pytest.fixture(scope='session')
def dataset_with_features_path(config):
    return config['data']['dataframe_loc']

@pytest.fixture(scope='session')
def model_execution_result(dataset_with_features):
    model_execution_result = execute_models(dataset_with_features)
    return model_execution_result

@pytest.fixture(scope='session')
def predict_url():
    return "https://www.youtube.com/channel/UCdG2SN326Vzdobb0EFykZfA?guidded_help_flow=3"

@pytest.fixture(scope='session')
def prediction_result(predict_url):
    prediction_result = predict_model(predict_url)
    return prediction_result

@pytest.fixture(scope='session')
def test_dataset_path():
    return "tests/test_data/processed_data_for_testing.csv"

@pytest.fixture(scope='session')
def random_forest_result(test_dataset_path):
    df = pd.read_csv(test_dataset_path)
    y = models.load_labels_for_training(df)
    x = models.load_data(df)
    datalog = models.random_forest(x,y)
    return datalog

@pytest.fixture(scope='session')
def test_url_1():
    return "https://www.google.com/webhp?sxsrf=green#colour%20"

@pytest.fixture(scope='session')
def test_url_2():
    return "wwwgo0gle4!dj5$6"

@pytest.fixture(scope='session')
def test_url_3():
    return "https://234.154.5.23:40"

@pytest.fixture(scope='session')
def test_url_4():
    return "https://www.google.com/pink.png"

@pytest.fixture(scope='session')
def test_url_5():
    return "https://www.google.com:80"

@pytest.fixture(scope='session')
def test_url_6():
    return "https://www.google.com/green.exe"

@pytest.fixture(scope='session')
def test_url_7():
    return "https://www.google.com/webhp?s23£rf=gr£§n143&id5=rt123&name19§=45£"

@pytest.fixture(scope='session')
def test_url_8():
    return "www.go0gle.c4/!dj5$6"

@pytest.fixture(scope='session')
def test_url_9():
    return "wwwgoodcom👌"

@pytest.fixture(scope='session')
def test_url_10():
    return "234.154.5.23"

@pytest.fixture(scope='session')
def api_client():
    return app.test_client()

@pytest.fixture(scope='session')
def api_root_route(config):
    return config['data']['api']['root_route']

@pytest.fixture(scope='session')
def api_curl_route(config):
    return config['data']['api']['curl_route']

@pytest.fixture(scope='session')
def api_file_load_route(config):
    return config['data']['api']['file_load_route']
