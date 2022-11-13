from typing import NoReturn

import numpy as np
from cvxopt import matrix, solvers


# Линейный SVM.
#
# Методы:
# `fit(X, y)` - обучает SVM, решая задачу оптимизации при помощи `cvxopt.solvers.qp`
#
# `decision_function(X)` - возвращает значение решающей функции (т.е. то число, от которого берем знак с целью узнать класс)
#
# Поля:
# `support` - индексы опорных элементов
class LinearSVM:
    def __init__(self, C: float):
        self.C = C
        self.support = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> NoReturn:
        samples, features = X.shape

        y = y.reshape(-1, 1)

        solution = np.array(solvers.qp(
            matrix(np.block([
                [np.eye(samples), np.zeros((samples, 3))],
                [np.zeros((3, samples)), np.zeros((3, 3))]
            ])),
            matrix(np.block([
                np.zeros(3),
                np.ones(samples) * self.C
            ])),
            matrix(np.block([
                [np.zeros((samples, features)), np.zeros((samples, 1)), -np.eye(samples)],
                [-y * X, -y, -np.eye(samples)]
            ])),
            matrix(np.block([
                [np.zeros((samples, 1))],
                [-np.ones((samples, 1))]
            ]))
        )['x']).reshape(samples + 3)

        self.weights = solution[:features]
        self.bias = solution[features]

        self.support = [i for i in range(len(solution[features + 1:]))
                        if solution[features + 1:][i] > 1e-4]

    def decision_function(self, X: np.ndarray) -> np.ndarray:
        return np.dot(X, self.weights) + self.bias

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.sign(self.decision_function(X))
