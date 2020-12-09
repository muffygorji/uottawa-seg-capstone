
def test_random_forest(model_execution_result):
    """
    This method tests Random Forest was returned
    """
    assert('Random Forest' in model_execution_result)

def test_accuracy(model_execution_result):
    """
    This method tests Accuracy in Random Forest was returned
    """
    assert('accuracy' in model_execution_result['Random Forest'])

def test_f1_score(model_execution_result):
    """
    This method tests F1 score in Random Forest was returned
    """
    assert('f1score' in model_execution_result['Random Forest'])

def test_recall(model_execution_result):
    """
    This method tests Recall in Random Forest was returned
    """
    assert('recall' in model_execution_result['Random Forest'])

def test_precision(model_execution_result):
    """
    This method tests Precision in Random Forest was returned
    """
    assert ('precision' in model_execution_result['Random Forest'])


def test_runtime(model_execution_result):
    """
    This method tests runtime in Random Forest was returned
    """
    assert ('runtime' in model_execution_result['Random Forest'])

