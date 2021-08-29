import math
from typing import Optional
from typing import List


def euclidean_distance(instance_1: dict, instance_2: dict):
    distance = pow((instance_1["comprimento_sepala"] - instance_2["comprimento_sepala"]), 2)
    distance += pow((instance_1["largura_sepala"] - instance_2["largura_sepala"]), 2)
    distance += pow((instance_1["comprimento_petala"] - instance_2["comprimento_petala"]), 2)
    distance += pow((instance_1["largura_petala"] - instance_2["largura_petala"]), 2)
    return math.sqrt(distance)
