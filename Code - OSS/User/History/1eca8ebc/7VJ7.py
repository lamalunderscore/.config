import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class RegressionPlotter:
    def __init__(self, data:pd.DataFrame=None, target:pd.DataFrame=None) -> None:
        '''
        This initialies data points for this instance to plot as a scatterplot in different functions.

        :param data:pandas.DataFrame: features to use
        :param target:pandas.DataFrame: truth values to use
        :raises AttributeError: if target and data are not the same sample size
        '''
        self._data = data
        self._target = target
        if len(self._target) != len(self._data):
            raise AttributeError("Data and target do not share the same sample size.")
    
    def plot(self, model:object) -> None:
        """
        This function plots a regression line or plane depending on its number of coefficients.   

        :param model:object: model to plot
        :raises AttributeError: if model does not suppot model.get_intercept() or model.get_slope()
        """
        try:
            slope = model.get_slope()
            intercept = model.get_intercept()
        except AttributeError:
            print("Specified model does not support necessary getter functions.")

        num_coefficients=len(slope)

        if num_coefficients == 1:
            plt.scatter(self._data, self._target, label = "Data")
            plt.axline((0, intercept), slope=slope[0], label = "Regression Line", color = 'orange')

        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(range(10), range(10))
            Z = X*slope[0] + Y*slope[1] + intercept
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            ax.plot_surface(X, Y, Z)
            ax.scatter3D(self._data.iloc[:,0], self._data.iloc[:,1], self._target, color = "orange", label = "Prediction")
        plt.show()

    def plot_all(self, model:"MultiLinearRegression") -> None:
        """
        This function is used to generate subplots for each coefficient of a given model.

        :model:MultiLinearRegression: Model to plot
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
            plt.axline((0, intercept), slope=slope[i], label=('Prediction'), color = 'orange')
            plt.scatter(self._data.iloc[:,0], self._target, label = "Data")
            plt.ylabel("Data")
            plt.xlabel("Feature " + str(i+1))
            ax.legend()
        plt.legend()
        plt.show()

