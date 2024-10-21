# Chapter 13 - CONVOLUTIONAL NEURAL NETWORKS

## About This Chapter

Convolutional neural networks (CNN) are extensively used in image classification and object recognition applications. Therefore, we consider them in this chapter. We introduce mathematical definition of the convolution operation and its implementation by a single neuron first. Afterward, we introduce the convolution definition under Keras. Then, we explore how to form a complete CNN model under Keras. Here, we focus on feature extraction and classification blocks forming the CNN model. Afterward, we consider training and testing steps of the formed model. We then explore transfer learning to benefit from existing CNN models to be modified for our own problem. We next consider implementation steps for embedding the trained and tested CNN model on the STM32 microcontroller. Finally, we provide examples on the usage of CNN models to solve real-life problems.

## Listings
<center>

| Description  | Code    |
|----------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Sobel filtering example under Keras | [![Code](../Images/py.png)](PythonScripts/sobel.py) |
| Feature extraction block of the CNN model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/mnist_cnn_model.py) |
| Visualizing the filters in the trained CNN model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/intermediate_layers.py) |
| Testing the trained CNN model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/mnist_cnn_model.py) |
| Building SqueezeNet in Keras | [![Code](../Images/py.png)](PythonScripts/squeezenet.py) |
| Transfer learning application with the SqueezeNet model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/squeezenet_tl.py) |
| Transfer learning application with the ResNet model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/resnet_tl.py) |
| Transfer learning application with the EfficientNet model for handwritten digit recognition| [![Code](../Images/py.png)](PythonScripts/efficientnet_tl.py) |
| Creating the MobileNetV2 model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/mobilenet.py) |
| Transfer learning application with the MobileNetV2 model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/mobilenet_tl.py) |
| Training ShuffleNet model for handwritten digit recognition | [![Code](../Images/py.png)](PythonScripts/shufflenet_tl.py) |

</center>


## End of Chapter Applications

<center>

<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Code</th>
            <th>Project Files </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2"><b>Application: Keyword Spotting from Audio Signals</b></td>
            <td><a href = ""><img src = "" alt="Project"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Creating spectrogram dataset from audio files</td>
            <td><a href="EOC1/data_loader.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Forming a CNN model for keyword spotting</td>
            <td><a href="EOC1/model.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Training the formed CNN model for keyword spotting</td>
            <td><a href="EOC1/fsdd_cnn.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting the trained CNN model to TensorFlow Lite model and C++ array</td>
            <td><a href="EOC1/convert_lite.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Handwritten Digit Recognition from Digital Images</b></td>
            <td><a href = ""><img src = "" alt="Project"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Training the ResNet model for handwritten digit recognition</td>
            <td><a href="EOC3/mlp_mnist.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting the trained ResNet model to TensorFlow Lite model and C++ array</td>
            <td><a href="EOC3/tflite2cc.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
    </tbody>
</table>

</center>