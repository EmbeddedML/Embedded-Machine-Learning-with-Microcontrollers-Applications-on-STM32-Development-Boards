This is the official code repository of the book:
**Embedded Machine Learning with Microcontrollers: Applications on ?? Development Boards**

## Before you start
Before getting started, it is highly recommended to create a Python virtual environment and install required libraries. To do so, run the following command in your terminal:
``` python -m venv .venv```
### On Windows:
```.\.venv\Scripts\activate```
### On macOS/Linux:
```source .venv/bin/activate```

### Running Python Scripts
You can Python scripts by calling the corresponding file as Python module using the following command.
```python -m <Chapter#>.PythonScripts.<module_name>```
or
```python -m <Chapter#>.<Application>.main``` to run main application codes related to that End of Chapter applications.

For example, one can use the following commands to run Chapter5 scripts.
```python -m Chapter05.PythonScripts.clf_data_generation``` to generate classification data
or 
```python -m Chapter05.Application1-HAR.main``` to generate Human Activity Recognition features.

### Running Embedded Project Files

Furthermore, one can directly import ?? projects to ?? IDE using the ?? Projects folder under each chapter.

<TBD>

You can find more detailed information regarding files and their capabilities in the chapter folders.