from typing import List, NoReturn

import numpy as np
from cvxopt import matrix, solvers


# kernel SVM
#
# Описание
# fit(X, y) - обучает kernel SVM, решая задачу оптимизации при помощи cvxopt.solvers.qp
#
# decision_function(X) - возвращает значение решающей функции (т.е. то число, от которого берем знак с целью узнать класс)
#
# Конструктор
# kernel - ядро-функция
class KernelSVM:
    def __init__(self, c: float, svm_type: str, kernal_args: List):
        if svm_type == "Polynomial":
            self.kernel = KernelSVM.get_polynomial_kernel(*kernal_args)
        elif svm_type == "Gaussian":
            self.kernel = KernelSVM.get_gaussian_kernel(*kernal_args)
        else:
            raise AttributeError()
        self.C = c
        self.support = None

    @staticmethod
    def get_polynomial_kernel(c=1, power=2):
        "Возвращает полиномиальное ядро с заданной константой и степенью"
        return lambda a, b: (c + a @ b.T) ** power

    @staticmethod
    def get_gaussian_kernel(sigma=1.0):
        "Возвращает ядро Гаусса с заданным коэффицинтом сигма"
        return lambda a, b: np.exp(-sigma * np.linalg.norm(b - a) ** 2)

    def fit(self, X: np.ndarray, y: np.ndarray) -> NoReturn:
        samples, _ = X.shape

        K = np.zeros((samples, samples))
        for i in range(samples):
            for j in range(samples):
                K[i, j] = self.kernel(X[i], X[j])

        self.alpha = np.ravel(
            solvers.qp(
                matrix(np.outer(y, y) * K),
                matrix(-np.ones((samples, 1))),
                matrix(np.block([[np.eye(samples)], [-np.eye(samples)]])),
                matrix(np.block([np.ones(samples) * self.C, np.zeros(samples)])),
                matrix(y.astype("float"), (1, samples)),
                matrix(0.0),
            )["x"]
        )

        self.support = np.arange(samples)[self.alpha > 1e-4]
        self.support_X = X[self.support]
        self.support_y = y[self.support]
        self.alpha = self.alpha[self.support]

        self.bias = np.mean(
            self.support_y
            - np.sum(
                self.alpha * self.support_y * K[:, self.support][self.support, :],
                axis=1,
            )
        )

    def decision_function(self, X: np.ndarray) -> np.ndarray:
        def helper(x):
            s = 0
            for alpha, support_y, support_X in zip(
                self.alpha, self.support_y, self.support_X
            ):
                s += alpha * support_y * self.kernel(x, support_X)
            return s

        return np.apply_along_axis(helper, 1, X) + self.bias

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.sign(self.decision_function(X))
