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
    For the implementation of the MultiLinearRegression class, we used the formulas provided in the description of the assignment. More specifically, we used the formulas to compute the slope and to compute the predicted values using the two dimensional matrix.

# The constructor
    The user can initialize the model with a default slope and intercapt that will be used without training. If that does no happen, then those values will be set to `None`. Both the models `_intercept` and `_slope`` are indicated to be private and should therefore only be accessed by functions inside of the class. We chose this to apply the OOP concept as best as possible. Therefore, we also indicated the setter functions `_set_slope()` and `_set_intercept()` to be private.
    
    The first functions that we created were the train and predict which are used to train the model on a given dataset and make predictions based on a different dataset. The functions were implemented based on the formulas provided in the description of the assignment. 
    In order to optimize this object and improve its functionality we added separete functions for getting the parameters, the slope and the intercept of the current model. This way we can import the object into other files and make use of these functions. We implemented private functions for setting the parameters, the slope and the intercept.
    Moreover, we implemented exceptions for the train() function that would raise a TypeError which would declare that the given data/target is not fully numeric. We also implemented the type errors LinAlgError (would raise an error if the matrix is not invertible) and ValueError (would raise an error if data and target do not have the same sample size) 

**regression_plotter.py**

    Inside the constructor we intialize the values for the given data frame and the given target values. Inside the constructor we raise an error (ValueError) whenever the data and target do not share the same sample size. 
    Inside the RegressionPlotter object we have two functions. The plot() function is used to create a scatterplot in 2D or 3D depending on how many parameters we have. It is important to note that this scatterplot also shows the regression line of the model that was used to predict the target values.
    The plot_all() function is used to generate subplots to visualize each coefficient of a linear regression model.
    Both the plot() and plot_all() function raise an error (AttributeError) whenever we want to plot a graph of a model that does not support the use of intercepts or of a slope. 

**model_saver.py**

    Inside the constructor of the ModelSaver object we initialize the supported formats for the files for saving and loading the the parameters of a machine learning model (the formats are json and pickle). We do not want the user to interfere with the process of getting and setting the parameters thus, we make the _get_params() and _set_params() functions private. We use the functions save_parameters() and load_parameters() to simply choose the type of file we want to save and load the parameters in. The other functions which are used to save and load the parameters to their respective type of file (either json or pickle) are made private.
