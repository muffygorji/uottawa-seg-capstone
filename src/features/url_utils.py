"""Utilities for processing URLs."""

import math
import numpy
import requests
import re
import os
import logging
import requests
from crtsh import crtshAPI

def get_digit_count(word):
  """Returns the number of digits in the word as an integer.

  Args:
    word: The string whose digits are to be counted.
  """
  count = 0
  for char in word:
    if char.isdigit():
      count += 1
  return count

def get_letter_count(word):
  """Returns the number of letters in the word as an integer.

  Args:
    word: The string whose letters are to be counted.
  """
  count = 0
  for char in word:
    if char.isalpha():
      count += 1
  return count

def get_digit_to_letter_ratio(word):
  """Returns the ratio of digits to letters in the word as a float.

  Args:
    word: The string whose digit to letter ratio is to be determined.
  """
  if not word:
    return 0

  num_letters = get_letter_count(word)
  return get_digit_count(word) / num_letters if num_letters else 0

def is_special_character(char):
  """Returns True if the character is an ASCII special character.

  The special characters can be found here:
  https://en.wikipedia.org/wiki/List_of_Unicode_characters#Latin_script.

  Args:
    char: The character to consider.
  """
  char_int = ord(char)
  return ((32 <= char_int <= 47) or (58 <= char_int <= 64) or
          (91 <= char_int <= 96) or (123 <= char_int <= 126))

def get_symbol_count(word):
  """Returns the number of symbols in the word as an integer.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters.

  Args:
    word: The string whose symbols are to be counted.
  """
  count = 0
  for char in word:
    if not char.isalnum() and not is_special_character(char):
      count += 1
  return count

def is_delimiter(char):
  """Returns True if the character is a delimiter and False otherwise.

  These characters are considered to be delimiters: {. , : / ? = - _ #}.

  Args:
    char: The character to consider.
  """
  return char in {'.', ',', ':', '/', '?', '=', '-', '_', '#'}

def get_delimiter_count(word):
  """Returns the number of delimiters in the word as an integer.

  Delimiters are elements of this set: {. , : / ? = - _ #}.

  Args:
    word: The string whose delimiters are to be counted.
  """
  count = 0
  for char in word:
    if is_delimiter(char):
      count += 1
  return count

def get_average_count(words, function):
  """Returns the average number of specified characters in words as a float.

  The function specifies a kind of character, e.g. digits.

  Args:
    words: A list of strings, e.g. ['bob8@aol.com', 'maple%20scones'].
    function: The function to apply to the given words.
  """
  num_words = 0
  total = 0

  for word in words:
    num_words += 1
    total += function(word)

  return total / num_words if num_words else 0

def get_total_count(words, function):
  """Returns the number of specified characters as an integer.

  The function specifies a kind of character, e.g. letters.
  Args:
    words: A list of strings, e.g. ['bob8@aol.com', 'maple%20scones'].
    function: The function to apply to the given words.
  """
  total = 0
  for value in words:
    total += function(value)
  return total

def get_max_length(words):
  """Returns the length of the longest word in words.
  
  Args:
    words: A list of strings, e.g. ['joe@yahoo.com', '123abc'].
  """
  maximum = 0
  for word in words:
    length = len(word)
    if length > maximum:
      maximum = length
  return maximum

def get_average_length(words):
  """Returns the average length of the words as a float.

  Args:
    words: A list of strings, e.g. ['joe@yahoo.com', '123abc'].
  """
  num_words = len(words)
  total = 0

  for word in words:
    total += len(word)

  return total / num_words if num_words else 0

def get_total_length(words):
  """Returns the total length of query variables as an integer.

  Args:
    words: A list of strings, e.g. ['joe@yahoo.com', '123abc'].
  """
  total = 0
  for word in words:
    total += len(word)
  return total

def get_n_grams(n, word):
  """Returns a list of strings that are n-grams of word.

  For example, if n is 2 and word is 'owl', the result is ['ow', 'wl'].

  Args:
    n: The size of the n-gram.
    word: The string to split into n-grams.
  """
  if n < 1:
    return []

  return [word[index:index + n] for index in range(0, len(word) - n + 1)]

def get_probabilities(words):
  """Returns a dict mapping words to their probabilities of appearing in words.

  For example, if words is ['re', 'er', 're', 'ea', 'ad'], then the result is
  {'ad': 0.2, 're': 0.4, 'er': 0.2, 'ea': 0.2}.

  Args:
    words: A list of strings, e.g. ['bl', 'lu', 'ue'].
  """
  num_words = len(words)

  if num_words < 1:
    return {}

  unique_words, counts = numpy.unique(words, return_counts=True)
  probabilities = counts / num_words

  return {unique_words[index]: probabilities[index]
          for index in range(len(unique_words))}

def get_entropy(words_to_probabilities):
  """Returns the Shannon entropy of the words' distribution as a float.

  Args:
    words_to_probabilities: A dict 
  """
  if len(words_to_probabilities) <= 1:
    return 0

  entropy = 0
  for _, probability in words_to_probabilities.items():
    entropy -= probability * math.log(probability)

  return entropy

def count_distinct_characters(word):
  """Returns the number of distinct characters in word as an integer.

  Args:
    word: A string, e.g. 'pdf'.
  """
  characters = set([char for char in word])
  return len(characters)


def ip_in_domain(domain):
  "Returns 1 if the domain contains a IP address, 0 otherwise."
  pattern = re.compile(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
  result = pattern.search(domain)
  return int(result is not None)
            
#### Incomplete Features ####

def ca_issuer(domain):
    """Returns the name of the Certificate authority (CA) issuer of the URL
      Issue with this feature: It takes so long to execute large amount of data.
    """
    ca_issuer = crtshAPI().search(domain)

    if not ca_issuer:
        return None
    else:
        return ca_issuer[0]['issuer_name']

def ca_issuer2(domain):
    """Returns the name of the Certificate authority (CA) issuer of the URL
      Another Implementation which also is unsuccessful to process large data.
    """
    url = 'https://urlscan.io/api/v1/search/?q={}&size=1'.format(domain)
    # The request returns a very nested json
    r = requests.get(url)
    json = r.json()
    if 'results' in json:
        if len(json['results']) > 0:
            if 'result' in json['results'][0]:
                result = json['results'][0]['result']
                req = requests.get(result)
                reqj = req.json()
                if 'lists' in reqj:
                    if 'certificates' in reqj['lists']:
                        if len(reqj['lists']['certificates']) > 0:
                            if 'issuer' in reqj['lists']['certificates'][0]:
                                return reqj['lists']['certificates'][0]['issuer']
    return None


def get_domain_age(url):
  """Returns the number of days a domain has existed for

  Args:
    url: A valid url, e.g. youtube.com
  """
  url_split = url.split("//")[-1].split("?")[0]
  sender = "https://input.payapi.io/v1/api/fraud/domain/age/" + url_split
  r = requests.get(sender)
  data = r.text
  url_info = data.loads(data)
  return url_info["result"]


def get_ttl(type: str, domain: str) -> int:
    """ Returns the value of the TTL (Time To Live) for a DNS A or DNS NS record
        E.g.: get_ttl("A","google.ca")) or get_ttl("NS","google.ca"))
    """
    logging.info("Entering: " + domain)
    
    if type != "A" and type != "NS":
        logging.error(type + " is not a valid type. Only type A and NS are supported.")
    else:
        command = "dig " + type + " " + domain
        
        try:
            stream = os.popen(command)
        except:
            logging.error("Exception: dig failed or no results found")
            return -1
        
        output = stream.read()
        output = output.split("\n")
        for i in range (0, len(output)):
            line = output[i]
            if line == "" or ";" in line:
                continue;
            else:
                results = output[i].split("\t")
                try:
                    ttl = results[2]
                except:
                    logging.error("Error: failed to get ttl")
                    return -1
                return ttl
