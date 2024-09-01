# Chapter 14 - RECURRENCE IN NEURAL NETWORKS

## About This Chapter

We only had forward connections in neural network models up to this point. In this chapter, we will add feedback connection between neurons to form recurrence. This will help us in forming neural network structures with memory capability. Hence, they will be more suitable for sequential data processing. To explain these concepts better, we will first associate recurrence with memory in this chapter. Afterward, we will introduce three popular neural network models based on recurrence as recurrent neural networks (RNN), gated recurrent unit (GRU), and long short-term memory (LSTM). While introducing each model, we will first provide general information about it. Then, we will focus on its formation and training in Keras. Then, we will provide the usage examples of recurrence models on PC. Afterward, we will consider implementing recurrence models on the STM32 microcontroller. Finally, we will provide examples on the usage of recurrence based models to solve real-life problems.

## Listings
<center>

| Description                                            | Code                                                              |
|------------------------------------------------------- | ----------------------------------------------------------------- |
| Manual RNN formation                                   | [![Code](../Images/py.png)](PythonScripts/simpleRNN.py)           |
| Manual RNN formation, second case                      | [![Code](../Images/py.png)](PythonScripts/rnn_layers.py)          |
| Extracting RNN model parameters                        | [![Code](../Images/py.png)](PythonScripts/rnn_weights.py)         |
| Manual GRU formation                                   | [![Code](../Images/py.png)](PythonScripts/gru.py)                 |
| Extracting GRU model parameters                        | [![Code](../Images/cpp.png)](PythonScripts/gru_layers.py)         |
| Manual LSTM formation                                  | [![Code](../Images/py.png)](PythonScripts/lstm.py)                |
| Extracting LSTM model parameters                       | [![Code](../Images/py.png)](PythonScripts/lstm_layers.py)         |
| Preparing dataset for regression via recurrence models | [![Code](../Images/cpp.png)](PythonScripts/timeseries_dataset.py) |
| Regression example via RNN, GRU, and LSTM              | [![Code](../Images/py.png)](PythonScripts/lstm_timeseries.py)     |
| Image classification example via RNN, GRU, and LSTM    | [![Code](../Images/py.png)](PythonScripts/mnist_lstm.py)          |

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
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Forming a data loader to generate MFCC features for keyword spotting from audio signals</td>
            <td><a href="EOC1/data_loader.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Forming the LSTM model for keyword spotting from audio signals</td>
            <td><a href="EOC1/model.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Training the formed LSTM model for keyword spotting from audio signals</td>
            <td><a href="EOC1/fsdd_rnn.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting the trained LSTM model to TensorFlow Lite format and C++ array</td>
            <td><a href="EOC1/convert_lite.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Handwritten Digit Recognition from Digital Images</b></td>
            <td><a href = ""><img src = "" alt="Project"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;The LSTM model for handwritten digit recognition</td>
            <td><a href="EOC2/model.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Training the LSTM model on the MNIST dataset</td>
            <td><a href="EOC2/mnist_rnn.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting the trained LSTM model to TensorFlow Lite model and C++ array</td>
            <td><a href="EOC2/convert_lite.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td colspan="2"><b>Application: Handwritten Digit Recognition from Digital Images</b></td>
            <td><a href = ""><img src = "" alt="Project"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Forming the GRU model in Keras</td>
            <td><a href="EOC3/model.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Training the GRU model for future temperature value estimation</td>
            <td><a href="EOC3/rnn_temperature_pred.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;Converting future temperature value estimation model to TensorFlow Lite format</td>
            <td><a href="EOC3/convert_lite.py"><img src="../Images/py.png" alt="Code"></a></td>
        </tr>
    </tbody>
</table>

</center>