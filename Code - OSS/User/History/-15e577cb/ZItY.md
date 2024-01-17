### Part 2
#### Generic Machine Learning Model
This abstract class is supposed to be a developmet frame for a generic model. Since every model has to be trained and can predict something, these are the included functionality methods. There is also a property introduced in this class: the parameters. Any model that is trained trains these parameters, so they have to exist.

#### MultiLinearRegression Changes
This class has been adjusted to improve the style and implement the private variables as properties. We also copied our MSE code from the old main.py and implemented it as a function in the MultiLinearRegression class, since it is useful in any regression model.

#### NormRegression
To implement these two classes, we wrote this template class, which covers all the functionalities of regression models with a norm implementation, except the specific changes for the norms. This class directly inherits from MultiLinearRegression, but changes `train()` and adds the abstract methods `_norm()` and `_gradient()` which are specific to the used norm. We chose this approach to make the code more readable and the differences between RidgeRegression and LassoRegression more apparent. `train()` uses `_norm()` and `_gradient()` for its calculations and takes four optional arguments as well as two non-optional ones. The non-optional arguments are the data and target for the training. The optional arguments specify the norm factor, learning-rate, the random initialization range and iterations for gradient descent.`_gradient()` takes five non-optional arguments, which are the passed norm factor, the weights of the model, the data, the current prediction of the model and the target. It returns a numpy.ndarray with the gradient of each parameter. `_norm()` takes only one non-optional argument, namely the weights to calculate the norm on.

#### LassoRegression
LassoRegresison directly inherits from NormRegression and implments the abstract methods `_norm()` `_gradient()` with the specific formulas for the L1 norm and respective gradient descent.

#### RidgeRegression
RidgeRegresison directly inherits from NormRegression and implments the abstract methods `_norm()` `_gradient()` with the specific formulas for the L2 norm and respective gradient descent.