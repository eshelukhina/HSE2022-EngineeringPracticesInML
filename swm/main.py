from swm.model.model_svm import Model


def start_experiments():
    model1 = Model(svm_type="Linear", c=1, dataset_moons=True)
    model1.visualize()

    # model2 = Model(svm_type="Linear", c=1, dataset_moons=False)
    # model2.visualize()
    #
    # model3 = Model(svm_type="Polynomial", c=1,
    #                dataset_moons=True, kernal_args=[1, 3])
    # model3.visualize()
    #
    # model4 = Model(svm_type="Polynomial", c=1,
    #                dataset_moons=False, kernal_args=[1, 3])
    # model4.visualize()
    #
    # model5 = Model(svm_type="Gaussian", c=1,
    #                dataset_moons=True, kernal_args=[0.4])
    # model5.visualize()
    #
    # model6 = Model(svm_type="Gaussian", c=1,
    #                dataset_moons=False, kernal_args=[0.4])
    # model6.visualize()
    #
    # model7 = Model(svm_type="Polynomial", c=1,
    #                dataset_moons=True, kernal_args=[1, 3])
    # model7.visualize()
    #
    # model8 = Model(
    #     svm_type="Polynomial", c=1, dataset_moons=True, kernal_args=[1000, 3],
    # )
    # model8.visualize()
    #
    # model9 = Model(svm_type="Polynomial", c=1,
    #                dataset_moons=True, kernal_args=[1, 15])
    # model9.visualize()
    #
    # model10 = Model(svm_type="Gaussian", c=1,
    #                 dataset_moons=False, kernal_args=[0.5])
    # model10.visualize()
    #
    # model11 = Model(svm_type="Gaussian", c=1,
    #                 dataset_moons=False, kernal_args=[0.1])
    # model11.visualize()
    #
    # model12 = Model(svm_type="Gaussian", c=1,
    #                 dataset_moons=False, kernal_args=[2])
    # model12.visualize()


if __name__ == "__main__":
    start_experiments()
