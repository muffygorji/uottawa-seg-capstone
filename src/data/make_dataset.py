import logging
import pandas as pd
import json
from dotenv import find_dotenv, load_dotenv
from pandas_profiling import ProfileReport

load_dotenv(find_dotenv())


def convert_string_label_to_int(data):
    """
    Converts a list of string (malicious/benign) to a list of int (1/0)
    :param data: an array of string
    :return: an array of int
    """
    new_column = []
    for row in data:
        if row == "malicious":
            new_column.append(1)
        elif row == "benign":
            new_column.append(0)
        else:
            # TODO: Add this error to logger
            raise Exception("invalid valid for label. must either be 'malicious' or 'benign'")
    return new_column


def make_dataset():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
        Returns: dataframe
    """
    logger = logging.getLogger(__name__)
    logger.info('Making final data set from raw data')
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)

    datasets = config['data']['datasets']
    final_file = []  # Combine all the dataframes into an array

    for key in datasets:
        dataset_details = config['data']['datasets'][key]
        path = dataset_details['path']
        csv_data = pd.read_csv(path)
        csv_data.rename(columns={dataset_details["columns"]["url"]: "url"},
                        inplace=True)  # Make sure the url column is called 'url'

        if dataset_details["columns"]["label"] is None and dataset_details['label'] is not None:
            # label column is not included. but a value is given to append
            set_label = dataset_details['label']

            if set_label == "malicious":
                label = 1
            elif set_label == "benign":
                label = 0
            else:
                # TODO: Add this error to logger
                raise ValueError("Invalid label. Please provide either 'malicious' or 'benign' as the label in config "
                                 "file.")

            csv_data['label'] = label  # Add a new columns "label" and assign the label

        elif dataset_details["columns"]["label"] is not None:
            # label column is populated already.
            column_type = csv_data['label'].dtype

            if column_type != 'int64': # if the label is not integer
                if column_type == 'O':  # convert if the column type is string/object
                    csv_data['label'] = convert_string_label_to_int(csv_data['label'])
                else:
                    # TODO: Add this error to logger
                    raise TypeError("invalid column type. Label must either be integer or string.")

        else:
            # TODO: Add this error to logger
            raise ValueError("Not enough data to create the dataset. Please provide a value for the label in the "
                             "config file")

        final_file.append(csv_data)  # Add the processed dataframe to the array

    result = pd.concat(final_file, sort=False)  # combine the dataframes into one dataframes
    # Take only the 'url' and 'label' columns
    final_columns = result[['url', 'label']]

    final_columns.to_csv(config['data']['data_loc'], index=False)  # Save the processed file into the 'data' directory

    logger.info('Finished making the final data set')
    logger.info('Preparing a report for the data set.')

    # Create a report from the processed data
    profile = ProfileReport(final_columns, minimal=True, title='Preprocessed Data Report',
                            html={'style': {'full_width': True}})
    profile.to_file(output_file="data/processed/preprocessed_data_report.html")
    logger.info('The report is ready. It can be found at data/processed/preprocessed_data_report.html')

    return final_columns
