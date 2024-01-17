from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
from src.multi_linear_regression import MultiLinearRegression
from src.model_saver import ModelSaver
from src.regression_plotter import RegressionPlotter

if __name__=="__main__":
    data = load_diabetes()
    y = pd.DataFrame(data.target)
    data = pd.DataFrame(data.data, columns = data.feature_names)

    model = MultiLinearRegression()
    model.train(data, y)
    predict_model = model.predict(data)

    y_loss = y.to_numpy().flatten()
    loss = y_loss - predict_model
    mse = sum((loss**2)/len(loss))
    print("MSE: ", mse)
    print("Predicted value by our implementation: ", predict_model[0])

    saver = ModelSaver('json')
    filename = "saving_file.sav"
    saver.save_parameters(filename, model)
    new_model = MultiLinearRegression()
    saver.load_parameters(filename, new_model)

    plotter = RegressionPlotter()
    plotter.plot(new_model)
    plotter.plot_all(new_model)

    print("Predicted value by model with imported parameters: ",new_model.predict(data)[0])

     