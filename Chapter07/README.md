# Chapter 7 - REGRESSION

## About This Chapter

The aim in regression is forming a relationship between one or more input and output variables. Hence, information on one variable can be obtained by using the information on other variables. To fully explain the regression concept, we will start with its definition in this chapter. Then, we will introduce linear, polynomial, kNN,and decision tree regression. While handling each regression method, we will cover its theoretical background. Then, we will explore its formation in Python language on PC. Afterward, we will show methods to deploy the formed regressor to the STM32 microcontroller. We will form a regressor to estimate future temperature values as end of chapter application.

## Listings
<center>

| Description                                                       | Code                                                                                                   |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Training the linear regressor and saving the trained model        | [![Code](../Images/py.png)](PythonScripts/train_reg_lr.py)                                             |
| Predictions with the formed linear regressors.                    | [![Code](../Images/py.png)](PythonScripts/inference_reg_lr.py)                                         |
| Exporting the trained linear regression model                     | [![Code](../Images/py.png)](PythonScripts/export_reg_lr.py)                                            |
| Header file for the linear regression model                       | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_LR/Core/Inc/linear_reg_config.h) |
| Source file for the linear regression model                       | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_LR/Core/Src/linear_reg_config.c) |
| Linear regression CubeIDE project                                 | [![Code](../Images/stm32.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_LR)                          |
| Python script for comparing linear regression results             | [![Code](../Images/py.png)](PythonScripts/setup_reg_lr.py)                                             |
| Linear regression test code for Mbed Studio                       | [![Code](../Images/cpp.png)]()                                                                         |
| Training the polynomial regressor and saving the trained model    | [![Code](../Images/py.png)](PythonScripts/train_reg_pr.py)                                             |
| Predictions with the polynomial regressor                         | [![Code](../Images/py.png)](PythonScripts/inference_reg_pr.py)                                         |
| Exporting the trained polynomial regression model                 | [![Code](../Images/py.png)](PythonScripts/export_reg_pr.py)                                            |
| Header file for the polynomial regression model                   | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_PR/Core/Inc/poly_reg_config.h)   |
| Source file for the polynomial regression model                   | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_PR/Core/Src/poly_reg_config.c)   |
| Polynomial regression CubeIDE project                             | [![Code](../Images/stm32.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_PR)                          |
| Python script for comparing polynomial regression results         | [![Code](../Images/py.png)](PythonScripts/setup_reg_pr.py)                                             |
| Polynomial regression test code for Mbed Studio                   | [![Code](../Images/cpp.png)]()                                                                         |
| Training the kNN regressor and saving the trained model           | [![Code](../Images/py.png)](PythonScripts/train_reg_knn.py)                                            |
| Predictions with the kNN regressor                                | [![Code](../Images/py.png)](PythonScripts/inference_reg_knn.py)                                        |
| Exporting the trained kNN regression model                        | [![Code](../Images/py.png)](PythonScripts/export_reg_knn.py)                                           |
| Header file for the kNN regression configuration                  | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_KNN/Core/Inc/knn_reg_config.h)   |
| SSource file for the kNN regression configuration                 | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_KNN/Core/Src/knn_reg_config.c)   |
| kNN regression CubeIDE project                                    | [![Code](../Images/stm32.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_KNN)                         |
| Python script for comparing kNN regression results                | [![Code](../Images/py.png)](PythonScripts/setup_reg_knn.py)                                            |
| kNN regression test code for Mbed Studio                          | [![Code](../Images/cpp.png)]()                                                                         |
| Training the decision tree regressor and saving the trained model | [![Code](../Images/py.png)](PythonScripts/train_reg_dt.py)                                             |
| Predictions with the decision tree regressor                      | [![Code](../Images/py.png)](PythonScripts/inference_reg_dt.py)                                         |
| Exporting the trained decision tree regression model              | [![Code](../Images/py.png)](PythonScripts/export_reg_dt.py)                                            |
| Header file for the decision tree regression configuration        | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_DT/Core/Inc/dt_reg_config.h)     |
| Source file for the decision tree regression configuration        | [![Code](../Images/C.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_DT/Core/Src/dt_reg_config.c)     |
| Decision tree regression CubeIDE project                          | [![Code](../Images/stm32.png)](Chapter07/CubeIDEProjects/F746NG_REGRESSOR_DT)                          |
| Python script for comparing decision tree regression results      | [![Code](../Images/py.png)](PythonScripts/export_reg_dt.py)                                            |
| Decision tree regression test code for Mbed Studio                | [![Code](../Images/cpp.png)]()                                                                         |

</center>

<!-- ## End of Chapter Applications
<center>

| Description                   | Python Scripts                                         | Project Files                                         |
| ----------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| Human Activity Recognition    | [![Code](../Images/py.png)](Application1-HAR/main.py)  | [![Code](../Images/stm32.png)](Application1-HAR/.ioc) |
| Keyword Spotting              | [![Code](../Images/py.png)](Application2-KWS/main.py)  | [![Code](../Images/stm32.png)](Application2-KWS/.ioc) |
| Handwritten Digit Recognition | [![Code](../Images/py.png)](Application3-HDR/mnist.py) | [![Code](../Images/stm32.png)](Application3-HDR/.ioc) |

</center> -->