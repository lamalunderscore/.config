from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import pandas as pd
from multi_linear_regression import MultiLinearRegression
from model_saver import ModelSaver
from regression_plotter import RegressionPlotter

if __name__=="__main__":
    data = load_diabetes()
    diabetes_data = pd.DataFrame(data.data, columns = data.feature_names)
    y = pd.DataFrame(data.target)
    sklear = LinearRegression().fit(diabetes_data, y)

#our model
    model = MultiLinearRegression()
    model.train(diabetes_data, y)
    predict_model = model.predict(diabetes_data)
    loss_ = data.target - sklear.predict(diabetes_data).flatten()
    loss = data.target-predict_model
    mse_ = sum((loss_**2)/len(loss_))
    mse = sum((loss**2)/len(loss))
    print("MSE: ", mse)
    print("Predicted value by our implementation: ", predict_model[0])

    saver = ModelSaver('json')
    filename = "saving_file.sav"
    saver.save_parameters(filename, model)
    new_model = MultiLinearRegression()
    saver.load_parameters(filename, new_model)

    plotter = RegressionPlotter()

    #plotter.plot(new_model)
    #plotter.plot_all(new_model)

    print("Predicted value by model with imported parameters: ",new_model.predict(diabetes_data)[0])


    
    