import numpy as np
import src.multi_linear_regression as m
from src.model_saver import ModelSaver

if __name__ == "__main__":
    y = np.array([1, 2, 3, 4, 5, 6])
    data = np.array(
        [[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]
    )

    model = m.RidgeRegression()
    model.train(data, y)
    predict_model = model.predict(data)
    print(model.mse(data, predict_model, y))
    print("Predicted value by our implementation: ", predict_model[0])

    saver = ModelSaver("pickle")
    filename = "saving_file.sav"
    saver.save_parameters(filename, model)
    new_model = m.RidgeRegression()
    saver.load_parameters(filename, new_model)

    # print(
    #     "Predicted value by model with imported parameters: ",
    #     new_model.predict(data)[0],
    # )
