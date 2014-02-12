import re

training_file = 'data/train.csv'
test_file = 'data/test.csv'
features_count = 100000

class Data:

    @classmethod
    def train(self, limit=None):
        features, targets = self.labels_and_features(limit)
        data = []
        for f in features:
            print f
            data.append(self.features_array(f))
        return data, targets

    @classmethod
    def labels_and_features(self, limit=None):
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
            features = line[start_of_features_index:]

            targets.append(labels)
            data.append(features)
        f.close()
        return data, targets

    @classmethod
    def lines(self, filepath, limit):
        f = file(filepath, 'r')
        if limit:
            lines = f.readlines()[1:limit] # start at 1 to strip the header
        else:
            lines = f.readlines()[1:] # start at 1 to strip the header
        lines = [re.sub('\n', '', line) for line in lines]
        return f, lines

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

if __name__ == "__main__":
    data, targets = Data.train(limit=3)
    print targets
    print data[0]
