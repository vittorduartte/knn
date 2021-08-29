import csv
import random
from typing import Optional
from typing import List

def load(path: str, field_names: List[str] = []):

    with open(path, "rt") as file:
        data = csv.DictReader(file, delimiter=",")
        data.fieldnames = field_names
        dataset = list(data)

    return dataset
