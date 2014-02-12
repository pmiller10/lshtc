def precision(preds, targets):
    true_positives = float(len([prediction for prediction in preds if prediction in targets]))
    false_positives = len(preds) - true_positives
    return true_positives/(true_positives+false_positives)

def recall(preds, targets):
    true_positives = float(len([prediction for prediction in preds if prediction in targets]))
    false_negatives = len([target for target in targets if target not in preds])
    return true_positives/(true_positives+false_negatives)

def f1(preds, targets):
    p = precision(preds, targets)
    r = recall(preds, targets)
    if p+r == 0:
        return 0
    else:
        return (2 * p * r)/(p + r)

def score(all_preds, all_targets):
    scores = []
    for i,preds in enumerate(all_preds):
        targets = all_targets[i]
        scores.append(f1(targets, preds))
    return sum(scores)/float(len(scores))

if __name__ == "__main__":
    print precision([1,2,4], [2,3,4,5,6])
    print recall([1,2,4], [2,3,4,5,6])
    print f1([1,2,4], [2,3,4,5,6])
    print score([[1,2,4]], [[2,3,4,5,6]])
