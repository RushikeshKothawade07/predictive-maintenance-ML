# Machine Predictive Maintenance Classification
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.2-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-0.87.0-blueviolet.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-brightgreen.svg)
![Joblib](https://img.shields.io/badge/Joblib-1.1.1-yellow.svg)

This application is designed to predict machine failure for predictive maintenance using machine learning. It utilizes a synthetic dataset with 10,000 data points and 14 features. The application is built using a Random Forest model to classify whether the machine will experience failure or not based on the provided inputs.

You can view the deployed app here : https://predictive-maintenance-using-machine-learning.streamlit.app/

## Google Colab Notebook
Click [here](https://colab.research.google.com/drive/1QXPrLjqd07hcsgr3JxycuTREV998h4Yr?usp=sharing) to open the Google Colab notebook for this project.

### Kaggle Dataset
Click [here](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification) to view the dataset used in this project.

## Dataset Description

The dataset consists of the following features:
- `UID`: Unique identifier ranging from 1 to 10000.
- `productID`: Product quality variant with letters L, M, or H, and a variant-specific serial number.
- `air temperature [K]`: Generated using a random walk process, later normalized to a standard deviation of 2 K around 300 K.
- `process temperature [K]`: Generated using a random walk process, normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.
- `rotational speed [rpm]`: Calculated from power of 2860 W, overlaid with normally distributed noise.
- `torque [Nm]`: Torque values are normally distributed around 40 Nm with an Ïƒ = 10 Nm and no negative values.
- `tool wear [min]`: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.
- `machine failure`: A label that indicates whether the machine has failed in this particular data point for any of the following failure modes.

Important Note: There are two targets in the dataset. Do not use one of them as a feature, as it will lead to data leakage.

## How to Use the Application

To use the application, follow these steps:
1. Make sure you have Python installed on your system.
2. Install the required packages by running `pip install streamlit pandas scikit-learn` in your terminal or command prompt.
3. Clone this repository to your local machine.

## Running the Application

Navigate to the cloned repository in your terminal or command prompt, then run the following command:

```bash
streamlit run app.py
```


This will launch the application in your web browser.

## Application Workflow

1. Upon launching the application, you will see an input form with various fields corresponding to the features in the dataset.
2. Provide the required inputs in the form. Select the product quality variant, air temperature, process temperature, rotational speed, torque, and tool wear.
3. Click on the "Predict Failure" button to make a prediction.
4. The application will display whether the machine is predicted to experience failure or not.

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn

## About the Dataset

The synthetic dataset provided in this application reflects real predictive maintenance encountered in the industry to the best of our knowledge. The dataset contains 10,000 data points with 14 features. It includes a mix of low, medium, and high-quality variants, each with a specific serial number. The features represent various parameters like air temperature, process temperature, rotational speed, torque, and tool wear.

## Model Details

The predictive model used in this application is a Random Forest Classifier, a powerful ensemble learning method that can handle both numerical and categorical features. The model is trained on the synthetic dataset and can predict whether the machine will experience failure based on the input parameters.

## Disclaimer

This application uses a synthetic dataset for illustrative purposes. Real predictive maintenance datasets might differ in complexity and distribution. The predictions made by the model are based on the provided inputs and do not guarantee real-world results. Use this application for educational and demonstration purposes only.

Feel free to explore the application and experiment with different input values to observe how the predictive model performs for predictive maintenance classification.

---
*Author: [Rushikesh Kothawade]*
*Date: [05/08/2023]*
