# Chapter 7 - REGRESSION

## About This Chapter

The aim in regression is forming a relationship between one or more input and output variables. Hence, information on one variable can be obtained by using the information on other variables. To fully explain the regression concept, we will start with its definition in this chapter. Then, we will introduce linear, polynomial, kNN,and decision tree regression. While handling each regression method, we will cover its theoretical background. Then, we will explore its formation in Python language on PC. Afterward, we will show methods to deploy the formed regressor to the STM32 microcontroller. We will form a regressor to estimate future temperature values as end of chapter application.

## Listings
<center>

| Description                                                       | Code                                                              |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| Training the linear regressor and saving the trained model        | [![Code](../Images/py.png)](PythonScripts/train_reg_lr.py)        |
| Predictions with the formed linear regressors.                    | [![Code](../Images/py.png)](PythonScripts/inference_reg_lr.py)    |
| Exporting the trained linear regression model                     | [![Code](../Images/py.png)](PythonScripts/export_reg_lr.py)       |
| Header file for the linear regression model                       | [![Code](../Images/C.png)]()                                      |
| Source file for the linear regression model                       | [![Code](../Images/C.png)]()                                      |
| Linear regression test code for STM32CubeIDE                      | [![Code](../Images/C.png)]()                                      |
| Python script for comparing linear regression results             | [![Code](../Images/py.png)](PythonScripts/setup_reg_lr.py)        |
| Linear regression test code for Mbed Studio                       | [![Code](../Images/cpp.png)]()                                    |
| Training the polynomial regressor and saving the trained model    | [![Code](../Images/py.png)](PythonScripts/train_reg_pr.py)        |
| Predictions with the polynomial regressor                         | [![Code](../Images/py.png)](PythonScripts/inference_reg_pr.py)    |
| Exporting the trained polynomial regression model                 | [![Code](../Images/py.png)](PythonScripts/export_reg_pr.py)       |
| Header file for the polynomial regression model                   | [![Code](../Images/C.png)]()                                      |
| Source file for the polynomial regression model                   | [![Code](../Images/C.png)]()                                      |
| Polynomial regression test code for STM32CubeIDE                  | [![Code](../Images/C.png)]()                                      |
| Python script for comparing polynomial regression results         | [![Code](../Images/py.png)](PythonScripts/setup_reg_pr.py)        |
| Polynomial regression test code for Mbed Studio                   | [![Code](../Images/cpp.png)]()                                    |
| Training the kNN regressor and saving the trained model           | [![Code](../Images/py.png)](PythonScripts/train_reg_knn.py)       |
| Predictions with the kNN regressor                                | [![Code](../Images/py.png)](PythonScripts/inference_reg_knn.py)   |
| Exporting the trained kNN regression model                        | [![Code](../Images/py.png)](PythonScripts/export_reg_knn.py)      |
| Header file for the kNN regression configuration                  | [![Code](../Images/C.png)]()                                      |
| SSource file for the kNN regression configuration                 | [![Code](../Images/C.png)]()                                      |
| kNN regression test code for STM32CubeIDE                         | [![Code](../Images/C.png)]()                                      |
| Python script for comparing kNN regression results                | [![Code](../Images/py.png)](PythonScripts/setup_reg_knn.py)       |
| kNN regression test code for Mbed Studio                          | [![Code](../Images/cpp.png)]()                                    |
| Training the decision tree regressor and saving the trained model | [![Code](../Images/py.png)](PythonScripts/train_reg_dt.py)        |
| Predictions with the decision tree regressor                      | [![Code](../Images/py.png)](PythonScripts/inference_reg_dt.py)    |
| Exporting the trained decision tree regression model              | [![Code](../Images/py.png)](PythonScripts/export_reg_dt.py)       |
| Header file for the decision tree regression configuration        | [![Code](../Images/C.png)]()                                      |
| Source file for the decision tree regression configuration        | [![Code](../Images/C.png)]()                                      |
| Decision tree regression test code for STM32CubeIDE               | [![Code](../Images/C.png)]()                                      |
| Python script for comparing decision tree regression results      | [![Code](../Images/py.png)](PythonScripts/export_reg_dt.py)       |
| Decision tree regression test code for Mbed Studio                | [![Code](../Images/cpp.png)]()                                    |

</center>

<!-- ## End of Chapter Applications
<center>

| Description  | Python Scripts   | Project Files |
| ----------------------------------- | ----------------------------------------------------   | ----------------------------------------------------  |
| Human Activity Recognition          | [![Code](../Images/py.png)](Application1-HAR/main.py)  | [![Code](../Images/stm32.png)](Application1-HAR/.ioc) |
| Keyword Spotting                    | [![Code](../Images/py.png)](Application2-KWS/main.py)  | [![Code](../Images/stm32.png)](Application2-KWS/.ioc)  |
| Handwritten Digit Recognition       | [![Code](../Images/py.png)](Application3-HDR/mnist.py) | [![Code](../Images/stm32.png)](Application3-HDR/.ioc)  |

</center> -->