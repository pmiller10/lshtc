from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier

class Classifier:

    def __init__(self, model):
        self.model = model

    def train(self, data, targets):
        self.model.fit(data, targets)
    
    def predict(self, data):
        return self.model.predict(data)

if __name__ == "__main__":
    logistic = Classifier(LogisticRegression())
    logistic.train([[0.],[1.]], [0,1])
    print logistic.predict([1.])
