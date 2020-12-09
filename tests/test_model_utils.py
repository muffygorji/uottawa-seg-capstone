import pytest
import pandas as pd
import src.models.model_utils as models

def test_random_forest_accuracy_key(random_forest_result):
    '''
    This method tests accuracy key from random forest results
    '''
    assert('accuracy' in random_forest_result)

def test_random_forest_f1score_key(random_forest_result):
    '''
    This method tests f1score key from random forest results
    '''
    assert('f1score' in random_forest_result)

def test_random_forest_precision_key(random_forest_result):
    '''
    This method tests precision key from random forest results
    '''
    assert('precision' in random_forest_result)

def test_random_forest_recall_key(random_forest_result):
    '''
    This method tests recall key from random forest results
    '''
    assert('recall' in random_forest_result)

def test_random_forest_accuracy_value(random_forest_result):
    '''
    This method tests accuracy value from random forest results
    '''
    assert(random_forest_result['accuracy'] >= 0)

def test_random_forest_f1score_value(random_forest_result):
    '''
    This method tests f1score value from random forest results
    '''
    assert(random_forest_result['f1score'] >= 0)

def test_random_forest_precision_value(random_forest_result):
    '''
    This method tests precision value from random forest results
    '''
    assert(random_forest_result['precision'] >= 0)

def test_random_forest_recall_value(random_forest_result):
    '''
    This method tests recall value from random forest results
    '''
    assert(random_forest_result['recall'] >= 0)

