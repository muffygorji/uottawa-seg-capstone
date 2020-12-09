import src.features.url_utils as url_utils

def test_digit_count_digit_exists(test_url_8):
    """
    This method tests correct column value when digit count exists
    """
    digit_count = url_utils.get_digit_count(test_url_8)
    assert (digit_count == 4)

def test_digit_count_digit_does_not_exist(test_url_9):
    """
    This method tests correct column value when no digit count exists
    """
    digit_count = url_utils.get_digit_count(test_url_9)
    assert (digit_count == 0)

def test_letter_count_letter_exists(test_url_8):
    """
    This method tests correct column value when letter count exists
    """
    letter_count = url_utils.get_letter_count(test_url_8)
    assert (letter_count == 11)

def test_letter_count_letter_does_not_exist(test_url_10):
    """
    This method tests correct column value when no letter count exists
    """
    letter_count = url_utils.get_letter_count(test_url_10)
    assert (letter_count == 0)

def test_digit_to_letter_ratio_exists(test_url_8):
    """
    This method tests correct column value when letter ratio exists
    """
    digit_letter_ratio = url_utils.get_digit_to_letter_ratio(test_url_8)
    assert (digit_letter_ratio == (4/11))

def test_digit_to_letter_ratio_does_not_exist(test_url_9):
    """
    This method tests correct column value when no letter ratio exists
    """
    digit_letter_ratio = url_utils.get_digit_to_letter_ratio(test_url_9)
    assert (digit_letter_ratio == (0/10))

def test_symbol_count_symbol_exists(test_url_9):
    """
    This method tests correct column value when symbol count exists
    """
    symbol_count = url_utils.get_symbol_count(test_url_9)
    assert (symbol_count == 1)

def test_symbol_count_symbol_does_not_exist(test_url_8):
    """
    This method tests correct column value when no symbol count exists
    """
    symbol_count = url_utils.get_symbol_count(test_url_8)
    assert (symbol_count == 0)

def test_delimiter_count_exists(test_url_8):
    """
    This method tests correct column value when delimiter count exists
    """
    delimiter_count = url_utils.get_delimiter_count(test_url_8)
    assert (delimiter_count == 3)

def test_delimiter_count_does_not_exist(test_url_9):
    """
    This method tests correct column value when no delimiter count exists
    """
    delimiter_count = url_utils.get_delimiter_count(test_url_9)
    assert (delimiter_count == 0)

def test_ip_in_domain_exists(test_url_10):
    """
    This method tests correct column value when ip in domain exists
    """
    ip_domain = url_utils.ip_in_domain(test_url_10)
    assert (ip_domain == 1)

def test_ip_in_domain_does_not_exist(test_url_8):
    """
    This method tests correct column value when no ip in domain exists
    """
    ip_domain = url_utils.ip_in_domain(test_url_8)
    assert (ip_domain == 0)
