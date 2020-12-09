# Capstone-Phishy

Phishing Detection Using Machine Learning

Please find the Wiki Here: https://github.com/SEG2105-uottawa/capstone-phishy/wiki

## Contents
- [1 Project Setup](https://github.com/SEG2105-uottawa/capstone-phishy#1-project-setup)
  - [1.1 Using GitHub Repo](https://github.com/SEG2105-uottawa/capstone-phishy#11-using-github-repo)
    - [1.1.1 Installing requirements](https://github.com/SEG2105-uottawa/capstone-phishy#111-install-the-requirements)
    - [1.1.2 Build the project](https://github.com/SEG2105-uottawa/capstone-phishy#112-build-the-project)
  - [1.2 Using Docker](https://github.com/SEG2105-uottawa/capstone-phishy#12-using-docker)

- [2 Project Setup](https://github.com/SEG2105-uottawa/capstone-phishy#2-running-the-project)
  - [2.1 API](https://github.com/SEG2105-uottawa/capstone-phishy#21-api)
    - [2.1.1 Root path](https://github.com/SEG2105-uottawa/capstone-phishy#211-root-path---api)
    - [2.1.2 Predict single urls](https://github.com/SEG2105-uottawa/capstone-phishy#212-predict-single-urls---apiapi_curl)
    - [2.1.3 Batch upload a csv of urls](https://github.com/SEG2105-uottawa/capstone-phishy#213-batch-upload-a-csv-of-urls---apiapi_files)
  - [2.2 Processing and visualization using Kafka and ELK stack](https://github.com/SEG2105-uottawa/capstone-phishy#22-processing-and-visualization-using-kafka-and-elk-stack)
    - [2.2.1 Pre-requisites](https://github.com/SEG2105-uottawa/capstone-phishy#221-pre-requisites)
    - [2.2.2 Kafka](https://github.com/SEG2105-uottawa/capstone-phishy#222-kafka)
      - [2.2.2.1 Producer](https://github.com/SEG2105-uottawa/capstone-phishy#2221-producer)
      - [2.2.2.2 Consumer](https://github.com/SEG2105-uottawa/capstone-phishy#2222-consumer)
    - [2.2.3 ELK (Elasticsearch, Logstash, Kibana)](https://github.com/SEG2105-uottawa/capstone-phishy#223-elk-elasticsearch-logstash-kibana)
      - [2.2.3.1 Kibana index pattern](https://github.com/SEG2105-uottawa/capstone-phishy#2231-kibana-index-pattern)
      - [2.2.3.2 Import Kibana Dashboards](https://github.com/SEG2105-uottawa/capstone-phishy#2232-import-kibana-dashboards)
   - [2.3 Logger: Tracking logs using Filebeat and ELK](https://github.com/SEG2105-uottawa/capstone-phishy#23-logger-tracking-logs-using-filebeat-and-elk) 
- [3 Continuous Delivery](https://github.com/SEG2105-uottawa/capstone-phishy#5-continous-delivery)
- [4 Project Organization](https://github.com/SEG2105-uottawa/capstone-phishy#3-project-organization)
- [5 Further development](https://github.com/SEG2105-uottawa/capstone-phishy#4-further-development)
    - [5.1 Features](https://github.com/SEG2105-uottawa/capstone-phishy#41-features)
## 1. Project Setup
### 1.1. Using GitHub Repo
- Clone Git Repo in your local computer: `git clone https://github.com/SEG2105-uottawa/capstone-phishy.git`
- Go to the project directory (capstone-phishy)
#### 1.1.1. Install the requirements
- From the project's root directory, run: `pip3 install -r requirements.txt`
#### 1.1.1.1. Install service requirements
- Assuming that you have ELK (Elasticsearch, Logstash, Kibana) already pre-installed:
- From the project root, run the following in order to install filebeat and copy the provided configuration files into the appropriate directory:
```
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.10.0-amd64.deb
sudo dpkg -i filebeat-7.10.0-amd64.deb
sudo apt update -y && sudo apt upgrade -y
sudo apt install filebeat
```
#### 1.1.2. Build the project
- Get the project ready for prediction by running: `python3 build.py`
The project is now ready to be used to predict. Go to "Running the Project" section to learn how to use the Phishy software.

#### 1.2. Using Docker        
To pull using docker, start by ensuring the docker daemon is active (```sudo service docker start```), and in a command line of choice, type
```
docker login (proceed to login through CLI)
docker pull mahyargorji/capstone:development 
docker run -it mahyargorji/capstone
```
Doing this will load the project, and place you within a Python3 terminal. 
Run the following:
```
exec(open('api.py').read())
```
If you need to rebuild the project from the docker image, run the following in the Python3 terminal:
```
exec(open('build.py').read())
```
#### 1.3. Planned Changes:
- Change base image from python-slim to ubuntu


## 2. Running the Project
This project can be accessed 2 ways. 
### 2.1. API
One way is through the flask API. The API has two end-points.  Both can be accessed through curl.
First, start the API by running the following command from the project's root directory.
```
python3 api.py
```
The API is now ready to listen to the requests from either endpoints explained below.

#### 2.1.1. Root path - `/api/`
From console run:
```
curl http://127.0.0.1:8080/api/
```
You will receive the following message, showing the end points to get prediction for urls.
```
{"message":"Welcome to Phishing Detection App","possible routes":"/api/api_curl/ ; /api/api_files/"} 
```

#### 2.1.2. Predict single urls - `/api/api_curl/`
From console run:
```
    curl -d "url=<insert_url>"  http://127.0.0.1:8080/api/api_curl/
```
Note: Insert a URL for '<insert_url>'. Example:

```
    curl -d "url=https://www.google.com"  http://127.0.0.1:8080/api/api_curl/
```

The API must return the result as a list. Example:

```
{
    "message":"Phishy has detected that this URL is malicious",
    "result":{
        "confidence_score":0.61,
        "domain":"www.google.com",
        "features":{
            "avg_query_value_digit_count":0,"avg_query_value_length":0,"avg_query_value_letter_count":0,"avg_query_value_symbol_count":0,"avg_query_variable_digit_count":0,"avg_query_variable_length":0,"avg_query_variable_letter_count":0,"avg_query_vari
            able_symbol_count":0,"domain_delimiter_count":2,"domain_digit_count":0,"domain_digit_to_letter_ratio":0.0,"domain_letter_count":12,"domain_symbol_count":0,"file_ext_delimiter_count":0,"fi
            le_ext_digit_count":0,"file_ext_digit_to_letter_ratio":0,"file_ext_is_executable":0,"file_ext_letter_count":0,"file_ext_symbol_count":0,"fragment_delimiter_count":0,"fragment_digit_count"
            :0,"fragment_digit_to_letter_ratio":0,"fragment_letter_count":0,"fragment_symbol_count":0,"ip_in_domain":0,"ip_in_url":0,"max_query_value_length":0,"max_query_variable_length":0,"path_del
            imiter_count":0,"path_digit_count":0,"path_digit_to_letter_ratio":0,"path_letter_count":0,"path_symbol_count":0,"query_delimiter_count":0,"query_digit_count":0,"query_digit_to_letter_rati
            o":0,"query_letter_count":0,"query_symbol_count":0,"subdomain_in":1,"total_query_value_digit_count":0,"total_query_value_length":0,"total_query_value_symbol_count":0,"total_query_variable
            _digit_count":0,"total_query_variable_length":0,"total_query_variable_symbol_count":0,"url_delimiter_count":5,"url_digit_count":0,"url_digit_to_letter_ratio":0.0,"url_encodes_characters":
            0,"url_get_port":-1,"url_letter_count":17,"url_symbol_count":0,"url_uses_default_port_number":0,"url_uses_https":1
        },
        "model":"Random Forest",
        "prediction_score":1,
        "url":"https://www.google.com"
    }
}

```


#### 2.1.3. Batch upload a csv of urls - `/api/api_files/

```
curl -i -X POST -F urls=@<insert_filename>.csv http://127.0.0.1:8080/api/api_files/
```
Note: insert a csv file for `<insert_filename>.csv`. Example:

```
curl -i -X POST -F urls=@urls.csv http://127.0.0.1:8080/api/api_files/
```

```
{
    "http://bcaf.co/5v1l/,":{
        "message":"Phishy has detected that this URL is malicious",
        "result":{
            "confidence_score":0.73,
            "domain":"bcaf.co",
            "features":{
                "avg_query_value_digit_count":0,"avg_query_value_length":0,"avg_query_value_letter_count":0,"avg_query_value_symbol_count":0,"avg_query_variable_digit_count":0,"avg_query_variable_length":0,"avg_query_variable_letter_count"
                :0,"avg_query_variable_symbol_count":0,"domain_delimiter_count":1,"domain_digit_count":0,"domain_digit_to_letter_ratio":0.0,"domain_letter_count":6,"domain_symbol_count":0,"file_ext_delim
                iter_count":0,"file_ext_digit_count":0,"file_ext_digit_to_letter_ratio":0,"file_ext_is_executable":0,"file_ext_letter_count":0,"file_ext_symbol_count":0,"fragment_delimiter_count":0,"frag
                ment_digit_count":0,"fragment_digit_to_letter_ratio":0,"fragment_letter_count":0,"fragment_symbol_count":0,"ip_in_domain":0,"ip_in_url":0,"max_query_value_length":0,"max_query_variable_le
                ngth":0,"path_delimiter_count":3,"path_digit_count":2,"path_digit_to_letter_ratio":1.0,"path_letter_count":2,"path_symbol_count":0,"query_delimiter_count":0,"query_digit_count":0,"query_d
                igit_to_letter_ratio":0,"query_letter_count":0,"query_symbol_count":0,"subdomain_in":0,"total_query_value_digit_count":0,"total_query_value_length":0,"total_query_value_symbol_count":0,"t
                otal_query_variable_digit_count":0,"total_query_variable_length":0,"total_query_variable_symbol_count":0,"url_delimiter_count":7,"url_digit_count":2,"url_digit_to_letter_ratio":0.16666666
                666666666,"url_encodes_characters":0,"url_get_port":-1,"url_letter_count":12,"url_symbol_count":0,"url_uses_default_port_number":0,"url_uses_https":0
            },
            "model":"Random Forest",
            "prediction_score":1,
            "url":"http://bcaf.co/5v1l/,"
        }
    },
    "http://mobn.it/AX8jbE,":{
        "message":"Phishy has detected that this URL is benign",
        "result":{
            "confidence_score":0.92,
            "domain":"mobn.it",
            "features": {
                "avg_query_value_digit_count":0,"avg_query_value_length":0,"avg_query_value_letter_count":0,"avg_query_value_symbol_count":0,"avg_query_variable_digit_count":0,"avg_query_variable_leng
                th":0,"avg_query_variable_letter_count":0,"avg_query_variable_symbol_count":0,"domain_delimiter_count":1,"domain_digit_count":0,"domain_digit_to_letter_ratio":0.0,"domain_letter_count":6,
                "domain_symbol_count":0,"file_ext_delimiter_count":0,"file_ext_digit_count":0,"file_ext_digit_to_letter_ratio":0,"file_ext_is_executable":0,"file_ext_letter_count":0,"file_ext_symbol_coun
                t":0,"fragment_delimiter_count":0,"fragment_digit_count":0,"fragment_digit_to_letter_ratio":0,"fragment_letter_count":0,"fragment_symbol_count":0,"ip_in_domain":0,"ip_in_url":0,"max_query
                _value_length":0,"max_query_variable_length":0,"path_delimiter_count":2,"path_digit_count":1,"path_digit_to_letter_ratio":0.2,"path_letter_count":5,"path_symbol_count":0,"query_delimiter_
                count":0,"query_digit_count":0,"query_digit_to_letter_ratio":0,"query_letter_count":0,"query_symbol_count":0,"subdomain_in":0,"total_query_value_digit_count":0,"total_query_value_length":
                0,"total_query_value_symbol_count":0,"total_query_variable_digit_count":0,"total_query_variable_length":0,"total_query_variable_symbol_count":0,"url_delimiter_count":6,"url_digit_count":1
                ,"url_digit_to_letter_ratio":0.06666666666666667,"url_encodes_characters":0,"url_get_port":-1,"url_letter_count":15,"url_symbol_count":0,"url_uses_default_port_number":0,"url_uses_https":
                0
            },
            "model":"Random Forest",
            "prediction_score":0,
            "url":"http://mobn.it/AX8jbE,"
        }
    }
}
```

### 2.2. Processing and visualization using Kafka and ELK stack
#### 2.2.1. Pre-requisites
- You will need to have Zookeeper, Kafka, Elasticsearch, Kibana and Logstash installed and configured.
- Visit https://github.com/SEG2105-uottawa/capstone-phishy/wiki/Kafka-&-ELK:-installation-and-configuration-steps for 
more information on how to install these on your environment.

#### 2.2.2. Kafka
You can specify the Kafka server specification in `config.json` file as follows:
```
"kafka": {
    "bootstrap_servers": ["localhost:9092"],
    "api_version": [0, 10, 1],

    "producer": {
      "kafka_topic": "all_urls"
    },
    "consumer": {
      "kafka_topic_to_read_from": "all_urls",
      "kafka_topic_to_send_to": "malicious_urls",
      "group_id": "group_id",
      "enable_auto_commit": false,
      "auto_offset_reset": "earliest",
      "consumer_timeout_ms": 30000,
      "max_poll_interval_ms": 3600000
    },
    "predicted_label": 1,
    "confidence_score": 0.85
  },
```

#### 2.2.2.1. Producer
The purpose of the kafka producer is to bulk load urls into a kafka topic specified in the config file. 
The producer currently ingests the urls in `capstone-phishy\data\preprocessed.csv` file. 
Place your kafka topic in the producer's config:
```
"producer": {
      "kafka_topic": "all_urls"
    },
```
Note: the default topic is called `all_urls`. If you wish to send data to another topic, simply change the value. The
topic you specify doesn't need to have existed before. The producer creates the topic if it does not exist already in 
your environment.

##### Run Producer
From the project directory run:
```
python3 src/kafka/producer.py
```
The producer will start ingesting the urls from the csv and send them to the specified Kafka topic.

##### 2.2.2.2. Consumer
The purpose of the consumer is to read from a Kafka topic that ideally holds many URLs, run prediction on each urls,
and send the malicious labeled urls with a certain confidence score (specified in the config) to the second url that is 
also given in the config file.

Place your kafka topics in the consumer's config:

```
"consumer": {
      "kafka_topic_to_read_from": "all_urls",
      "kafka_topic_to_send_to": "malicious_urls",
      "group_id": "group_id",
      "enable_auto_commit": false,
      "auto_offset_reset": "earliest",
      "consumer_timeout_ms": 30000,
      "max_poll_interval_ms": 3600000
    },
    "predicted_label": 1,
    "confidence_score": 0.85
```
Note: `kafka_topic_to_read_from` is the kafka topics that holds all the urls. This topic could be the same topic 
specified for producer. `kafka_topic_to_send_to` is the second kafka topic that receives the malicious URLs.


##### Run Consumer
Important pre-requisite:
- If you want to be able to view your data in Kibana, you will need to have Elasticsearch, Kibana and Logstash running
 before running the consumer. For more info go to section `2.2.3. ELK (Elasticsearch, Logstash, Kibana)`.
  
From the project directory run:
```
python3 src/kafka/consumer.py
```
This will send the prediction result to the specified kafka topic. Example:
```
{
    "url": "https://dailym.ai/2PuqV8R", 
    "domain": "dailym.ai", 
    "model": "Random Forest", 
    "prediction_score": 1, 
    "confidence_score": 0.97,
    "features": {
        "url_delimiter_count": 5, "url_digit_count": 2, "url_letter_count": 18, "url_symbol_count": 0, "url_digit_to_letter_ratio": 0.1111111111111111, 
        "url_encodes_characters": 0, "url_uses_https": 1, "url_get_port": -1, "url_uses_default_port_number": 0, "ip_in_url": 0, "domain_delimiter_count": 1, 
        "domain_digit_count": 0, "domain_letter_count": 8, "domain_symbol_count": 0, "domain_digit_to_letter_ratio": 0.0, "subdomain_in": 0, "ip_in_domain": 0, 
        "path_delimiter_count": 1, "path_digit_count": 2, "path_letter_count": 5, "path_symbol_count": 0, "path_digit_to_letter_ratio": 0.4, "query_delimiter_count": 0, 
        "query_digit_count": 0, "query_letter_count": 0, "query_symbol_count": 0, "query_digit_to_letter_ratio": 0, "total_query_value_length": 0, "avg_query_value_length": 0, 
        "max_query_value_length": 0, "total_query_value_digit_count": 0, "avg_query_value_digit_count": 0, "avg_query_value_letter_count": 0, "total_query_value_symbol_count": 0, 
        "avg_query_value_symbol_count": 0, "total_query_variable_length": 0, "avg_query_variable_length": 0, "max_query_variable_length": 0, "total_query_variable_digit_count": 0, 
        "avg_query_variable_digit_count": 0, "avg_query_variable_letter_count": 0, "total_query_variable_symbol_count": 0, "avg_query_variable_symbol_count": 0, 
        "fragment_delimiter_count": 0, "fragment_digit_count": 0, "fragment_letter_count": 0, "fragment_symbol_count": 0, "fragment_digit_to_letter_ratio": 0, 
        "file_ext_delimiter_count": 0, "file_ext_digit_count": 0, "file_ext_letter_count": 0, "file_ext_symbol_count": 0, "file_ext_digit_to_letter_ratio": 0, "file_ext_is_executable": 0
    }
}
```

Tip: You can monitor the kafka topic as the consumer is running by executing the following command in a separate console:
```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic "<insert_kafka_topic>" --from-beginning
``` 

### 2.2.3. ELK (Elasticsearch, Logstash, Kibana)
- Follow https://github.com/SEG2105-uottawa/capstone-phishy/wiki/Kafka-&-ELK:-installation-and-configuration-steps for 
installation and configuration steps.
- Run Elasticsearch 
- Run Kibana
- Configure Logstash:

in the project directory, open `<capstone-phishy>/ext-config/logstash-malicious-url.conf`
```
input {
  kafka{
    bootstrap_servers => "localhost:9092"
    topics => ["malicious_urls"]
    codec => json {}
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "malicious_url"
  }
}

```
Place your Kafka and ES server specifications, as well as the kafka topic you gave consumer to send malicious URLs to. 

Copy the local config files to the `/etc/logstash/conf.d` (Assuming `/etc` directory is where your logstash lives)
```
sudo cp ~/capstone-phishy/ext-config/logstash-logs.conf /etc/logstash/conf.d
sudo cp ~/capstone-phishy/ext-config/logstash-malicious-url.conf /etc/logstash/conf.d
```
Since there are 2 config files, we have defined the pipelines in the `pipelines.yml` files:
```
- pipeline.id: malicious_url
  path.config: "/etc/logstash/conf.d/logstash-malicious-url.conf"
- pipeline.id: phishy_logs
  path.config: "/etc/logstash/conf.d/logstash-logs.conf"
```
Copy this file into the logstash directory as well:
```
sudo cp ~/capstone-phishy/ext-config/pipelines.yml /etc/logstash
```
- Run Logstash:
```
sudo /usr/share/logstash/bin/logstash --path.settings /etc/logstash
```
#### 2.2.3.1 Kibana index pattern
If you're ingesting data for the first time, you will need to create an index pattern for the data coming in.
The index pattern is set in your logstash config:
```
output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "malicious_url"
  }
``` 
Go to `http://localhost:5601/app/management/kibana/indexPatterns` in Kibana, and create the index pattern `malicious_url*`


#### 2.2.3.2 Import Kibana Dashboards

To view Phishy's Kibana dashboards, import the dashboard in `visualization/phishy_dashboard.ndjson`.
The import can be done from `http://localhost:5601/app/management/kibana/objects` in Kibana.

Note: `visualization/mappings.json` has been provided to show the field mappings for data in Kibana.

### 2.3 Logger: Tracking logs using Filebeat and ELK 
Assuming the following is true:
- you have already installed filebeat (see: step 1.1.1.1)
- you have capstone as a folder in your user home directory (~)
- you have ~/logs/ as a valid directory (if not, ```cd ~ && mkdir logs```)

First, go into ext-config/filebeat.yml. Next, uncomment and change line 28 to:
```-/home/<your local machine user account>/logs/build.log ```
If you do not know who your local machine user account is, type ```whoami``` in any terminal and record the output

Use the following line to copy the filebeat config and overwrite the existing one in the filebeat directory
```
sudo cp ~/capstone-phishy/ext-config/filebeat.yml /etc/filebeat/
```

Start the services (Please make sure the Logstash configuration has been done according to steps in `2.2.3. ELK (Elasticsearch, 
Logstash, Kibana)`)
```
sudo service docker start
sudo service elasticsearch start
sudo service filebeat start (OR: /usr/share/filebeat/bin/filebeat -e)
sudo /usr/share/logstash/bin/logstash
sudo service kibana start
```

You now can track your logs through the kibana dashboard (http://localhost:5601/)using the index specified in your 
logstash configuration file (default: "logs-phishy")
## 5. Continous Delivery
MLflow is used to keep track of the experiments when the `train_model.py` is ran as well as `predict_model.py`. 
To access the reports, enter `mlflow ui` from the project directory and you will be able to access the experiment 
data in `http://localhost:5000`. 


## 4. Project Organization


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    │                         
    ├── Dockerfile         <- Provides runnable instructions when the Docker container is ran on a different
    |                         docker location. Current entry point at train_model.py
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

## 5. Further development

### 5.1 Features

The complete list of features with their status can be found [here](https://github.com/SEG2105-uottawa/capstone-phishy/wiki/Features)

There are some incomplete features that were attempted but did not make it to the final code. Most of the issues were
regarding the runtime and processing the large amount of data. 

These methods are written in the `src/features/url_utils.py` under `#### Incomplete Features ####` and are left for
future developers of this project to tackle. 


--------
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
