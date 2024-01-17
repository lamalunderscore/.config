import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes


class MultiLinearRegression:
    def __init__(self, default_slope:np.ndarray=None, default_intercept:float=None):
        """
        This initializes a class and sets necessary check values.

        :param default_slope:numpy.ndarray: default slope to use without training
        :param default_intercept:float: default slope to use without training
        """
        self._slope = default_slope
        self._intercept = default_intercept
    
    def set_params(self, parameters:np.array) -> None:
        """
        This sets the parameters to a given value.

        :param parameters:numpy.array: array of all coefficients to be set (intercept, slope)
        """
        self._set_intercept(parameters[0])
        self._set_slope(parameters[1:])
        return

    def _set_intercept(self, intercept:float) -> None:
        """
        This sets the intercept to a given value.

        :param intercept:float: intercept value to be set
        """
        self._intercept = intercept
        return

    def _set_slope(self, slope:np.array) -> None:
        """
        This sets the slope coefficients from a given array.

        :param slope:nump.array: slope coefficients to be set
        """
        self._slope = slope
        return

    def get_params(self) -> np.array:
        """
        This returns an array of the models parameters.

        :returns:numpy.array: all coefficients (intercept, slope)
        """
        parameters = np.insert(self._slope, 0, self._intercept)
        return parameters

    def get_slope(self) -> np.array:
        """
        This returns an array of the models slope coefficients.
        
        :returns:numpy.array: slope coefficients
        """
        return self._slope
        
    
    def get_intercept(self) -> float:
        """
        This returns the intercept value.

        :returns:float: intercept value
        """
        return self._intercept


    def train(self, X:pd.DataFrame, y:pd.DataFrame) -> None:
        """
        This trains (sets slope and intercept of) the model on the given data and targets.

        :param X:pandas.DataFrame: labeled continous data
        :param y:pandas.DataFrame: continous targets
        :raises TypeError: if the data or targets are not all numerical data
        :raises LinAlgError: if production matrix is not inversible
        :raises ValueError: if data and target do not have the same sample size
        """

        try:
            X.astype(float)
        except TypeError:
            print("The given data are not (fully) numeric.")

        try:
            y.astype(float)
        except TypeError:
            print("The given targets are not (fully) numeric.")

        if len(X) != len(y):
            raise ValueError("Data and target do not share the same sample size. (", len(X), ") !=  (", len(y), ")")

        X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))
        X_transpose = X_with_intercept.transpose()
        production = np.dot(X_transpose, X_with_intercept)

        try:
            inverse_production = np.linalg.inv(production)
        except LinAlgError:
            print("The production matrix is not invertible.")
        
        slope_product = np.dot(inverse_production, X_transpose)
        parameters = np.dot(slope_product, y)
        self._set_intercept(float(parameters[0][0]))
        self._set_slope(parameters[1:].flatten())

    def predict(self, X:pd.DataFrame) -> np.ndarray:
        """
        This predicts new values from data on the trained model.

        :param X:pandas.DataFrame: data to predict upon
        :raises ValueError: if the model has not been trained yet
        :raises ValueError: if the number of features in the data and the number of coefficients of the model are not the same
        :raises TypeError: if the given data are not all numerical
        """

        try:
            X.astype(float)
        except TypeError:
            print("The given data are not (fully) numeric.")

        intercept = self.get_intercept()
        slope = self.get_slope()

        if type(slope) == None:
            raise ValueError("The model does not have the slope parameter set yet. Please set it when initializing, or train the model first.")

        if type(intercept) == None:
            raise ValueError("The model does not have the intercept parameter set yet. Please set it when initializing, or train the model first.")


        if X.shape[1] != len(slope):
            raise ValueError("The number of features (", X.shape[1], ") does not fit the number of model coefficients (", len(slope), ").")
            
        X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))

        parameters = np.insert(self.get_slope(), 0, self.get_intercept())
        return np.dot(X_with_intercept, parameters)


if __name__=="__main__":
    model = MultiLinearRegression()
    y = pd.DataFrame(np.array([1, 2, 3, 4, 5, 6]))
    data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))
    #data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))
    #data = pd.DataFrame(np.array([[3, 2, 4], [5, 1, 7], [3, 5, 2], [1, 8, 2], [8, 6, 2], [3, 8, 5]]))

    model.train(data, y)
    print(model.predict(data)[0])
    print(type(model.get_slope()))
    print(type(model.get_intercept()))
