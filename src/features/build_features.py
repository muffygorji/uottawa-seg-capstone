import json
import logging
import time
import src.features.url_utils as url_utils
import src.features.url_analysis as url_analysis
from dotenv import find_dotenv, load_dotenv

with open('config.json') as json_data_file:
    dataset = json.load(json_data_file)

load_dotenv(find_dotenv())

final_dataset_path = dataset['data']['processed-output'] + 'final_processed_with_features.csv'

def build_features(df, csv):
    """
    returns a dataframe with all the columns created and populated

    Args:
        df: A dataframe
        csv: A boolean. If True, the df data will be written to a csv file

    Returns:
        A dataframe.
    """
    logger = logging.getLogger(__name__)

    for url in df["url"]:
        # Ellapsed time check for efficiency
        start = time.time()
        # URL Features
        logger.info("beginning URL Features")
        df["url_delimiter_count"] = df["url"].map(lambda x: url_utils.get_delimiter_count(x))
        df["url_digit_count"] = df["url"].map(lambda x: url_utils.get_digit_count(x))
        df["url_letter_count"] = df["url"].map(lambda x: url_utils.get_letter_count(x))
        df["url_symbol_count"] = df["url"].map(lambda x: url_utils.get_symbol_count(x))
        df["url_digit_to_letter_ratio"] = df["url"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))
        df["url_encodes_characters"] = df["url"].map(lambda x: url_analysis.encodes_characters(x))
        df["url_uses_https"] = df["url"].map(lambda x: url_analysis.uses_https(x))
        df["url_get_port"] = df["url"].map(lambda x: url_analysis.get_port(x))
        df["url_uses_default_port_number"] = df["url"].map(lambda x: url_analysis.uses_default_port_number(x))
        df["ip_in_url"] = df["url"].map(lambda x: url_analysis.ip_in_url(x))

        # Domain Features
        logger.info("beginning DOMAIN features")
        df["domain"] = df["url"].map(lambda x: url_analysis.get_domain(x))
        # Above line is necessary for the lines below. Will get an NPE otherwise
        df["domain_delimiter_count"] = df["domain"].map(lambda x: url_utils.get_delimiter_count(x))
        df["domain_digit_count"] = df["domain"].map(lambda x: url_utils.get_digit_count(x))
        df["domain_letter_count"] = df["domain"].map(lambda x: url_utils.get_letter_count(x))
        df["domain_symbol_count"] = df["domain"].map(lambda x: url_utils.get_symbol_count(x))
        df["domain_digit_to_letter_ratio"] = df["domain"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))
        df["subdomain_in"] = df["url"].map(lambda x: url_analysis.get_subdomain_in(x))
        df["ip_in_domain"] = df["domain"].map(lambda x: url_utils.ip_in_domain(x))

        # Path Features
        logger.info("beginning PATH Features")
        df["path"] = df["url"].map(lambda x: url_analysis.get_path(x))
        df["path_delimiter_count"] = df["path"].map(lambda x: url_utils.get_delimiter_count(x))
        df["path_digit_count"] = df["path"].map(lambda x: url_utils.get_digit_count(x))
        df["path_letter_count"] = df["path"].map(lambda x: url_utils.get_letter_count(x))
        df["path_symbol_count"] = df["path"].map(lambda x: url_utils.get_symbol_count(x))
        df["path_digit_to_letter_ratio"] = df["path"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))

        # Query Features
        logger.info("beginning QUERY Features")
        df["query"] = df["url"].map(lambda x: url_analysis.get_query(x))
        df["query_delimiter_count"] = df["query"].map(lambda x: url_utils.get_delimiter_count(x))
        df["query_digit_count"] = df["query"].map(lambda x: url_utils.get_digit_count(x))
        df["query_letter_count"] = df["query"].map(lambda x: url_utils.get_letter_count(x))
        df["query_symbol_count"] = df["query"].map(lambda x: url_utils.get_symbol_count(x))
        df["query_digit_to_letter_ratio"] = df["query"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))

        df["decoded_query_values"] = df["url"].map(lambda x: url_analysis.get_decoded_query_values(x))
        df["total_query_value_length"] = df["url"].map(lambda x: url_analysis.get_total_query_value_length(x))
        df["avg_query_value_length"] = df["url"].map(lambda x: url_analysis.get_average_query_value_length(x))
        df["max_query_value_length"] = df["url"].map(lambda x: url_analysis.get_max_query_value_length(x))
        df["total_query_value_digit_count"] = df["url"].map(lambda x: url_analysis.get_total_query_value_digit_count(x))
        df["avg_query_value_digit_count"] = df["url"].map(lambda x: url_analysis.get_average_query_value_digit_count(x))
        df["total_query_value_digit_count"] = df["url"].map(
            lambda x: url_analysis.get_total_query_value_letter_count(x))
        df["avg_query_value_letter_count"] = df["url"].map(
            lambda x: url_analysis.get_average_query_value_letter_count(x))
        df["total_query_value_symbol_count"] = df["url"].map(
            lambda x: url_analysis.get_total_query_value_symbol_count(x))
        df["avg_query_value_symbol_count"] = df["url"].map(
            lambda x: url_analysis.get_average_query_value_symbol_count(x))

        df["total_query_variable_length"] = df["url"].map(lambda x: url_analysis.get_total_query_variable_length(x))
        df["avg_query_variable_length"] = df["url"].map(lambda x: url_analysis.get_average_query_variable_length(x))
        df["max_query_variable_length"] = df["url"].map(lambda x: url_analysis.get_max_query_variable_length(x))
        df["total_query_variable_digit_count"] = df["url"].map(
            lambda x: url_analysis.get_total_query_variable_digit_count(x))
        df["avg_query_variable_digit_count"] = df["url"].map(
            lambda x: url_analysis.get_average_query_variable_digit_count(x))
        df["total_query_variable_digit_count"] = df["url"].map(
            lambda x: url_analysis.get_total_query_variable_letter_count(x))
        df["avg_query_variable_letter_count"] = df["url"].map(
            lambda x: url_analysis.get_average_query_variable_letter_count(x))
        df["total_query_variable_symbol_count"] = df["url"].map(
            lambda x: url_analysis.get_total_query_variable_symbol_count(x))
        df["avg_query_variable_symbol_count"] = df["url"].map(
            lambda x: url_analysis.get_average_query_variable_symbol_count(x))

        # Fragment features
        logger.info("beginning FRAGMENT Features")
        df["fragment"] = df["url"].map(lambda x: url_analysis.get_fragment(x))
        df["fragment_delimiter_count"] = df["fragment"].map(lambda x: url_utils.get_delimiter_count(x))
        df["fragment_digit_count"] = df["fragment"].map(lambda x: url_utils.get_digit_count(x))
        df["fragment_letter_count"] = df["fragment"].map(lambda x: url_utils.get_letter_count(x))
        df["fragment_symbol_count"] = df["fragment"].map(lambda x: url_utils.get_symbol_count(x))
        df["fragment_digit_to_letter_ratio"] = df["fragment"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))

        # # EXT features
        logger.info("beginning EXT Features")
        df["file_ext"] = df["url"].map(lambda x: url_analysis.get_file_ext(x))
        df["file_ext_delimiter_count"] = df["file_ext"].map(lambda x: url_utils.get_delimiter_count(x))
        df["file_ext_digit_count"] = df["file_ext"].map(lambda x: url_utils.get_digit_count(x))
        df["file_ext_letter_count"] = df["file_ext"].map(lambda x: url_utils.get_letter_count(x))
        df["file_ext_symbol_count"] = df["file_ext"].map(lambda x: url_utils.get_symbol_count(x))
        df["file_ext_digit_to_letter_ratio"] = df["file_ext"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))
        df["file_ext_is_executable"] = df["file_ext"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))
        # Break is necessary here
        break
    end = time.time()
    logger.info("Ellapsed time: " + str(end - start) + " for features")
    if csv:
        logger.info("Sending to CSV...")
        df.to_csv(final_dataset_path, index=False)
    return df
