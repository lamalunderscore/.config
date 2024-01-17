import pandas as pd
import numpy as np
import pickle
import json

class ModelSaver:
    def __init__(self, format:str='json') -> None:
        '''
        This initializes the saver with the chosen format.

        :param format:str: format for the saver
        :raises NotImplementedError: if a passed string is not a supported format
        '''
        supported_formats= ['json', 'pickle']
        if format not in supported_formats:
            raise NotImplementedError("This format is not implemented yet. Please Choose one of the following: 'json', 'pickle'.")
        self._format = format

    def _get_params(self, model:object) -> np.array:
        """
        This function is used to get the parameters of an object (generic machine learning model). 

        :param model:object: A generic machine learning model
        :returns:numpy.array: parameters of the model
        :raises AttributeError: In the case the model does not support saving the parameters and the function get_params
        """
        try:
            return model.get_params()
        except AttributeError:
            print("Specified model does not support saving parameters.")
            return

    def _set_params(self, model:object, parameters:np.array) -> None:
        """
        This function is used to set the parameters to given values.

        :param model:object: A generic machine learning model
        :param parameters:np.ndarray: An array made out of
        :raises AttributeError: In the case the model does not support the function set_params
        """
        try:
            model.set_params(parameters)
        except AttributeError:
            print("Specified model does not support loading parameters.")
        return

    def save_parameters(self, filename:str, model:object) -> None:
        """
        This function is used to save the parameters of a given machine learning mdoel to a file in a specified format, either pickle or json.

        :param filename:str: The name of the file where the parameters will be saved.
        :param model:object: The machine learning model from where the parameters will be extracted.
        """
        parameters = self._get_params(model)
        match self._format:
            case 'pickle':
                self._save_pickle(filename, parameters)
            case 'json':
                self._save_json(filename, parameters)
        return
    
    def load_parameters(self, filename:str, model:object) -> None:
        """
        This function is used to load the parameters of a given machine learning mdoel from a file in a specified format, either pickle or json.

        :param filename:str: The name of the file where the parameters will be extracted from.
        :param model:object: The machine learning model to which the parameters will be set.
        """
        match self._format:
            case 'pickle':
                parameters = self._load_pickle(filename)
            case 'json':
                parameters = self._load_json(filename)
        self._set_params(model, parameters)
        return

    def _save_pickle(self, filename:str, parameters:np.ndarray) -> None:
        """
        This function is used to save the parameters of a machine learning model in the pickle format.

        :param filename:str: The name of the file where the parameters will be saved.
        :param parameters:np.ndarray: An array of the parameters that we want to save.
        """
        with open(filename, "wb") as openfile:
            pickle.dump(parameters, openfile)
        return

    def _load_pickle(self, filename:str) -> np.ndarray:
        """
        This function is used to load the parameters of a machine learning model from a file with the pickle format.

        :param filename:str: The name of the file from which we want to extract the parameters from.
        :returns:np.ndarray: An array of the parameters that we just loaded.
        """
        with open(filename, "rb") as openfile:
            loaded_parameters = pickle.load(filename)
        return loaded_parameters
    
    def _save_json(self, filename:str, parameters:np.ndarray) -> None:
        """
        This function is used to save the parameters of a machine learning model in the json format.

        :param filename:str: The name of the file where the parameters will be saved.
        :param parameters:np.ndarray: An array of the parameters that we want to save.
        """
        with open(filename, "w") as outfile:
            try:
                json.dump(parameters, outfile)
            except TypeError:
                json.dump(parameters.tolist(), outfile)
        return

    def _load_json(self, filename:str) -> np.ndarray:
        """
        This function is used to load the parameters of a machine learning model from a file with the json format.

        :param filename:str: The name of the file from which we want to extract the parameters from.
        :returns:np.ndarray: An array of the parameters that we just loaded.
        """
        with open(filename, "r") as openfile:
            loaded_parameters = np.asarray(json.load(openfile))
        return loaded_parameters

