import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from multi_linear_regression import MultiLinearRegression

class RegressionPlotter:
    def __init__(self, data:pd.DataFrame, target:pd.DataFrame) -> None:
        self.data = data
        self.target = target
        if len(target) != len(data):
            raise ValueError("Data and target do not share the same sample size.")
    
    def plot(self, model:"MultiLinearRegression") -> None:
        """
        This function is used to plot the coefficients of a model in either 2D or 3D depending in the number of coefficients.   

        :model:Any machine learning model: Any machine learning model could be used here, we use Multi Linear Regression just to give an example.
        :raises AttributeError: In the case the model does not support getting the slope ane the intercept.
        """
        try:
            slope = model.get_slope()
            intercept = model.get_intercept()
        except AttributeError:
            print("Specified model does not support necessary getter functions.")

        num_coefficients=len(slope)
        #if len(data)
        if num_coefficients == 1:
            plt.scatter(self.data, self.target, label = "Data")
            plt.axline((0, intercept[0]), slope=slope[0][0], label = "Regression Line", color = 'yellow')
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(range(10), range(10))
            Z = X*slope[0] + Y*slope[1] + intercept
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            plt.zlabel("Data")
            ax.plot_surface(X, Y, Z)
            ax.scatter3D(self.data[0], self.data[1], self.target, color = "green", label = "Prediction")
        plt.ylim(0,)
        plt.xlim(left = 0)
        plt.show()

    def plot_all(self, model:"MultiLinearRegression") -> None:
        """
        This function is used to generate subplots of each coefficient of a given model.

        :model:Any machine learning model: Any machine learning model could be used here, we use Multi Linear Regression just to give an example.
        :raises AttributeError: In the case the model does not support getting the slope and the intercept.
        """
        try:
            slope = model.get_slope()
            intercept = model.get_intercept()
        except AttributeError:
            print("Specified model does not support saving parameters.")

        num_coefficients=len(slope)
        plt.figure(figsize=(20, 8))
        for i in range(num_coefficients):
            ax = plt.subplot(int(np.sqrt(num_coefficients))+1, int(np.sqrt(num_coefficients))+1, i+1)
            plt.axline((0, intercept[0]), slope=slope[i][0], label=('Prediction'))
            plt.scatter(self.data[i], self.target, label = "Data")
            plt.xlabel("Data")
            plt.xlabel("Feature " + str(i+1))
            #plt.ylim(0.9*intercept, 1.1*intercept)
            plt.xlim(left=0)
            ax.legend()
        plt.legend()
        plt.show()

if __name__=="__main__":
    model = MultiLinearRegression()
    y = pd.DataFrame(np.array([1, 2, 3, 4, 5, 6]))
    data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))
    #data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))
    #data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))

    model.train(data, y)
    model.predict(data)
    plotter = RegressionPlotter(data, y)
    plotter.plot_all(model)
    slope = model.get_slope()
    intercept = model.get_intercept()
    print(slope)
    print(intercept)