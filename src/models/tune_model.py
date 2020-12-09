import src.models.model_utils as model_utils
import pandas as pd
import multiprocessing
import time
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import csv

df = pd.read_csv('data/processed/final_processed_with_features.csv')
y = model_utils.load_labels_for_training(df)
x = model_utils.load_data(df)

def tune_random_forest(params):
    """ Tuning function for automating how we test the performance of our random forest model
        by adjusting the model's parameters
        
        Param: params is a list of paramters [n,c,d] where:
            n is the n_estimators (# trees)
            c is the criterion (either 'gini' or 'entropy')
            d is the max_depth (of each tree)
    """
    n = params[0]
    c = params[1]
    d = params[2]
    
    start = time.time()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    clf = RandomForestClassifier(n_estimators=n, criterion=c, max_depth=d)
    clf.fit(x_train, y_train.values.ravel())
    y_pred = clf.predict(x_test)
    
    accuracy = metrics.accuracy_score(y_test, y_pred.round())
    f1score = metrics.f1_score(y_test, y_pred.round())
    recall = metrics.recall_score(y_test, y_pred.round())
    precision = metrics.precision_score(y_test, y_pred.round())

    stop = time.time()

    total_runtime = str(stop - start)
    entry = [n,c,d,accuracy,f1score,recall,precision,total_runtime]
    return entry

if __name__ == "__main__":
    """ Run the tests/experiments using the tuning function and save the results in a csv """

    data = []
    columns = ["n_estimators", "criterion", "max_depth", "accuracy", "f1score", "recall", "precision", "exectime"]
    data.append(columns)

    inputs = []

    # adjusted n_estimators (# trees) classifiers
    for n in range(95,106):
        inputs.append([n,'gini',None])
        
    # adjusted criterion classfiers
    inputs.append([100,'gini',None])
    inputs.append([100,'entropy',None])

    # adjusted max_depth classifiers
    for d in range(1,11):
        inputs.append([100,'gini',d])

    print("Running experiments...")

    # run model experiments in parallel to reduce runtimes
    pool = multiprocessing.Pool()
    results = pool.map(tune_random_forest, inputs)
    pool.close()

    # save the results
    for result in results:
        data.append(result)
    file = open('tune_model_data.csv', 'w')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Writing complete")
