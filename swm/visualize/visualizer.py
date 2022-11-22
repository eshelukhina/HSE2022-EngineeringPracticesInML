import matplotlib.pyplot as plt
import numpy as np


class Visualizer():

    @staticmethod
    def visualize(clf, X, y):
        x_min, x_max = X[:, 0].min(), X[:, 0].max()
        y_min, y_max = X[:, 1].min(), X[:, 1].max()
        x_border = (x_max - x_min) / 20 + 1.0e-3
        x_h = (x_max - x_min + 2 * x_border) / 200
        y_border = (y_max - y_min) / 20 + 1.0e-3
        y_h = (y_max - y_min + 2 * y_border) / 200

        cm = plt.cm.Spectral

        xx, yy = np.meshgrid(np.arange(x_min - x_border, x_max + x_border, x_h),
                             np.arange(y_min - y_border, y_max + y_border, y_h))
        mesh = np.c_[xx.ravel(), yy.ravel()]

        z_class = clf.predict(mesh).reshape(xx.shape)

        # Put the result into a color plot
        plt.figure(1, figsize=(8, 8))
        plt.pcolormesh(xx, yy, z_class, cmap=cm, alpha=0.3, shading='gouraud')

        # Plot hyperplane and margin
        z_dist = clf.decision_function(mesh).reshape(xx.shape)
        plt.contour(xx, yy, z_dist, [0.0], colors='black')
        plt.contour(xx, yy, z_dist, [-1.0, 1.0], colors='black', linestyles='dashed')

        # Plot also the training points
        y_pred = clf.predict(X)

        ind_support = []
        ind_correct = []
        ind_incorrect = []
        for i in range(len(y)):
            if i in clf.support:
                ind_support.append(i)
            elif y[i] == y_pred[i]:
                ind_correct.append(i)
            else:
                ind_incorrect.append(i)

        plt.scatter(X[ind_correct, 0], X[ind_correct, 1], c=y[ind_correct], cmap=cm, alpha=1., edgecolor='black',
                    linewidth=.8)
        plt.scatter(X[ind_incorrect, 0], X[ind_incorrect, 1], c=y[ind_incorrect], cmap=cm, alpha=1., marker='*',
                    s=50, edgecolor='black', linewidth=.8)
        plt.scatter(X[ind_support, 0], X[ind_support, 1], c=y[ind_support], cmap=cm, alpha=1., edgecolor='yellow',
                    linewidths=1.,
                    s=40)

        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.tight_layout()
