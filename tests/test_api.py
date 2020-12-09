import io
import os
import csv


def test_api_server(api_client, api_root_route):
    """ Tests that server is working """
    response = api_client.get(api_root_route)
    assert response.get_json() == {'message': 'Welcome to Phishing Detection App',
                                   'possible routes': '/api/api_curl/ ; /api/api_files/'}


def test_api_curl_no_url(api_client, api_curl_route):
    """ Test if no url is passed """
    response = api_client.post(api_curl_route)
    response_data = response.get_json()
    assert response_data == 'Please provide a url as a -d parameter: curl -d "url=<insert_url>"  ' \
                            'http://127.0.0.1:8080/api/api_curl/'


def test_api_curl_valid_url(api_client, api_curl_route):
    """ Test if a valid url is passed """
    response = api_client.post(api_curl_route, data={'url': 'https://www.google.com'})
    response_data = response.get_json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert 'result' in response_data
    assert 'url' in response_data.get('result')
    assert 'confidence_score' in response_data.get('result')
    assert 'confidence_score' in response_data.get('result')
    assert 'features' in response_data.get('result')
    assert 'domain' in response_data.get('result')
    assert 'model' in response_data.get('result')


def test_api_curl_invalid_url(api_client, api_curl_route):
    """ Test if an invalid url is passed """
    response = api_client.post(api_curl_route, data={'url': 'I am invalid'})
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == 'Please provide a valid url as a parameter: curl -d "url=<insert_url>"  ' \
                            'http://127.0.0.1:8080/api/api_curl/'


def test_no_api_files(api_client, api_file_load_route):
    """ Test if no file is passed """
    response = api_client.post(api_file_load_route)
    response_data = response.get_json()
    assert response_data == 'Please provide a valid CSV file as a parameter: curl -i -X POST -F ' \
                            'urls=@<insert_filename>.csv http://127.0.0.1:8080/api/api_files/'


def test_valid_api_files(api_client, api_file_load_route):
    """ Test if a valid (csv) file is passed """
    dataString = ""
    csvPath = os.path.abspath(os.curdir) + '/tests/test_data/test_urls.csv'
    with open(csvPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if len(row) > 0:
                dataString = dataString + row[0] + '\n'
    data = bytes(dataString, 'utf-8')
    response = api_client.post(api_file_load_route, data={'urls': (io.BytesIO(data), csvPath)})
    response_data = response.get_json()

    assert 'http://yournews10.com/' in response_data.keys()
    assert 'https://www.youtube.com/' in response_data.keys()
    assert 'https://www.google.ca/' in response_data.keys()

    url_result_1 = response_data['http://yournews10.com/']
    assert 'message' in url_result_1
    assert 'result' in url_result_1
    assert 'url' in url_result_1.get('result')
    assert 'confidence_score' in url_result_1.get('result')
    assert 'confidence_score' in url_result_1.get('result')
    assert 'features' in url_result_1.get('result')
    assert 'domain' in url_result_1.get('result')
    assert 'model' in url_result_1.get('result')

    url_result_2 = response_data['https://www.youtube.com/']
    assert 'message' in url_result_2
    assert 'result' in url_result_2
    assert 'url' in url_result_2.get('result')
    assert 'confidence_score' in url_result_2.get('result')
    assert 'confidence_score' in url_result_2.get('result')
    assert 'features' in url_result_2.get('result')
    assert 'domain' in url_result_2.get('result')
    assert 'model' in url_result_2.get('result')

    url_result_3 = response_data['https://www.google.ca/']
    assert 'message' in url_result_3
    assert 'result' in url_result_3
    assert 'url' in url_result_3.get('result')
    assert 'confidence_score' in url_result_3.get('result')
    assert 'confidence_score' in url_result_3.get('result')
    assert 'features' in url_result_3.get('result')
    assert 'domain' in url_result_3.get('result')
    assert 'model' in url_result_3.get('result')


def test_invalid_api_files(api_client, api_file_load_route):
    """ Test if an invalid file is passed """
    response = api_client.post(api_file_load_route,
                               data={'urls': (io.BytesIO(b'I am not a csv file'), 'test_urls.txt')})
    response_data = response.get_json()
    assert response_data == 'Please provide a CSV file containing URLs'
