from sklearn.datasets import make_moons, make_blobs


class Dataset():

    def __init__(self, moons=False):
        if moons:
            self.X, self.y = make_moons(1000, noise=0.075, random_state=42)
            self.y = 2 * self.y - 1
            return
        self.X, self.y = make_blobs(1000, 2, centers=[[0, 0], [-4, 2], [3.5, -2.0], [3.5, 3.5]], random_state=42)
        self.y = 2 * (self.y % 2) - 1
