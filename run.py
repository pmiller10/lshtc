from data import CompressedData
from models.classifier import Classifier
from sklearn.linear_model import LogisticRegression
from score import score
import time
import sys

limit = int(sys.argv[1])
data, targets = CompressedData.data(limit=limit)
tr_data, tr_targets = data[:limit/2], targets[:limit/2]
cv_data, cv_targets = data[limit/2:], targets[limit/2:]

logistic = Classifier(LogisticRegression())
start = time.time()
logistic.train(tr_data, tr_targets) 
print 'duration ', time.time() - start

preds = [logistic.predict(c) for c in cv_data]
print score(preds, cv_targets)
