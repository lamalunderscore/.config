import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from multi_linear_regression import MultiLinearRegression

class RegressionPlotter:
    def __init__(self, data:pd.DataFrame, target:pd.DataFrame) -> None:
        self.data = data
        self.target = target
        if len(target) != len(data):
            raise ValueError("Data and target do not share the same sample size.")
    
    def plot(self, model:object) -> None:
        """
        This function plots a regression line or plane depending on its number of coefficients.   

        :model:object: model to plot
        :raises AttributeError: if model does not suppot model.get_intercept() or model.get_slope()
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
            plt.axline((0, intercept), slope=slope[0], label = "Regression Line", color = 'yellow')
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(range(10), range(10))
            Z = X*slope[0] + Y*slope[1] + intercept
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            ax.plot_surface(X, Y, Z)
            ax.scatter3D(self.data[0], self.data[1], self.target, color = "green", label = "Prediction")
        plt.ylim(0,)
        plt.xlim(left = 0)
        plt.show()

    def plot_all(self, model:"MultiLinearRegression") -> None:
        """
        This function is used to generate subplots for each coefficient of a given model.

        :model:MultiLinearRegression: Model to plot.
        :raises AttributeError: if model does not suppot model.get_intercept() or model.get_slope()
        """
        try:
            slope = model.get_slope()
            intercept = model.get_intercept()
        except AttributeError:
            print("Specified model does not support necessary functions.")

        num_coefficients=len(slope)
        plt.figure(figsize=(20, 8))
        for i in range(num_coefficients):
            ax = plt.subplot(int(np.sqrt(num_coefficients))+1, int(np.sqrt(num_coefficients))+1, i+1)
            plt.axline((0, intercept), slope=slope[i], label=('Prediction'))
            plt.scatter(self.data[i], self.target, label = "Data")
            plt.ylabel("Data")
            plt.xlabel("Feature " + str(i+1))
            plt.xlim(left=0)
            ax.legend()
        plt.legend()
        plt.show()

