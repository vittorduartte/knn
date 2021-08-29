from typing import List
from typing import Optional
from sklearn.model_selection import KFold, RepeatedKFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import LeaveOneOut

def kFold(dataset: List[dict], n_splits: int = 2):

    kf = KFold(n_splits=n_splits)
    kf_dataset = []

    for split in kf.split(dataset):
        kf_dataset.append(tuple(split))

    return kf_dataset


def repeatedKFold(dataset: List[dict], n_splits: int = 2, n_repeats: int = 2, random_state=93578473):

    rkf = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    rkf_dataset = []

    for split in rkf.split(dataset):
        rkf_dataset.append(tuple(split))

    return rkf_dataset

def leaveOneOut(dataset: List[dict]):
    
    loo = LeaveOneOut()
    loo_dataset = []

    for split in loo.split(dataset):
        loo_dataset.append(tuple(split))
    
    return loo_dataset

def indexToData(indexset: List, dataset: List[dict]):
    data = []
    for dataset_ in indexset:
        aux_dataset = {}
        aux_dataset["train"] = [dataset[index] for index in dataset_[0]]
        aux_dataset["test"] = [dataset[index] for index in dataset_[1]]
        data.append(aux_dataset)

    return data
