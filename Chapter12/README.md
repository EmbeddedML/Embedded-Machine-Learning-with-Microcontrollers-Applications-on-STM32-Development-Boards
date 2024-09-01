# Chapter 12 - EMBEDDING THE NEURAL NETWORK MODEL TO THE MICROCONTROLLER

## ABout This Chapter

We introduced the TensorFlow platform and fundamentals of neural networks in previous chapters. It is time to embed the trained neural network models to the microcontroller. To do so, we will benefit from TensorFlow Lite as the specialized version of TensorFlow for embedded systems (including microcontrollers). Hence, we will start with its properties. Then, we will show ways of converting TensorFlow and Keras models to TensorFlow Lite format. Model conversion is not sufficient alone to embed the model on a microcontroller. The main reason is the size of TensorFlow Lite model. In other words, the model should be optimized beforehand since microcontrollers have limited flash and RAM size. Therefore, we will cover model optimization via quantization, pruning, and weight clustering. Operations to be performed up to this point will be done on PC. The next step is embedding the final TensorFlow Lite model to the microcontroller. Hence, we will consider necessary steps to be followed for this purpose. Embedding the trained neural network model to the microcontroller can also be done by the STM32Cube.AI platform. We will cover it to provide a second way of embedding a TensorFlow or Keras model to the STM32 microcontroller. Throughout the chapter, we will reconsider the neural network models introduced in Chapter 11 and embed them to the microcontroller. We will also apply the same procedure to the end of chapter applications.

## Listings
<center>

| Description                                                                        | Code                                                                   |
|----------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Converting a formed Keras model for classification to TensorFlow Lite format       | [![Code](../Images/py.png)](PythonScripts/convert_Keras_classifier.py) |
| Converting a formed Keras model for regression to TensorFlow Lite format           | [![Code](../Images/py.png)](PythonScripts/convert_Keras_regression.py) |
| Converting a saved TensorFlow model to TensorFlow Lite format                      | [![Code](../Images/py.png)](PythonScripts/convert_saved.py)            |
| Running the TensorFlow Lite interpreter on PC to check how the converted model responds to a given input | [![Code](../Images/py.png)](PythonScripts/TFLite_Interpreter.py) |
| Dynamic range quantization while forming the TensorFlow Lite model                 | [![Code](../Images/py.png)](PythonScripts/TFLite_DRQ.py)               |
| Full integer quantization while forming the TensorFlow Lite model                  | [![Code](../Images/py.png)](PythonScripts/TFLite_FIQ.py)               |
| Quantization aware training while forming the TensorFlow Lite model                | [![Code](../Images/py.png)](PythonScripts/TFLite_QAT.py)               |
| Pruning while forming the TensorFlow model                                         | [![Code](../Images/py.png)](PythonScripts/TFLite_Prune1.py)            |
| Quantization applied to the pruned TensorFlow model                                | [![Code](../Images/py.png)](PythonScripts/TFLite_Prune2.py)            |
| Weight clustering while forming the TensorFlow model                               | [![Code](../Images/py.png)](PythonScripts/TFLite_Cluster1.py)          |
| Quantization applied to the weight clustered TensorFlow model                      | [![Code](../Images/py.png)](PythonScripts/TFLite_Cluster2.py)          |
| Usage of the script for converting a TensorFlow Lite model to C array              | [![Code](../Images/py.png)](PythonScripts/export_tflitecc.py)          |
| Content of the converted file in shortened form                                    | [![Code](../Images/C.png)]()                                           |
| Python script for comparing TensorFlow Lite model inference results                | [![Code](../Images/py.png)](PythonScripts/Python_tflite_test_setup.py) |
| TensorFlow Lite model test code for Mbed Studio                                    | [![Code](../Images/C.png)]()                                           |

</center>


## End of Chapter Applications

<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Code</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2"><b>Application: Human Activity Recognition via Accelerometer Data</b></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Saving trained TensorFlow model</td>
            <td><a href="EOC1/mlp_har.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting TensorFlow model to TensorFlow Lite format and C array</td>
            <td><a href="EOC1/export_tflite.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Keyword Spotting from Audio Signals</b></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Saving trained TensorFlow model</td>
            <td><a href="EOC2/mllp_fsdd.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting TensorFlow model to TensorFlow Lite format and C array</td>
            <td><a href="EOC2/tflite2cc.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Handwritten Digit Recognition from Digital Images</b></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Saving trained TensorFlow model</td>
            <td><a href="EOC3/mlp_mnist.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting TensorFlow model to TensorFlow Lite format and C array</td>
            <td><a href="EOC3/tflite2cc.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
    </tbody>
</table>

