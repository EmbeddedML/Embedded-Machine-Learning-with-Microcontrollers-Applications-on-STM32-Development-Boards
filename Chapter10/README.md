# Chapter 10 - FUNDAMENTALS OF NEURAL NETWORKS

## About This Chapter

As all journeys start with a single step, all neural network models can be formed by defining a single neuron. Therefore, we will introduce the single neuron in this chapter. To do so, we will start with its structure and mathematical definition. Then, we will consider forming the single neuron in TensorFlow and Keras. Although we will benefit from the latter option in the following sections, forming the neuron in TensorFlow gives valuable insight on working principles of neural networks. Therefore, we will cover it in this chapter. Afterward, we will focus on training the single neuron. Here, we will explain the mechanism in training, loss function, and optimizers used in training. We will cover training both in TensorFlow and Keras. Next, we will form a classifier and regressor by the single neuron. Finally, we will consider real-life applications introduced in the previous chapters now from the single neuron perspective.

## Listings
<center>

| Description                                               | Code                                                                        |
|---------------------------------------------------------- | --------------------------------------------------------------------------- |
| Initializing the single neuron weights in TensorFlow      | [![Code](../Images/py.png)](PythonScripts/tf_model_class.py)                |
| Input output relation of the single neuron in TensorFlow  | [![Code](../Images/py.png)](PythonScripts/tf_model_call.py)                 |
| Single neuron definition in Keras                         | [![Code](../Images/py.png)](PythonScripts/keras_neuron_def.py)              |
| Single neuron input output calculation on an interval     | [![Code](../Images/py.png)](PythonScripts/decision_boundary.py)             |
| Binary cross-entropy loss calculation                     | [![Code](../Images/py.png)](PythonScripts/bce.py)                           |
| Categorical cross entropy loss calculation                | [![Code](../Images/py.png)](PythonScripts/cce.py)                           |
| MSE loss calculation                                      | [![Code](../Images/py.png)](PythonScripts/mse.py)                           |
| Cosine similarity loss calculation                        | [![Code](../Images/py.png)](PythonScripts/cos_sim.py)                       |
| Stochastic gradient descent optimizer example             | [![Code](../Images/py.png)](PythonScripts/sgd.py)                           |
| Gradient descent steps in TensorFlow                      | [![Code](../Images/py.png)](PythonScripts/gradient_step.py)                 |
| RMSProp optimizer example                                 | [![Code](../Images/py.png)](PythonScripts/rmsprop.py)                       |
| Adam optimizer example                                    | [![Code](../Images/py.png)](PythonScripts/adam.py)                          |
| Training the single neuron in TensorFlow                  | [![Code](../Images/py.png)](PythonScripts/tf_train_loop.py)                 |
| Training the single neuron in Keras                       | [![Code](../Images/py.png)](PythonScripts/single_neuron_regressor.py)       |
| Forming a classifier with the single neuron               | [![Code](../Images/py.png)](PythonScripts/single_neuron_classifier.py)      |
| Forming a regressor with the single neuron                | [![Code](../Images/py.png)](PythonScripts/single_neuron_regressor_sine.py)  |

</center>


## End of Chapter Applications

<center>

| Description                         | Python Scripts                                                                                 | Projecet Files |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- | -------------- |
| **Application: Human Activity Recognition via Accelerometer Data** | [![Code](../Images/py.png)](EOC1/har_perceptron.py)             | [![Code]()]()  |
| **Application: Keyword Spotting from Audio Signals**               | [![Code](../Images/py.png)](EOC2/fsdd_perceptron.py)            | [![Code]()]()  |
| **Application: Handwritten Digit Recognition from Digital Images** | [![Code](../Images/py.png)](EOC3/mnist_perceptron_train.py)     | [![Code]()]()  |
| **Application: Estimating Future Temperature Value**               | [![Code](../Images/py.png)](EOC4/temperature_pred.py)           | [![Code]()]()  |

</center>

