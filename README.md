# End2End Heart Disease Prediction Using Machine Learning

### Project Description
<p align='justify'> This project aims to develop an end-to-end machine learning model that predicts the likelihood of heart disease based on various medical parameters. By analyzing key factors such as age, gender, blood pressure, cholesterol levels, heart rate, and other health metrics, the model provides insights into the risk of heart disease. This project intends to support healthcare professionals and individuals by providing quick predictions to promote early detection and lifestyle interventions. </p>

### Screenshot
<img width="800" height="400" align="center" src="/screenshots/sample_image.png">

### Technologies Used in This Project
* Python: Core programming language for building the model and the application
* Pandas: For data handling and manipulation
* Scikit-learn: For developing, training, and evaluating the model
* MLflow: For Experiment Tracking and Optimizing the Model
* Flask: For deploying the model as a web-based application
* Jupyter Notebook: For exploratory data analysis (EDA)
* HTML/CSS: To design the user interface for the web application
* Git/GitHub: For version control and project hosting

### Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sharan-vj/End2End_Heart_Disease_Prediction_Using_ML.git
    cd End2End_Nutrition_Based_Food_Health_Classifier_Using_ML
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:8080/`.

6. **Note**:

    In Default, This project will track parameters and metrics in local mlflow tracking uri `http://127.0.0.1:5000/`. To view experiments run the below command from project directory

    ```bash
    mlflow ui
    ```
    and open `http://127.0.0.1:5000/` this url.


### DagsHub Integration (Optional)

1. Create .env file in project main directory and Store below environment variables with required values from dagshub.
    ```
    MLFLOW_TRACKING_URI = " "
    MLFLOW_TRACKING_USERNAME = " "
    MLFLOW_TRACKING_PASSWORD = " "
    ```

2. Change the tracking URI `http://127.0.0.1:5000` to `MLFLOW_TRACKING_URI` in `model_trainer.py` and `model_evaluation.py` found in src/components folder.

### Usage
* Input Health Data: Enter parameters such as age, cholesterol levels, blood pressure, etc., into the web interface.
* Get Prediction: The model will predict whether there is a risk of heart disease based on the input parameters.

### Dataset
* The dataset used to train the model contains information on patient health metrics along with labels indicating the presence or absence of heart disease. The dataset is available in the `data/` directory.

### Model
* The prediction model is built using Scikit-learn. After training, the model is saved as a joblib file (final_model.joblib) inside the` models/` directory for easy reusability.

### Contributing
* Contributions are welcome! If you have any suggestions or improvements, please raise an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.