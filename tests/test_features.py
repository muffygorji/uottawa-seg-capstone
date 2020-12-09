from os import path

def test_column_len(dataset_with_features):
    """
        This method tests that column length is 62
    """
    assert (len(dataset_with_features.columns) == 62)

def test_url(dataset_with_features):
    """
    This method url that path was created
    """
    assert('url' in dataset_with_features)

def test_label(dataset_with_features):
    """
    This method label that path was created
    """
    assert('label' in dataset_with_features)

def test_url_delimiter_count(dataset_with_features):
    """
    This method tests that url_delimiter_count was created
    """
    assert('url_delimiter_count' in dataset_with_features)

def test_url_digit_count(dataset_with_features):
    """
    This method tests that url_digit_count was created
    """
    assert('url_digit_count' in dataset_with_features)

def test_url_letter_count(dataset_with_features):
    """
    This method tests that url_letter_count was created
    """
    assert('url_letter_count' in dataset_with_features)

def test_url_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that url_digit_to_letter_ratio was created
    """
    assert('url_digit_to_letter_ratio' in dataset_with_features)

def test_url_get_port(dataset_with_features):
    """
    This method tests that url_get_port was created
    """
    assert('url_get_port' in dataset_with_features)

def test_url_uses_default_port_number(dataset_with_features):
    """
    This method tests that url_uses_default_port_number was created
    """
    assert('url_uses_default_port_number' in dataset_with_features)

def test_domain_delimiter_count(dataset_with_features):
    """
    This method tests that domain_delimiter_count was created
    """
    assert('domain_delimiter_count' in dataset_with_features)

def test_domain_digit_count(dataset_with_features):
    """
    This method tests that domain_digit_count was created
    """
    assert('domain_digit_count' in dataset_with_features)

def test_domain_letter_count(dataset_with_features):
    """
    This method tests that domain_letter_count was created
    """
    assert('domain_letter_count' in dataset_with_features)

def test_domain_symbol_count(dataset_with_features):
    """
    This method tests that domain_symbol_count was created
    """
    assert('domain_symbol_count' in dataset_with_features)

def test_domain_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that domain_digit_to_letter_ratio was created
    """
    assert('domain_digit_to_letter_ratio' in dataset_with_features)

def test_path_delimiter_count(dataset_with_features):
    """
    This method tests that path_delimiter_count was created
    """
    assert('path_delimiter_count' in dataset_with_features)

def test_path_digit_count(dataset_with_features):
    """
    This method tests that path_digit_count was created
    """
    assert('path_digit_count' in dataset_with_features)

def test_path_letter_count(dataset_with_features):
    """
    This method tests that path_letter_count was created
    """
    assert('path_letter_count' in dataset_with_features)

def test_path_symbol_count(dataset_with_features):
    """
    This method tests that path_symbol_count was created
    """
    assert('path_symbol_count' in dataset_with_features)

def test_path_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that path_digit_to_letter_ratio was created
    """
    assert('path_digit_to_letter_ratio' in dataset_with_features)

def test_query_delimiter_count(dataset_with_features):
    """
    This method tests that query_delimiter_count was created
    """
    assert('query_delimiter_count' in dataset_with_features)

def test_query_digit_count(dataset_with_features):
    """
    This method tests that query_digit_count was created
    """
    assert('query_digit_count' in dataset_with_features)

def test_query_letter_count(dataset_with_features):
    """
    This method tests that query_letter_count was created
    """
    assert('query_letter_count' in dataset_with_features)

def test_query_symbol_count(dataset_with_features):
    """
    This method tests that query_symbol_count was created
    """
    assert('query_symbol_count' in dataset_with_features)

def test_query_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that query_digit_to_letter_ratio was created
    """
    assert('query_digit_to_letter_ratio' in dataset_with_features)

def test_total_query_value_length(dataset_with_features):
    """
    This method tests that total_query_value_length was created
    """
    assert('total_query_value_length' in dataset_with_features)

def test_avg_query_value_length(dataset_with_features):
    """
    This method tests that avg_query_value_length was created
    """
    assert('avg_query_value_length' in dataset_with_features)

def test_max_query_value_length(dataset_with_features):
    """
    This method tests that max_query_value_length was created
    """
    assert('max_query_value_length' in dataset_with_features)

def test_total_query_value_digit_count(dataset_with_features):
    """
    This method tests that total_query_value_digit_count was created
    """
    assert('total_query_value_digit_count' in dataset_with_features)

def test_avg_query_value_digit_count(dataset_with_features):
    """
    This method tests that avg_query_value_digit_count was created
    """
    assert('avg_query_value_digit_count' in dataset_with_features)

def test_avg_query_value_letter_count(dataset_with_features):
    """
    This method tests that avg_query_value_letter_count was created
    """
    assert('avg_query_value_letter_count' in dataset_with_features)

def test_total_query_value_symbol_count(dataset_with_features):
    """
    This method tests that total_query_value_symbol_count was created
    """
    assert('total_query_value_symbol_count' in dataset_with_features)

def test_avg_query_value_symbol_count(dataset_with_features):
    """
    This method tests that avg_query_value_symbol_count was created
    """
    assert('avg_query_value_symbol_count' in dataset_with_features)

def test_total_query_variable_length(dataset_with_features):
    """
    This method tests that total_query_variable_length was created
    """
    assert('total_query_variable_length' in dataset_with_features)

def test_avg_query_variable_length(dataset_with_features):
    """
    This method tests that avg_query_variable_length was created
    """
    assert('avg_query_variable_length' in dataset_with_features)

def test_max_query_variable_length(dataset_with_features):
    """
    This method tests that max_query_variable_length was created
    """
    assert('max_query_variable_length' in dataset_with_features)

def test_total_query_variable_digit_count(dataset_with_features):
    """
    This method tests that total_query_variable_digit_count was created
    """
    assert('total_query_variable_digit_count' in dataset_with_features)

def test_avg_query_variable_digit_count(dataset_with_features):
    """
    This method tests that avg_query_variable_digit_count was created
    """
    assert('avg_query_variable_digit_count' in dataset_with_features)

def test_avg_query_variable_letter_count(dataset_with_features):
    """
    This method tests that avg_query_variable_letter_count was created
    """
    assert('avg_query_variable_letter_count' in dataset_with_features)

def test_total_query_variable_symbol_count(dataset_with_features):
    """
    This method tests that total_query_variable_symbol_count was created
    """
    assert('total_query_variable_symbol_count' in dataset_with_features)

def test_avg_query_variable_symbol_count(dataset_with_features):
    """
    This method tests that avg_query_variable_symbol_count was created
    """
    assert('avg_query_variable_symbol_count' in dataset_with_features)

def test_fragment_delimiter_count(dataset_with_features):
    """
    This method tests that fragment_delimiter_count was created
    """
    assert('fragment_delimiter_count' in dataset_with_features)

def test_fragment_digit_count(dataset_with_features):
    """
    This method tests that fragment_digit_count was created
    """
    assert('fragment_digit_count' in dataset_with_features)

def test_fragment_letter_count(dataset_with_features):
    """
    This method tests that fragment_letter_count was created
    """
    assert('fragment_letter_count' in dataset_with_features)

def test_fragment_symbol_count(dataset_with_features):
    """
    This method tests that fragment_symbol_count was created
    """
    assert('fragment_symbol_count' in dataset_with_features)

def test_fragment_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that fragment_digit_to_letter_ratio was created
    """
    assert('fragment_digit_to_letter_ratio' in dataset_with_features)

def test_file_ext_delimiter_count(dataset_with_features):
    """
    This method tests that file_ext_delimiter_count was created
    """
    assert('file_ext_delimiter_count' in dataset_with_features)

def test_file_ext_digit_count(dataset_with_features):
    """
    This method tests that file_ext_digit_count was created
    """
    assert('file_ext_digit_count' in dataset_with_features)

def test_file_ext_letter_count(dataset_with_features):
    """
    This method tests that file_ext_letter_count was created
    """
    assert('file_ext_letter_count' in dataset_with_features)

def test_file_ext_symbol_count(dataset_with_features):
    """
    This method tests that file_ext_symbol_count was created
    """
    assert('file_ext_symbol_count' in dataset_with_features)

def test_file_ext_digit_to_letter_ratio(dataset_with_features):
    """
    This method tests that file_ext_digit_to_letter_ratio was created
    """
    assert('file_ext_digit_to_letter_ratio' in dataset_with_features)

def test_file_ext_is_executable(dataset_with_features):
    """
    This method tests that file_ext_is_executable was created
    """
    assert('file_ext_is_executable' in dataset_with_features)

def test_subdomain_in(dataset_with_features):
    """
    This method tests that subdomain_in was created
    """
    assert('subdomain_in' in dataset_with_features)

def test_path(dataset_with_features_path):
    """
    This method tests that path was created
    """
    assert(path.exists(dataset_with_features_path))

