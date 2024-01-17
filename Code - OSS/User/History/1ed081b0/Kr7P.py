from sklearn.datasets import load_diabetes
import pandas as pd
from src.multi_linear_regression import MultiLinearRegression
from src.model_saver import ModelSaver
from src.regression_plotter import RegressionPlotter

if __name__=="__main__":
    data = load_diabetes()
    diabetes_data = pd.DataFrame(data.data, columns = data.feature_names)
    y = pd.DataFrame(data.target)

#our model
    model = MultiLinearRegression()
    model.train(diabetes_data, y)
    print("data: ", diabetes_data)
    print("y: ", y)
    print(diabetes_data.shape)
    print(y.shape)
    predict_model = model.predict(diabetes_data)
    loss = data.target-predict_model
    mse = sum((loss**2)/len(loss))
    print("MSE: ", mse)
    print("Predicted value by our implementation: ", predict_model[0])

    saver = ModelSaver('json')
    filename = "saving_file.sav"
    saver.save_parameters(filename, model)
    new_model = MultiLinearRegression()
    saver.load_parameters(filename, new_model)

    #plotter = RegressionPlotter()

    #plotter.plot(new_model)
    #plotter.plot_all(new_model)

    print("Predicted value by model with imported parameters: ",new_model.predict(diabetes_data)[0])


    
    