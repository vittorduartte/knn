from typing import Optional
from typing import List
from ..similarity import Methods as similarity


def get_neighbors(training_set: List[dict], test_instance: dict, k: Optional[int] = 5):
    distances = []
    for instance in training_set:
        distance = similarity.euclidean_distance(test_instance, instance)
        instance["distance"] = distance
        distances.append(instance)
    distances = sorted(distances, key=lambda distance: distance["distance"])
    return distances[0:k]
