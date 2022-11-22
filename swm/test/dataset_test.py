from main.dataset.dataset import Dataset


def test_dataset_True():
    assert Dataset(True) is not None


def test_dataset_False():
    assert Dataset(False) is not None
