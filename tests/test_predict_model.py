
def test_result_keys_url(prediction_result):
    """tests if url key exists in the prediction result"""
    assert ('url' in prediction_result)

def test_result_keys_model(prediction_result):
    """tests if model key exists in the prediction result"""
    assert ('model' in prediction_result)

def test_result_keys_prediction_score(prediction_result):
    """tests if prediction score key exists in the prediction result"""
    assert ('prediction_score' in prediction_result)

def test_result_keys_confidence_score(prediction_result):
    """tests if confidence score key exists in the prediction result"""
    assert ('confidence_score' in prediction_result)