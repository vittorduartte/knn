import Knn.dataset.Methods as dataset
import Knn.holdout.Methods as holdout
import Knn.cross_validation.Methods as cross_validation
import Knn.similarity.Methods as similarity
import Knn.neighbors.Methods as neighbors
import Knn.response.Methods as response
import Knn.accuracy.Methods as accuracy


field_names = ['comprimento_sepala', 'largura_sepala',
               'comprimento_petala', 'largura_petala', 'classe']
dataset = dataset.load(path='./database/iris.data', field_names=field_names)


"""
KNN c/ Holdout
"""
holdout_dataset = holdout.load_dataset(dataset=dataset)

"""
Iteração para as predições e cálculo de acurácia do modelo
"""
holdout_predictions = []
for instance in holdout_dataset["test"]:
    neighbors_ = neighbors.get_neighbors(holdout_dataset["train"], instance, 3)
    result = response.get_response(neighbors_)
    holdout_predictions.append(result[0][0])
holdout_accuracy = accuracy.get_accuracy(holdout_dataset["test"], holdout_predictions)

print("Holdout Accuracy: %.3f" % holdout_accuracy)


"""
KNN c/ validação cruzada K-Fold
"""
kf_index = cross_validation.kFold(dataset, 3)
kf_accuracy = []

"""
Conversão de array de índices para lista de dados
"""
kf_dataset = cross_validation.indexToData(kf_index, dataset)

"""
Iteração para as predições e cálculo de acurácia do modelo
"""
for dataset_ in kf_dataset:
    kf_predictions = []
    for instance in dataset_["test"]:
        neighbors_ = neighbors.get_neighbors(dataset_["train"], instance, 3)
        result = response.get_response(neighbors_)
        kf_predictions.append(result[0][0])
    kf_accuracy.append(accuracy.get_accuracy(dataset_["test"], kf_predictions))
kf_accuracy = sum(kf_accuracy)/len(kf_accuracy)

print("K-Fold Accuracy: %.3f" % kf_accuracy)


"""
KNN c/ validação cruzada Repeated-K-Fold
"""
rkf_index = cross_validation.repeatedKFold(dataset=dataset, n_splits=5, n_repeats=5)
rkf_accuracy = []

"""
Conversão de array de índices para lista de dados de dicionário
com chave de train e test.
"""
rkf_dataset = cross_validation.indexToData(rkf_index, dataset)

"""
Iteração para as predições e cálculo de acurácia do modelo
"""
for dataset_ in rkf_dataset:
    rkf_predictions = []
    for instance in dataset_["test"]:
        neighbors_ = neighbors.get_neighbors(dataset_["train"], instance, 3)
        result = response.get_response(neighbors_)
        rkf_predictions.append(result[0][0])
    rkf_accuracy.append(accuracy.get_accuracy(dataset_["test"], rkf_predictions))
rkf_accuracy = sum(rkf_accuracy)/len(rkf_accuracy)

print("Repeated K-Fold Accuracy: %.3f" % rkf_accuracy)


"""
KNN c/ Leave One Out
"""
loo_index = cross_validation.leaveOneOut(dataset=dataset)
loo_accuracy = []

"""
Conversão de array de índices para lista de dados de dicionário
com chave de train e test.
"""
loo_dataset = cross_validation.indexToData(loo_index, dataset)

"""
Iteração para as predições e cálculo de acurácia do modelo
"""
for dataset_ in loo_dataset:
    loo_predictions = []
    for instance in dataset_["test"]:
        neighbors_ = neighbors.get_neighbors(dataset_["train"], instance, 3)
        result = response.get_response(neighbors_)
        loo_predictions.append(result[0][0])
    loo_accuracy.append(accuracy.get_accuracy(dataset_["test"], loo_predictions))
loo_accuracy = sum(loo_accuracy)/len(loo_accuracy)

print("Leave One Out Accuracy: %.3f" % loo_accuracy)