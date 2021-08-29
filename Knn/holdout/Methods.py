import csv
import random
from typing import Optional
from typing import List

def load_dataset(dataset: List[dict], training_lenght: float = 0.7):

    training_set = []
    test_set = []

    for _ in range(200):
        random.shuffle(dataset)

    for instance in dataset:
        instance["comprimento_sepala"] = float(instance["comprimento_sepala"])
        instance["largura_sepala"] = float(instance["largura_sepala"])
        instance["comprimento_petala"] = float(instance["comprimento_petala"])
        instance["largura_petala"] = float(instance["largura_petala"])

    for instance in dataset[0:int((len(dataset)) * training_lenght)]:
        training_set.append(instance)

    for instance in dataset[int((len(dataset)) * training_lenght):(len(dataset))]:
        test_set.append(instance)

    return {"train": training_set, "test": test_set}
