# Chapter 14 - RECURRENCE IN NEURAL NETWORKS

## About This Chapter

We only had forward connections in neural network models up to this point. In this chapter, we will add feedback connection between neurons to form recurrence. This will help us in forming neural network structures with memory capability. Hence, they will be more suitable for sequential data processing. To explain these concepts better, we will first associate recurrence with memory in this chapter. Afterward, we will introduce three popular neural network models based on recurrence as recurrent neural networks (RNN), gated recurrent unit (GRU), and long short-term memory (LSTM). While introducing each model, we will first provide general information about it. Then, we will focus on its formation and training in Keras. Then, we will provide the usage examples of recurrence models on PC. Afterward, we will consider implementing recurrence models on the STM32 microcontroller. Finally, we will provide examples on the usage of recurrence based models to solve real-life problems.

## Listings
<center>

| Description                                            | Code                                                              |
| ------------------------------------------------------ | ----------------------------------------------------------------- |
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

| Description                                                        | Python Scripts                                        | Project Files                                                                                 |
| ------------------------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Application: Human Activity Recognition via Accelerometer Data** | [![Code](../Images/py.png)](Application1-KWS/main.py) | [![Code](../Images/stm32.png)](Application1-HAR/F746NG_CH14_EOC1_KeywordSpotting)             |
| **Application: Keyword Spotting from Audio Signals**               | [![Code](../Images/py.png)](Application2-HDR/main.py) | [![Code](../Images/stm32.png)](Application2-KWS/F746NG_CH14_EOC2_HandwrittenDigitRecognition) |
| **Application: Temperature Prediction**                            | [![Code](../Images/py.png)](Application3-TP/main.py)  | [![Code](../Images/stm32.png)](Application3-TP/F746NG_CH14_EOC3_TemperaturePrediction)        |
</center>