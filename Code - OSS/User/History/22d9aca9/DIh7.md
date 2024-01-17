# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

Fork this repo on your private github account.
You can do so by clicking this button on the top-right panel:
![](fork.png) 

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 src/main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report

# Quick summary
In this assignment, we implemented three classes: MultiLinearRegression, RegressionPlotter and ModelSaver. MultiLinearRegression is a class that acts as a machine learning model in order to predict values based on a given dataset. The RegressionPlotter class is used to plot the graph of a given model. It plots the graph depending on the number of features. The ModelSaver class is used to save and load the parameters of a generic machine learning model.

## multi_linear_regression.py

# The constructor
The user can initialize the model with a default slope and intercapt that will be used without training. If that does no happen, then those values will be set to `None`. Both the models `_intercept` and `_slope`` are indicated to be private and should therefore only be accessed by functions inside of the class. We chose this to apply the OOP concept as best as possible.

# The getters and setters
For the same reason, we indicated the setter functions `_set_slope()` and `_set_intercept()` to be private. The `set_params()` function as well as all the getter functions are indicated to be public. These functions are all necessary to adhere to the requirements posed by both the RegressionPlotter and ModelSaver classes.

# `train()` and `predict()`
We created `train()` and `predict()` which are used to train the model on a given dataset and make predictions based on a (different) dataset. For the implementation of these two functions, we used the formulas provided in the assignment. More specifically, we used the formulas to compute the combined slope and intercept matrix as well as to compute the predicted values.
We implmented Error raises for scenarios that could occur due to false use. There are checks for equal sample sizes of data and target set, not fully numeric data or target sets, matrix invertability and if a data set has the right number of features to be used for predictions.


## regression_plotter.py

# The constructor
Inside the constructor the user has to initialize the scatter plot `_data` and `_target`, which are both indacated to be private. They do not feature a getter or setter. Both sets are being checked for compatibility, which raises an error if they are of different lengths.

# Plotting
We have two plotting functions. Both functions require a model to be passed.
`plot()` is used to create a scatterplot in 2D or 3D, depending on how many slope coefficients the model has. In the 2D plot, the regression prediction is shown as a line; in the 3D plot, the regression prediction is shown as a plane.
`plot_all()` is used to generate one subplot for every slope coefficient to visualize each parameter of a multilinear regression model.
Both `plot()` and `plot_all()` check for the necessary getter functions in the passed model and raise an Error if necessary. 

## model_saver.py

# The constructor
We initialize the saver with the chosen format. We also check if the passed format string is actually supported by this class and raise an exception if that is not the case.

# The getters and setters
We do not want the user to utilize the savers' `_get_params()` or `_set_params()` function, which is why they are indicated to be private. These functions are simply there to check if a model actually supports `get_params()` and `set_params()`. If the specified model does not, then we raise an Exception.

# Saving and Loading
We use the functions save_parameters() and load_parameters() to simply choose the type of file we want to save and load the parameters in. The other functions which are used to save and load the parameters to their respective type of file (either json or pickle) are made private.
