import src.models.model_utils as models
import pandas as pd
import json

def execute_models(processed_data_with_features):
    """ Execute one or more models from model_utils
        (here we just want to use random forest model
        as it produced the best results)
        
        Args: processed_data_with_features is the resulting data after discretization
        
        Returns: data_to_be_logged is the data produced from
        our (random forest) model
    """

    y = models.load_labels_for_training(processed_data_with_features)
    x = models.load_data(processed_data_with_features)

    with open('config.json') as json_data_file:
        cfgload = json.load(json_data_file)

    model_dataframe = pd.read_csv(cfgload['data']['dataframe_loc'])

    label_collection = []
    for label in model_dataframe['label']:
        if label == 'benign':
            label_collection.append(0)
        else:
            label_collection.append(1)
    model_dataframe['label_discrete'] = label_collection
    model_dataframe.drop(
        columns=['Unnamed: 0', 'url', 'label', 'domain', 'path', 'query', 'decoded_query_values', 'fragment',
                 'file_ext'], axis=1, inplace=True, errors='ignore')

    rf = models.random_forest(x, y)
    models.mlflow_logger(rf)
    print("returning data")
    data_to_be_logged = {'Random Forest': rf}
    return data_to_be_logged

