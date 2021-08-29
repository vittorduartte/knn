from typing import List


def get_response(neighbors: List[dict]):
    labels = []
    ranking = {}
    for instance in neighbors:
        if instance['classe'] in labels:
            label = instance['classe']
            ranking[label] += 1
        else:
            label = instance['classe']
            ranking[label] = 1
            labels.append(label)
    
    return sorted(ranking.items())
