# Chapter 6 - CLASSIFICATION

## About This Chapter

The aim of classification is to infer type of an unknown sample summarized by its features. Classifier is the machine learning system performing this operation. The classifier should have been trained beforehand for this purpose by labeled data. Hence, we assume that a supervisor has labeled the data to be used in training. To explain the classifier concept, we will start with its definition. Then, we will introduce the Bayes, k-nearest neighbor (kNN), support vector machine (SVM), and decision tree classifiers. While handling each classifier, we will start with its theoretical background. Then, we will explore its training on PC in Python language. Afterward, we will show methods of deploying the trained classifier to the STM32 microcontroller. As end of the chapter applications, we will form classifiers for the accelerometer data, audio signals, and digital images.We will benefit from the extracted features in Chapter 5 for this purpose.

## Listings
<center>

| Description                                                | Code                                                              |
| ---------------------------------------------------------- | ----------------------------------------------------------------- |
| Training the Bayes classifier                              | [![Code](../Images/py.png)](PythonScripts/train_cls_bayes.py)     |
| Inference with the Bayes classifier in Python              | [![Code](../Images/py.png)](PythonScripts/inference_cls_bayes.py) |
| Exporting the Bayes classifier                             | [![Code](../Images/py.png)](PythonScripts/export_cls_bayes.py)    |
| Header file for the Bayes classifier configuration         | [![Code](../Images/C.png)]()                                      |
| Source file for the Bayes classifier configuration         | [![Code](../Images/C.png)]()                                      |
| While loop for the Bayes classifier                        | [![Code](../Images/C.png)]()                                      |
| Bayes classifier test code for Mbed Studio                 | [![Code](../Images/cpp.png)]()                                    |
| Training the kNN classifier                                | [![Code](../Images/py.png)](PythonScripts/train_cls_knn.py)       |
| Inference with the kNN classifier in Python                | [![Code](../Images/py.png)](PythonScripts/inference_cls_knn.py)   |
| Exporting the kNN classifier                               | [![Code](../Images/py.png)](PythonScripts/export_cls_knn.py)      |
| Header file for the kNN classifier configuration           | [![Code](../Images/C.png)]()                                      |
| Source file for the kNN classifier configuration           | [![Code](../Images/C.png)]()                                      |
| While loop for the kNN classifier                          | [![Code](../Images/C.png)]()                                      |
| kNN classifier test code for Mbed Studio                   | [![Code](../Images/cpp.png)]()                                    |
| Training the SVM classifier                                | [![Code](../Images/py.png)](PythonScripts/train_cls_svm.py)       |
| Inference with the SVM classifier in Python                | [![Code](../Images/py.png)](PythonScripts/inference_cls_svm.py)   |
| Exporting the SVM classifier                               | [![Code](../Images/py.png)](PythonScripts/export_cls_svm.py)      |
| Header file for the SVM classifier configuration           | [![Code](../Images/C.png)]()                                      |
| Source file for the SVM classifier configuration           | [![Code](../Images/C.png)]()                                      |
| While loop for the SVM classifier                          | [![Code](../Images/C.png)]()                                      |
| SVM classifier test code for Mbed Studio                   | [![Code](../Images/cpp.png)]()                                    |
| Training the decision tree classifier                      | [![Code](../Images/py.png)](PythonScripts/train_cls_dt.py)        |
| Inference with the decision tree classifier in Python      | [![Code](../Images/py.png)](PythonScripts/inference_cls_dt.py)    |
| Exporting the decision tree classifier                     | [![Code](../Images/py.png)](PythonScripts/export_cls_dt.py)       |
| Header file for the decision tree classifier configuration | [![Code](../Images/C.png)]()                                      |
| Source file for the decision tree classifier configuration | [![Code](../Images/C.png)]()                                      |
| While loop for the decision tree classifier                | [![Code](../Images/C.png)]()                                      |
| Decision tree classifier test code for Mbed Studio         | [![Code](../Images/cpp.png)]()                                    |

</center>

## End of Chapter Applications
<center>

| Description  | Python Scripts   | Project Files |
| ----------------------------------- | ----------------------------------------------------   | ----------------------------------------------------  |
| Human Activity Recognition          | [![Code](../Images/py.png)](Application1-HAR/main.py)  | [![Code](../Images/stm32.png)](Application1-HAR/.ioc) |
| Keyword Spotting                    | [![Code](../Images/py.png)](Application2-KWS/main.py)  | [![Code](../Images/stm32.png)](Application2-KWS/.ioc)  |
| Handwritten Digit Recognition       | [![Code](../Images/py.png)](Application3-HDR/mnist.py) | [![Code](../Images/stm32.png)](Application3-HDR/.ioc)  |

</center>