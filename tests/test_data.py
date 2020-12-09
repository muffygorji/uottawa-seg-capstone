from os import path

def test_column_len(preprocessed_data):
    """
    This method tests that column length is 2
    """
    assert(len(preprocessed_data.columns) == 2)

def test_url(preprocessed_data):
    """
    This method tests that url column was created
    """
    assert('url' in preprocessed_data)

def test_label(preprocessed_data):
    """
    This method tests that label column was created
    """
    assert('label' in preprocessed_data)

def test_path(preprocessed_dataset_path):
    """
    This method tests that path was created
    """
    assert(path.exists(preprocessed_dataset_path))