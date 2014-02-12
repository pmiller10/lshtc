import re

training_file = 'data/train.csv'
test_file = 'data/test.csv'
features_count = 2100000
compressed = 'data/training_compressed_100.csv'
compressed = 'training_compressed_100.csv'

class Data:

    @classmethod
    def lines(self, filepath, limit):
        f = file(filepath, 'r')
        if limit:
            lines = f.readlines()[1:limit] # start at 1 to strip the header
        else:
            lines = f.readlines()[1:] # start at 1 to strip the header
        lines = [re.sub('\n', '', line) for line in lines]
        return f, lines

class RawData(Data):

    @classmethod
    def train(self, limit=None):
        features, targets = self.labels_and_features(training_file, limit)
        data = []
        for f in features:
            data.append(self.features_array(f))
        return data, targets

    @classmethod
    def raw_training_data(self, limit=None):
        return self.raw_data(training_file, limit)

    @classmethod
    def raw_data(self, filepath, limit=None):
        features, targets = self.labels_and_features(filepath, limit)
        documents = []
        for doc_features in features:
            document = []
            for pair in doc_features:
                f = pair.split(':')
                word, occurences = f[0], f[1]
                for i in range(int(occurences)):
                    document.append(word)
            documents.append(document)
        return documents, targets

    @classmethod
    def labels_and_features(self, filepath, limit=None):
        targets, data = [], []
        f, lines = self.lines(training_file, limit)
        for line in lines:
            line = line.split(' ')
            labels = []
            start_of_features_index = 0
            for l in line:
                if not re.match('.*:.*', l):
                    start_of_features_index += 1
                else:
                    break
            labels = line[:start_of_features_index]
            labels = [re.sub(',', '', label) for label in labels]
            features = line[start_of_features_index:]

            targets.append(labels)
            data.append(features)
        f.close()
        return data, targets

    @classmethod 
    def features_array(self, features):
        counts = [0] * features_count
        for pair in features:
            pair = pair.split(':')
            feature, count = int(pair[0]), int(pair[1])
            index = feature - 1 # so that feature number 1 gets indexed to 0
            if feature <= features_count:
                counts[index] = count
        return counts

class CompressedData(Data):

    @classmethod
    def data(self, limit=None):
        targets, data = [], []
        f, lines = self.lines(compressed, limit)
        for line in lines:
            line = line.split('\t')
            labels,features = line[0], line[1]
            labels = labels.split(',')
            features = features.split(',')
            features = [float(i) for i in features]
            targets.append(labels)
            data.append(features)
        f.close()
        return data, targets

if __name__ == "__main__":
    print Data.raw_training_data(10)
