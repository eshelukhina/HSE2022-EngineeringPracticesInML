import matplotlib.pyplot as plt

from swm.dataset.dataset import Dataset
from swm.svm.kernel_svm import KernelSVM
from swm.svm.linear_svm import LinearSVM
from swm.visualize.visualizer import Visualizer


class Model():
    def __init__(self, svm_type='Linear', c=1, kernal_args=None, dataset_moons=False):
        if svm_type == 'Linear':
            self.svm = LinearSVM(c)
        elif svm_type == 'Polynomial':
            self.svm = KernelSVM(c, svm_type, kernal_args)
        elif svm_type == 'Gaussian':
            self.svm = KernelSVM(c, svm_type, kernal_args)
        else:
            raise AttributeError()
        self.dataset = Dataset(dataset_moons)
        self.svm.fit(self.dataset.X, self.dataset.y)

    def visualize(self):
        Visualizer.visualize(self.svm, self.dataset.X, self.dataset.y)
        plt.show()
