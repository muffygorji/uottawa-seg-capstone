import src.features.url_analysis as url_analysis

def test_get_domain_exists(test_url_1):
    """
    This method tests correct column value when domain exists
    """
    domain = url_analysis.get_domain(test_url_1)
    assert (domain == 'www.google.com')

def test_domain_does_not_exist(test_url_2):
    """
    This method tests correct column value when no domain exists
    """
    domain = url_analysis.get_domain(test_url_2)
    assert (domain == '')

def test_get_query_exists(test_url_1):
    """
    This method tests correct column value when query exists
    """
    query = url_analysis.get_query(test_url_1)
    assert (query == 'sxsrf=green')

def test_get_query_does_not_exist(test_url_2):
    """
    This method tests correct column value when no query exists
    """
    query = url_analysis.get_query(test_url_2)
    assert (query == '')

def test_get_path_exists(test_url_1):
    """
    This method tests correct column value when path exists
    """
    path = url_analysis.get_path(test_url_1)
    assert (path == '/webhp')

def test_get_path_does_not_exist(test_url_3):
    """
    This method tests correct column value when no path exists
    """
    path = url_analysis.get_path(test_url_3)
    assert (path == '')

def test_get_fragment_exists(test_url_1):
    """
    This method tests correct column value when fragment exists
    """
    fragment = url_analysis.get_fragment(test_url_1)
    assert (fragment == 'colour%20')

def test_get_fragment_does_not_exist(test_url_2):
    """
    This method tests correct column value when no fragment exists
    """
    fragment = url_analysis.get_fragment(test_url_2)
    assert (fragment == '')

def test_get_file_ext_exists(test_url_4):
    """
    This method tests correct column value when file extension exists
    """
    file = url_analysis.get_file_ext(test_url_4)
    assert (file == 'png')

def test_get_file_ext_does_not_exist(test_url_1):
    """
    This method tests correct column value when no file extension exists
    """
    file = url_analysis.get_file_ext(test_url_1)
    assert (file == '')

def test_encodes_characters_exists(test_url_1):
    """
    This method tests correct column value when encodes characters exists
    """
    encodes = url_analysis.encodes_characters(test_url_1)
    assert (encodes == 1)

def test_encodes_characters_does_not_exist(test_url_2):
    """
    This method tests correct column value when no encodes characters exists
    """
    encodes = url_analysis.encodes_characters(test_url_2)
    assert (encodes == 0)

def test_uses_https_exists(test_url_1):
    """
    This method tests correct column value when https exists
    """
    https = url_analysis.uses_https(test_url_1)
    assert (https == 1)

def test_uses_https_does_not_exist(test_url_2):
    """
    This method tests correct column value when no https exists
    """
    https = url_analysis.uses_https(test_url_2)
    assert (https == 0)

def test_get_port_exists(test_url_3):
    """
    This method tests correct column value when port exists
    """
    port = url_analysis.get_port(test_url_3)
    assert (port == 40)

def test_get_port_does_not_exist(test_url_1):
    """
    This method tests correct column value when no port exists
    """
    port = url_analysis.get_port(test_url_1)
    assert (port == -1)

def test_uses_default_port_number_exists(test_url_5):
    """
    This method tests correct column value when port number exists
    """
    port = url_analysis.uses_default_port_number(test_url_5)
    assert (port == 1)

def test_uses_default_port_number_does_not_exist(test_url_3):
    """
    This method tests correct column value when no port number exists
    """
    port = url_analysis.uses_default_port_number(test_url_3)
    assert (port == 0)

def test_is_executable_exists(test_url_6):
    """
    This method tests correct column value when url is executable
    """
    executable = url_analysis.is_executable(test_url_6)
    assert (executable == 1)

def test_is_executable_does_not_exist(test_url_4):
    """
    This method tests correct column value when url is not executable
    """
    executable = url_analysis.is_executable(test_url_4)
    assert (executable == 0)

def test_get_decoded_query_values_exists(test_url_7):
    """
    This method tests correct column value when decoded query values exists
    """
    decoded_query_values = url_analysis.get_decoded_query_values(test_url_7)
    assert (decoded_query_values == ['gr£§n143', 'rt123', '45£'])

def test_get_decoded_query_values_does_not_exist(test_url_2):
    """
    This method tests correct column value when no decoded query values exists
    """
    decoded_query_values = url_analysis.get_decoded_query_values(test_url_2)
    assert (decoded_query_values == [])

def test_get_average_query_value_digit_count_exists(test_url_7):
    """
    This method tests correct column value when average query value digit count exists
    """
    digit = url_analysis.get_average_query_value_digit_count(test_url_7)
    assert (digit == (8.0/3.0))

def test_get_average_query_value_digit_count_does_not_exist(test_url_4):
    """
    This method tests correct column value when no average query value digit count exists
    """
    digit = url_analysis.get_average_query_value_digit_count(test_url_4)
    assert (digit == 0.0)

def test_get_total_query_value_digit_count_exists(test_url_7):
    """
    This method tests correct column value when total query value digit count exists
    """
    digit = url_analysis.get_total_query_value_digit_count(test_url_7)
    assert (digit == 8)

def test_get_total_query_value_digit_count_does_not_exist(test_url_4):
    """
    This method tests correct column value when no total query value digit count exists
    """
    digit = url_analysis.get_total_query_value_digit_count(test_url_4)
    assert (digit == 0)

def test_get_average_query_value_letter_count_exists(test_url_7):
    """
    This method tests correct column value when average query value letter count exists
    """
    value = url_analysis.get_average_query_value_letter_count(test_url_7)
    assert (value == (5.0/3.0))

def test_get_average_query_value_letter_count_does_not_exist(test_url_3):
    """
    This method tests correct column value when no average query value letter count exists
    """
    value = url_analysis.get_average_query_value_letter_count(test_url_3)
    assert (value == 0.0)

def test_get_total_query_value_letter_count_exists(test_url_7):
    """
    This method tests correct column value when total query value letter count exists
    """
    value = url_analysis.get_total_query_value_letter_count(test_url_7)
    assert (value == 5)

def test_get_total_query_value_letter_count_does_not_exist(test_url_3):
    """
    This method tests correct column value when no total query value letter count exists
    """
    value = url_analysis.get_total_query_value_letter_count(test_url_3)
    assert (value == 0)

def test_get_average_query_value_symbol_count_exists(test_url_7):
    """
    This method tests correct column value when average query value symbol count exists
    """
    symbol = url_analysis.get_average_query_value_symbol_count(test_url_7)
    assert (symbol == (3.0/3.0))

def test_get_average_query_value_symbol_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no average query value symbol count exists
    """
    symbol = url_analysis.get_average_query_value_symbol_count(test_url_1)
    assert (symbol == 0.0)

def test_get_total_query_value_symbol_count_exists(test_url_7):
    """
    This method tests correct column value when total query value symbol count exists
    """
    symbol = url_analysis.get_total_query_value_symbol_count(test_url_7)
    assert (symbol == 3)

def test_get_total_query_value_symbol_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no total query value symbol count exists
    """
    symbol = url_analysis.get_total_query_value_symbol_count(test_url_1)
    assert (symbol == 0)

def test_get_max_query_value_length_exists(test_url_7):
    """
    This method tests correct column value when max query value length exists
    """
    value_length = url_analysis.get_max_query_value_length(test_url_7)
    assert (value_length == 8)

def test_get_max_query_value_length_does_not_exist(test_url_4):
    """
    This method tests correct column value when no max query value length exists
    """
    value_length = url_analysis.get_max_query_value_length(test_url_4)
    assert (value_length == 0)

def test_get_average_query_value_length_exists(test_url_7):
    """
    This method tests correct column value when average query value length exists
    """
    value_length = url_analysis.get_average_query_value_length(test_url_7)
    assert (value_length == (16/3))

def test_get_average_query_value_length_does_not_exist(test_url_4):
    """
    This method tests correct column value when no average query value length exists
    """
    value_length = url_analysis.get_average_query_value_length(test_url_4)
    assert (value_length == 0.0)

def test_get_total_query_value_length_exists(test_url_7):
    """
    This method tests correct column value when total query value length exists
    """
    value_length = url_analysis.get_total_query_value_length(test_url_7)
    assert (value_length == 16)

def test_get_total_query_value_length_does_not_exist(test_url_4):
    """
    This method tests correct column value when no total query value length exists
    """
    value_length = url_analysis.get_total_query_value_length(test_url_4)
    assert (value_length == 0)

def test_get_average_query_variable_digit_count_exists(test_url_7):
    """
    This method tests correct column value when average query variable digit exists
    """
    value_length = url_analysis.get_average_query_variable_digit_count(test_url_7)
    assert (value_length == (5/3))

def test_get_average_query_variable_digit_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no average query variable digit exists
    """
    value_length = url_analysis.get_average_query_variable_digit_count(test_url_1)
    assert (value_length == 0)

def test_get_total_query_variable_digit_count_exists(test_url_7):
    """
    This method tests correct column value when total query variable digit exists
    """
    value_length = url_analysis.get_total_query_variable_digit_count(test_url_7)
    assert (value_length == 5)

def test_get_total_query_variable_digit_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no total query variable digit exists
    """
    value_length = url_analysis.get_total_query_variable_digit_count(test_url_1)
    assert (value_length == 0)

def test_get_average_query_variable_letter_count_exists(test_url_7):
    """
    This method tests correct column value when average query variable letter exists
    """
    value_length = url_analysis.get_average_query_variable_letter_count(test_url_7)
    assert (value_length == (9/3))

def test_get_average_query_variable_letter_count_does_not_exist(test_url_3):
    """
    This method tests correct column value when no average query variable letter exists
    """
    value_length = url_analysis.get_average_query_variable_letter_count(test_url_3)
    assert (value_length == 0)

def test_get_total_query_variable_letter_count_exists(test_url_7):
    """
    This method tests correct column value when total query variable letter exists
    """
    value_length = url_analysis.get_total_query_variable_letter_count(test_url_7)
    assert (value_length == 9)

def test_get_total_query_variable_letter_count_does_not_exist(test_url_3):
    """
    This method tests correct column value when no total query variable letter exists
    """
    value_length = url_analysis.get_total_query_variable_letter_count(test_url_3)
    assert (value_length == 0)

def test_get_average_query_variable_symbol_count_exists(test_url_7):
    """
    This method tests correct column value when average query variable symbol exists
    """
    value_length = url_analysis.get_average_query_variable_symbol_count(test_url_7)
    assert (value_length == (2/3))

def test_get_average_query_variable_symbol_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no average query variable symbol exists
    """
    value_length = url_analysis.get_average_query_variable_symbol_count(test_url_1)
    assert (value_length == 0)

def test_get_total_query_variable_symbol_count_exists(test_url_7):
    """
    This method tests correct column value when total query variable symbol exists
    """
    value_length = url_analysis.get_total_query_variable_symbol_count(test_url_7)
    assert (value_length == 2)

def test_get_total_query_variable_symbol_count_does_not_exist(test_url_1):
    """
    This method tests correct column value when no total query variable symbol exists
    """
    value_length = url_analysis.get_total_query_variable_symbol_count(test_url_1)
    assert (value_length == 0)

def test_get_max_query_variable_length_exists(test_url_7):
    """
    This method tests correct column value when max query variable length exists
    """
    value_length = url_analysis.get_max_query_variable_length(test_url_7)
    assert (value_length == 7)

def test_get_max_query_variable_length_does_not_exist(test_url_3):
    """
    This method tests correct column value when no max query variable length exists
    """
    value_length = url_analysis.get_max_query_variable_length(test_url_3)
    assert (value_length == 0)

def test_get_average_query_variable_length_exists(test_url_7):
    """
    This method tests correct column value when average query variable length exists
    """
    value_length = url_analysis.get_average_query_variable_length(test_url_7)
    assert (value_length == (16/3))

def test_get_average_query_variable_length_does_not_exist(test_url_3):
    """
    This method tests correct column value when no average query variable length exists
    """
    value_length = url_analysis.get_average_query_variable_length(test_url_3)
    assert (value_length == 0)

def test_get_total_query_variable_length_exists(test_url_7):
    """
    This method tests correct column value when total query variable length exists
    """
    value_length = url_analysis.get_total_query_variable_length(test_url_7)
    assert (value_length == 16)

def test_get_total_query_variable_length_does_not_exist(test_url_3):
    """
    This method tests correct column value when no total query variable length exists
    """
    value_length = url_analysis.get_total_query_variable_length(test_url_3)
    assert (value_length == 0)

def test_get_subdomain_in_exist(test_url_1):
    """
    This method tests correct column value when subdomain exists
    """
    subdomain = url_analysis.get_subdomain_in(test_url_1)
    assert (subdomain == 1)

def test_get_subdomain_in_does_not_exist(test_url_3):
    """
    This method tests correct column value when no subdomain in exists
    """
    subdomain = url_analysis.get_subdomain_in(test_url_3)
    assert (subdomain == 0)

def test_ip_in_url_exist(test_url_3):
    """
    This method tests correct column value when ip in url exists
    """
    url = url_analysis.ip_in_url(test_url_3)
    assert (url == 1)

def test_ip_in_url_does_not_exist(test_url_4):
    """
    This method tests correct column value when no ip in url exists
    """
    url = url_analysis.ip_in_url(test_url_4)
    assert (url == 0)