"""A class for analyzing a URL and its components.

A URL has the general form protocol://domain/path;parameters?query#fragment.
"""

import os
from urllib import parse
import tldextract
import src.features.url_utils as url_utils
import re

def get_domain(url):
  """Returns the domain as a string."""
  components = parse.urlparse(url)
  return components.netloc

def get_query(url):
  """Returns the query as a decoded string."""
  components = parse.urlparse(url)
  return components.query

def get_path(url):
  """Returns the path as a string."""
  components = parse.urlparse(url)
  return components.path

def get_fragment(url):
  """Returns the fragment as a string."""
  components = parse.urlparse(url)
  return components.fragment

def get_file_ext(url):
  """Returns the URL's file extension, e.g. 'pdf'.

  If there is no file extension, returns an empty string.
  """
  components = parse.urlparse(url)
  _, extension = os.path.splitext(components.path)
  return extension[1:]  # Removes the leading '.' from, e.g., '.txt'.

def encodes_characters(url):
  """Returns 1 if the URL encodes characters and 0 otherwise."""
  components = parse.urlparse(url)
  return int('%' in url)

def uses_https(url):
  """Returns 1 if the URL uses HTTPS and 0 otherwise."""
  components = parse.urlparse(url)
  return int(components.scheme == 'https')

def get_port(url):
  """Returns the port number, if any. Otherwise, returns None.

  Valid port numbers are between 0 and 65535, inclusively.
  """
  components = parse.urlparse(url)
  return components.port if components.port != None else -1

def uses_default_port_number(url):
  """Returns 1 if the port number is 80 (http) or 443 (https).

  Note that if the URL does not have a port number, then this returns 0.
  """
  components = parse.urlparse(url)
  return int(components.port == 80 or components.port == 443)
  
def get_length_ratio(url, word):
  """Returns the ratio of the word's length to the URL's length.

  Args:
    word: A string, e.g. 'www.xe.com'.

  Returns:
    A float for the ratio of the given word to the URL length.
  """
  components = parse.urlparse(url)
  return len(word) / len(components.url) if components.url else 0.0

def is_executable(url):
  """Returns 1 if the extension is 'exe' and 0 otherwise.

  Args:
    extension: A string extension, e.g. 'doc' or 'exe'.
  """
  return int(get_file_ext(url) == 'exe')

def get_encoded_query_params(url):
  """Returns a dict mapping query string variables to encoded values.

  For example, {'id': ['123', '456'], 'login': ['max%40yahoo.com']} could be
  returned.
  """
  components = parse.urlparse(url)
  decoded_query_params = parse.parse_qs(components.query)
  variables_to_encoded_values = {}
  for variable, values in decoded_query_params.items():
    encoded_values = [parse.quote(value) for value in values]
    variables_to_encoded_values[variable] = encoded_values
  return variables_to_encoded_values

def get_decoded_query_values(url):
  """Returns a list of string query values without percent-encoding.

  For example, if {'q': ['maple tea'], 'email': ['liz@aol.com']} represents
  the query parameters, then ['maple tea', 'liz@aol.com'] is returned.
  """
  components = parse.urlparse(url)
  values = []
  decoded_query_params = parse.parse_qs(components.query)
  # _ for throwaway in loop, the values are what we're after
  for _, lists_of_values in decoded_query_params.items():
    values.extend(lists_of_values)
  return values

def _get_encoded_query_values(url):
  """Returns a list of percent-encoded string query values.

  For example, if {'login': ['jay%40hotmail.com'], 'id': ['24', 68']}
  represents the query parameters, then ['jay%40hotmail.com', '24', '68'] is
  returned.
  """
  components = parse.urlparse(url)
  values = []
  for _, lists_of_values in get_encoded_query_params(url).items():
    values.extend(lists_of_values)
  return values

def get_average_query_value_digit_count(url):
  """Returns the average number of digits of query values as a float.

  Digits in the decoded values, e.g. ['$9.99', '3_owls'] are counted.
  """
  return url_utils.get_average_count(
      get_decoded_query_values(url), url_utils.get_digit_count)

def get_total_query_value_digit_count(url):
  """Returns the number of digits found in query values as an int.

  Digits in the decoded values, e.g. ['$9.99', '3_owls'] are counted.
  """
  return url_utils.get_total_count(
      get_decoded_query_values(url), url_utils.get_digit_count)

def get_average_query_value_letter_count(url):
  """Returns the average number of letters of query values as a float.

  Letters in the decoded values, e.g. ['a@aol.com', 'a b'], are counted.
  """
  return url_utils.get_average_count(
      get_decoded_query_values(url), url_utils.get_letter_count)

def get_total_query_value_letter_count(url):
  """Returns the number of letters found in query values as an int.

  Letters in the decoded values, e.g. ['a@aol.com', 'a b'], are counted.
  """
  return url_utils.get_total_count(
      get_decoded_query_values(url), url_utils.get_letter_count)

def get_average_query_value_symbol_count(url):
  """Returns the average number of symbols of query values as a float.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters. Symbols in the decoded values, e.g. ['§ Results', '£45'], are
  counted.
  """
  return url_utils.get_average_count(
      get_decoded_query_values(url), url_utils.get_symbol_count)

def get_total_query_value_symbol_count(url):
  """Returns the number of symbols found in query values as an int.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters. Symbols in the decoded values, e.g. ['§ Results', '£45'], are
  counted.
  """
  return url_utils.get_total_count(
      get_decoded_query_values(url), url_utils.get_symbol_count)

def get_max_query_value_length(url):
  """Returns the length of the longest query value as an integer.

  The lengths of the decoded values, e.g. ['a@aol.com', 'a b'], are
  considered.
  """
  return url_utils.get_max_length(get_decoded_query_values(url))

def get_average_query_value_length(url):
  """Returns the average length of query values as a float."""
  return url_utils.get_average_length(get_decoded_query_values(url))

def get_total_query_value_length(url):
  """Returns the total length of the query values as an integer."""

  return url_utils.get_total_length(get_decoded_query_values(url))

def get_average_query_variable_digit_count(url):
  """Returns the average number of digits of query variables as a float."""
  components = parse.urlparse(url)
  return url_utils.get_average_count(
      parse.parse_qs(components.query).keys(), url_utils.get_digit_count)

def get_total_query_variable_digit_count(url):
  """Returns the number of digits in query variables as an integer."""
  components = parse.urlparse(url)
  return url_utils.get_total_count(
      parse.parse_qs(components.query).keys(), url_utils.get_digit_count)

def get_average_query_variable_letter_count(url):
  """Returns the average number of letters of query variables as a float."""
  components = parse.urlparse(url)
  return url_utils.get_average_count(
      parse.parse_qs(components.query).keys(), url_utils.get_letter_count)

def get_total_query_variable_letter_count(url):
  """Returns the number of letters in query variables as an integer."""
  components = parse.urlparse(url)
  return url_utils.get_total_count(
      parse.parse_qs(components.query).keys(), url_utils.get_letter_count)

def get_average_query_variable_symbol_count(url):
  """Returns the average number of symbols of query variables as a float.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters.
  """
  components = parse.urlparse(url)
  return url_utils.get_average_count(
      parse.parse_qs(components.query).keys(), url_utils.get_symbol_count)

def get_total_query_variable_symbol_count(url):
  """Returns the number of symbols of query variables as an integer.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters.
  """
  components = parse.urlparse(url)
  return url_utils.get_total_count(
      parse.parse_qs(components.query).keys(), url_utils.get_symbol_count)

def get_max_query_variable_length(url):
  """Returns the length of the longest query variable as an integer."""
  components = parse.urlparse(url)
  return url_utils.get_max_length(parse.parse_qs(components.query).keys())

def get_average_query_variable_length(url):
  """Returns the average length of query variables as a float."""
  components = parse.urlparse(url)
  return url_utils.get_average_length(parse.parse_qs(components.query).keys())

def get_total_query_variable_length(url):
  """Returns the total length of query variables as an integer."""
  components = parse.urlparse(url)
  return url_utils.get_total_length(parse.parse_qs(components.query).keys())

def get_subdomain_in(url):
  """Returns 0 if subdomain doesnot exist, and 1 if it does exist."""
  url_features = tldextract.extract(url)
  return int(len(url_features.subdomain) != 0)

def ip_in_url(url):
  """Returns 1 if the url contains an IP address, 0 otherwise."""
  pattern = re.compile(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
  result = pattern.search(url)
  return int(result is not None)