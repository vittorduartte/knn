from typing import List


def get_accuracy(testSet: List, predictions: List):
    score = 0
    for x in range(len(testSet)):
        if testSet[x]['classe'] == predictions[x]:
            score += 1
    return score/float(len(testSet)) * 100
