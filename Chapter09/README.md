# Chapter 9 - THE TENSORFLOW PLATFORM AND KERAS API

## About This Chapter

We will be using neural network based methods extensively in the following chapters. These methods are based on multi-dimensional array operations. TensorFlow\index{TensorFlow} provides a platform to perform all these operations. The Keras\index{Keras} API will simplify life for use while benefiting from TensorFlow.\index{TensorFlow} Therefore, we will consider both in this chapter. To do so, we will start with their installation. Then, we will explore constant and variable declarations in TensorFlow. Afterward, we will define arithmetic operations on these. Then, we will consider activation functions under TensorFlow. We will also provide the link between the NumPy library and TensorFlow. We will consider loading data as the first end of chapter application. Next, we will introduce loading and storing neural network models under TensorFlow as the second end of chapter application. Finally, we will evaluate converting neural network models from other platforms to TensorFlow format as the third end of chapter application.

## Listings
<center>

| Description                                       | Code                                                       |
|-------------------------------------------------- | ---------------------------------------------------------- |
| Constant scalar assignment in TensorFlow          | [![Code](../Images/py.png)](PythonScripts/tf_scalar.py)    |
| Constant vector assignment in TensorFlow          | [![Code](../Images/py.png)](PythonScripts/tf_vector.py)    |
| Constant matrix assignment in TensorFlow          | [![Code](../Images/py.png)](PythonScripts/tf_matrix.py)    |
| Constant tensor assignment in TensorFlow          | [![Code](../Images/py.png)](PythonScripts/tf_tensor.py)    |
| Variable assignment in TensorFlow                 | [![Code](../Images/py.png)](PythonScripts/tf_variable.py)  |
| Addition and subtraction operations in TensorFlow | [![Code](../Images/py.png)](PythonScripts/tf_sum.py)       |
| Element-wise multiplication in TensorFlow         | [![Code](../Images/py.png)](PythonScripts/tf_multiply.py)  |
| Vector and matrix multiplications                 | [![Code](../Images/py.png)](PythonScripts/tf_matmul.py)    |
| TensorFlow and NumPy conversions                  | [![Code](../Images/py.png)](PythonScripts/tf_numpy.py)     |

</center>


## End of Chapter Applications

<!-- <center>

| Description                         | Python Scripts                                             |
| ----------------------------------- | ---------------------------------------------------------- |
| **Application: Load and Store Neural Network Models**     | 
|                              Saving a model in TensorFlow | [![Code](../Images/py.png)](PythonScripts/standard_scaler.py)     |
| **Application: Converting Neural Network Models from Other Platforms** |
| <table align="right"> <tbody> <tr> <td> Converting PyTorch model to ONNX format </td> <td>  </td> </tr>  <tr>  <td>Converting the ONNX model to TensorFlow and TensorFlow Lite model </td>  <td><code>[![Code](../Images/py.png)](PythonScripts/convert_from_onnx.py)</code></td> </tr>  </tbody>  </table> | |

</center> -->

<table>
    <thead>
        <tr>
            <th>Description</th>
            <th>Code</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2"><b>Application: Load and Store Neural Network Models</b></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Saving a model in TensorFlow</td>
            <td><a href="PythonScripts/tf_save.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Converting Neural Network Models from Other Platforms</b></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting PyTorch model to ONNX format</td>
            <td><a href="PythonScripts/convert_from_torch.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting the ONNX model to TensorFlow and TensorFlow Lite model</td>
            <td><a href="PythonScripts/convert_from_onnx.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
    </tbody>
</table>

