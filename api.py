import json
from flask import Flask, jsonify, request
from src.models.predict_model import predict_model
import logging
import os

if not os.path.exists(f'{os.path.expanduser("~")}/logs'):
    os.mkdir(f'{os.path.expanduser("~")}/logs')

logging.basicConfig(filename=f'{os.path.expanduser("~")}/logs/build.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

app = Flask(__name__) 
WrongFileFormat = 'Please provide a CSV file containing URLs'
CSVNotFoundError = 'Please provide a valid CSV file as a parameter: curl -i -X POST -F ' \
                  'urls=@<insert_filename>.csv http://127.0.0.1:8080/api/api_files/'
WrongUrlFormat = 'Please provide a valid url as a parameter: curl -d "url=<insert_url>"  ' \
                 'http://127.0.0.1:8080/api/api_curl/'
URLNotFoundError = 'Please provide a url as a -d parameter: curl -d "url=<insert_url>"  ' \
                   'http://127.0.0.1:8080/api/api_curl/'

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

@app.route(config['data']['api']['root_route'], methods=['GET'])
def api():
    return jsonify({'message': 'Welcome to Phishing Detection App', 'possible routes': '/api/api_curl/ ; /api/api_files/'})

@app.route(config['data']['api']['curl_route'], methods=['POST'])
def api_curl():
    """
     To access the API through CURL from command line run:
     curl -d "url=<insert_url>"  http://127.0.0.1:8080/api/api_curl/

     Returns: a dictionary of prediction results

    """
    logger = logging.getLogger(__name__)
    url = request.form.get('url')

    if not url:
        return jsonify(URLNotFoundError)
    elif ' ' in url:
        return jsonify(WrongUrlFormat)

    result = get_prediction_result(url)
    logger.info(result)
    return result


@app.route(config['data']['api']['file_load_route'], methods=["GET", "POST"])
def api_files():
    """
     To access the API through CURL from command line run:
     curl -i -X POST -F urls=@<insert_filename>.csv http://127.0.0.1:8080/api/api_files/

     Returns: a dictionary of prediction results

    """
    logger = logging.getLogger(__name__)
    ALLOWED_EXTENSIONS = {'csv'}

    try:
        file = request.files['urls']

        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS):
            return jsonify(WrongFileFormat)

        reader = str.splitlines(file.read().decode("utf-8"))
        urls = []
        for row in reader:
            urls.append(row)

        total_results = {}
        logger.info("Processing urls...")
        for url in urls:
            result = get_prediction_result(url)
            logger.info(result)
            total_results[url] = result
        return total_results
    except KeyError:
        return jsonify(CSVNotFoundError)


def get_prediction_result(url):
    """
    :param url: string
    :return: a dictionary containing the message and prediction result
    """
    result = predict_model(url)

    if (result['prediction_score'] == config['data']['api']['predicted_label'] and
            result['prediction_score'] >= config['data']['api']['confidence_score']):
        prediction = "malicious"
    else:
        prediction = "benign"

    message = "Phishy has detected that this URL is {}".format(prediction)

    return {"message": message, "result": result}


if __name__ == "__main__":
    app.run(debug=False, port=8080)
