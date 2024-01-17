import numpy as np
from sklearn.datasets import load_iris
from src.multi_linear_regression import MultiLinearRegression
from src.model_saver import ModelSaver

if __name__ == "__main__":
    y = np.array([1, 2, 3, 4, 5, 6])

    data = load_iris()
    X = data.data[:, :2]
    data = np.array(
        [[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]
    )
    print(X.shape)
    print(data.shape)

    model = MultiLinearRegression()
    model.train(data, y)
    print(model.slope)
    print(model.intercept)
    print(model.parameters)
    predict_model = model.predict(data)

    # y_loss = y.to_numpy().flatten()
    # loss = y_loss - predict_model
    # mse = sum((loss**2) / len(loss))
    # print("MSE: ", mse)
    # print("Predicted value by our implementation: ", predict_model[0])

    # saver = ModelSaver("pickle")
    # filename = "saving_file.sav"
    # saver.save_parameters(filename, model)
    # new_model = MultiLinearRegression()
    # saver.load_parameters(filename, new_model)

    # print(
    #     "Predicted value by model with imported parameters: ",
    #     new_model.predict(data)[0],
    # )
