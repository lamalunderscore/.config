import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes 
import pickle
import json
from multi_linear_regression import MultiLinearRegression

class ModelSaver:
    def __init__(self, format:str='json') -> None:
        supported_formats= ['json', 'pickle']
        if format not in supported_formats:
            raise NotImplementedError("This format is not implemented yet. Please Choose one of the following: 'json', 'pickle'.")
        self._format = format

    def _get_params(self, model:object) -> np.ndarray:
        try:
            return model.get_params()
        except AttributeError:
            print("Specified model does not support saving parameters.")
            return

    def _set_params(self, model:object, parameters:np.ndarray) -> None:
        try:
            model.set_params(parameters)
        except AttributeError:
            print("Specified model does not support loading parameters.")
        return

    def save_parameters(self, filename:str, model:object) -> None:
        parameters = self._get_params(model)
        match self._format:
            case 'pickle':
                self._save_pickle(filename, parameters)
            case 'json':
                self._save_json(filename, parameters)
        return
    
    def load_parameters(self, filename:str, model:object) -> None:
        match self._format:
            case 'pickle':
                parameters = self._load_pickle(filename)
            case 'json':
                parameters = self._load_json(filename)
        self._set_params(model, parameters)
        return

    def _save_pickle(self, filename:str, parameters:np.ndarray) -> None:
        with open(filename, "wb") as openfile:
            pickle.dump(parameters, openfile)
        return

    def _load_pickle(self, filename:str) -> np.ndarray:
        with open(filename, "rb") as openfile:
            loaded_parameters = pickle.load(filename)
        return loaded_parameters
    
    def _save_json(self, filename:str, parameters:np.ndarray) -> None:
        with open(filename, "w") as outfile:
            try:
                json.dump(parameters, outfile)
            except TypeError:
                json.dump(parameters.tolist(), outfile)
        return

    def _load_json(self, filename:str) -> np.ndarray:
        with open(filename, "r") as openfile:
            loaded_parameters = np.asarray(json.load(openfile))
        return loaded_parameters

if __name__=="__main__":
    data = load_diabetes()
    diabetes_data = pd.DataFrame(data.data, columns = data.feature_names)
    y = pd.DataFrame(data.target)

    model = MultiLinearRegression()
    model.train(diabetes_data, y)
    print(model.predict(diabetes_data)[0])

    saver = ModelSaver('json')
    filename = "new_file.sav"
    saver.save_parameters(filename, model)

    new_model = MultiLinearRegression()
    saver.load_parameters(filename, new_model)

    print(new_model.predict(diabetes_data)[0])


    
    