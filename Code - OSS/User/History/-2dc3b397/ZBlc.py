import numpy as np
import logging
from abc import ABC, abstractmethod


class MlModel(ABC):
    @abstractmethod
    def train(self, data: np.ndarray, target: np.ndarray):
        pass

    @abstractmethod
    def predict(self, data: np.ndarray):
        pass

    @property
    @abstractmethod
    def parameters(self) -> np.ndarray:
        pass

    @parameters.getter
    @abstractmethod
    def parameters(self) -> np.ndarray:
        pass

    @parameters.setter
    @abstractmethod
    def parameters(self, parameters: np.ndarray) -> None:
        pass


class MultiLinearRegression(MlModel):
    def __init__(self):
        """
        This initializes a class and sets necessary check values.

        """
        self._slope = None
        self._intercept = None

    @property
    def intercept(self):
        return self._intercept

    @intercept.getter
    def intercept(self) -> float:
        """
        This returns the intercept value.

        :returns:float: intercept value
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        """
        This sets the intercept to a given value.

        :param intercept:float: intercept value to be set
        """
        self._intercept = intercept

    @property
    def slope(self):
        return self._slope

    @slope.getter
    def slope(self) -> np.array:
        """
        This returns an array of the models slope coefficients.

        :returns:numpy.array: slope coefficients
        """
        return self._slope

    @slope.setter
    def slope(self, slope: np.array) -> None:
        """
        This sets the slope coefficients from a given array.

        :param slope:nump.array: slope coefficients to be set
        """
        self._slope = slope

    @property
    def parameters(self):
        return

    @parameters.getter
    def parameters(self) -> np.array:
        """
        This returns an array of the models parameters.

        :returns:numpy.array: all coefficients (intercept, slope)
        """
        parameters = np.insert(self.slope, 0, self.intercept)
        return parameters

    @parameters.setter
    def parameters(self, parameters: np.array) -> None:
        """
        This sets the parameters to a given value.

        :param parameters:numpy.array: array of all
        coefficients to be set (intercept, slope)
        """
        self.intercept = parameters[0]
        self.slope = parameters[1:]
        return

    def mse(
        self, data: np.ndarray, prediction: np.ndarray, target: np.ndarray
    ) -> float:
        y_loss = target.flatten()
        loss = y_loss - prediction
        return sum((loss**2) / len(loss))

    def _check_numerical(self, array: np.ndarray) -> None:
        """
        This checks if an array is fully numeric or not.
        :param array:numpy.ndarray: array to be checked
        :raises TypeError: if the data or targets are not all numerical data
        """
        if not isinstance(array, np.ndarray):
            raise TypeError(
                "The given array is not compatible with this model."
            )
        try:
            array.astype(float)
        except TypeError:
            print("The given array ({array}) is not (fully) numeric.")

    def _check_compatible(self, data: np.ndarray, target: np.ndarray) -> None:
        """
        This checks if two arrays are of the same length.

        :param data:np.ndarray: array 1 to compare
        :param target:numpy.ndarray: array 2 to compare
        :raises ValueError: if data and target do not have the same lenght
        """
        if data.shape[0] != len(target):
            raise ValueError(
                "The two arrays do not share the same length. (",
                data.shape[0],
                ") !=  (",
                len(target),
                ").",
            )

    def train(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        This trains (sets slope and intercept of)
        the model on the given data and targets.

        :param x:numpy.ndarray: labeled continous data
        :param y:numpy.ndarray: continous targets
        :raises LinAlgError: if production matrix is not inversible
        """
        self._check_numerical(x)
        self._check_numerical(y)
        self._check_compatible(x, y)

        x_with_intercept = np.c_[np.ones(x.shape[0]), x]
        x_transpose = x_with_intercept.transpose()
        production = np.dot(x_transpose, x_with_intercept)

        try:
            inverse_production = np.linalg.inv(production)
        except np.linalg.LinAlgError:
            print("The production matrix is not invertible.")

        slope_product = np.dot(inverse_production, x_transpose)
        parameters = np.dot(slope_product, y)
        self.intercept = float(parameters[0])
        self.slope = parameters[1:].flatten()

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        This predicts new values from data on the trained model.

        :param x:numpy.ndarray: data to predict upon
        :returns:np.ndarray: predicted values for each data point
        :raises ValueError: if the model has not been trained yet
        """
        self._check_numerical(x)

        intercept = self.intercept
        slope = self.slope

        if type(slope) is None:
            raise ValueError(
                "The model does not have the slope parameter set yet.",
                " Please train the model first.",
            )

        if type(intercept) is None:
            raise ValueError(
                "The model does not have the intercept parameter set yet.",
                " Please train the model first.",
            )

        self._check_compatible(x[0], slope)
        return intercept + np.dot(x, self.slope)


class NormRegression(MultiLinearRegression):
    def __init__(
        self,
        factor: float,
        learning_rate: float,
        random_0_t0_1: bool,
        iterations: int,
    ):
        super().__init__()
        self._iterations = iterations
        self._learning_rate = learning_rate
        self._random_0_to_1 = random_0_t0_1
        self._factor = factor
        self._parameters = None

    @abstractmethod
    def _gradient(self, weights: np.ndarray) -> None:
        pass

    @abstractmethod
    def _norm(self, weights: np.ndarray) -> None:
        pass

    @property
    def iterations(self):
        return self._iterations

    @property
    def learning_rate(self):
        return

    @learning_rate.getter
    def learning_rate(self) -> float:
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, rate: float) -> None:
        if not isinstance(rate, float):
            raise TypeError(f"Expected float, got {type(rate)}.")
        self._learning_rate = rate

    @property
    def factor(self):
        return

    @factor.getter
    def factor(self) -> float:
        return self._factor

    @factor.setter
    def factor(self, rate: float) -> None:
        if not isinstance(rate, float):
            raise TypeError(f"Expected float, got {type(rate)}.")
        self._factor = rate

    @property
    def random_0_to_1(self):
        return

    @random_0_to_1.getter
    def random_0_to_1(self) -> bool:
        return self._random_0_to_1

    @random_0_to_1.setter
    def random_0_to_1(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"Expected bool, got {type(value)}.")
        self._random_0_to_1 = value

    @property
    def parameters(self):
        return

    @parameters.getter
    def parameters(self) -> np.array:
        """
        This returns an array of the models parameters.

        :returns:numpy.array: all coefficients (learning_rate,
            random_0_to_1, intercept, slope)
        """
        parameters = np.insert(self.slope, 0, self.intercept)
        parameters = np.inset(parameters, 0, self.random_0_to_1)
        parameters = np.inset(parameters, 0, self.learning_rate)
        return parameters

    @parameters.setter
    def parameters(self, parameters: np.array) -> None:
        """
        This sets the parameters to a given value.

        :param parameters:numpy.array: array of all
        coefficients to be set (intercept, slope)
        """
        self.learning_rate = parameters[0]
        self.random_0_to_1 = parameters[1]
        self.intercept = parameters[2]
        self.slope = parameters[3:]
        return

    def train(self, data: np.ndarray, target: np.ndarray):
        logging.basicConfig(
            level=logging.DEBUG,
            filename="train.log",
        )
        if self.random_0_to_1:
            w = np.random.randn(data.shape[1] + 1)
        else:
            w = np.random.uniform(-1, 1, data.shape[1] + 1)
        self.intercept = w[0]
        self.slope = w[1:]

        for i in range(self.iterations):
            prediction = self.predict(data)
            mse = self.mse(data, prediction, target)
            loss = mse + self._norm(w)
            logging.debug(
                f"Iteration {i+1} out of {self.iterations}: Loss = {loss},"
                + f"MSE = {mse}."
            )
            w = w - self.learning_rate * self._gradient(
                w, data, prediction, target
            )


class LassoRegression(NormRegression):
    def _norm(self, weights: np.ndarray) -> float:
        return np.linalg.norm(weights, 1)

    def _gradient(
        self,
        weights: np.ndarray,
        data: np.ndarray,
        prediction: np.ndarray,
        target: np.ndarray,
    ) -> np.ndarray:
        print(prediction.shape)
        print(data.shape)
        print(data.T.shape)
        return (-2 / len(prediction)) * data.T.dot(
            target.flatten() - prediction
        ) + 2 * self.factor * weights


class RidgeRegression(NormRegression):
    def _norm(self, weights: np.ndarray) -> float:
        return np.linalg.norm(weights, 2)

    def _gradient(
        self,
        weights: np.ndarray,
        data: np.ndarray,
        prediction: np.ndarray,
        target: np.ndarray,
    ) -> np.ndarray:
        return (-2 / len(prediction)) * np.dot(
            data.T, target.flatten() - prediction
        ) + self.factor * np.sign(weights)
