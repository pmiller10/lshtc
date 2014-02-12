from data import Data
from models.classifier import Classifier
from sklearn.linear_model import LogisticRegression
import time
import sys

limit = int(sys.argv[1])
data, targets = RawData.train(limit=limit)
tr_data, tr_targets = data[:limit/2], targets[:limit/2]
cv_data, cv_targets = data[limit/2:], targets[limit/2:]

logistic = Classifier(LogisticRegression())
start = time.time()
logistic.train(tr_data, tr_targets) 
print 'duration ', time.time() - start

for i,c in enumerate(cv_data):
    pred = logistic.predict(c)
    print pred in cv_targets[i]
    print pred, cv_targets[i]
    print "\n"
