import sys,pdb
import time
sys.path.append('/home/ubuntu')
from kaggle.process.vector import VectorSpace
from lshtc.data import RawData

start = time.time()
tokens = 2100000
words = [str(i) for i in range(100000)]
vs = VectorSpace(words)
data, targets = RawData.raw_training_data(100)
f = file('training_compressed_100.csv', 'w+')
for i,doc in enumerate(data):
    t = targets[i]
    doc = vs.vector(doc)
    doc = list(doc)
    doc = [str(i) for i in doc]
    doc = ','.join(doc) + "\n"
    pdb.set_trace()
    doc = ','.join(t) + "\t" + doc # prepend targets
    f.write(str(doc))
f.close()
print 'duration: ', time.time() - start
