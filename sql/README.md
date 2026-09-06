# Predictive Churn Model for a Telecom Provider

This project builds and compares two machine learning models (Logistic Regression and Random Forest) to proactively predict customer churn. The goal is to identify the best-performing and most interpretable model to derive actionable business insights.

## Project Structure

- **/data**: Contains the raw CSV and the generated SQLite database (`telecom.db`).
- **/sql**: Holds the SQL script (`get_churn_data.sql`) for extracting and transforming data.
- **/notebooks**: Contains the main Jupyter Notebook (`churn_analysis.ipynb`) for analysis, model training, and comparison.
- **/saved_models**: Stores the final, selected model (`.joblib`) and scaler objects.
- `database_setup.py`: A one-time script to create the SQLite database from the raw CSV.
- `predict_churn.py`: An example script to load the final saved model and make a prediction.

## How to Run This Project

1.  **Install Libraries**:
    ```bash
    pip install pandas scikit-learn sqlalchemy joblib
    ```
2.  **Download the Data**: Place the `WA_Fn-UseC_-Telco-Customer-Churn.csv` file in the `/data` folder.
3.  **Create the Database**: Run the setup script from your terminal:
    ```bash
    python database_setup.py
    ```
4.  **Train and Compare Models**: Open and run all cells in the `churn_analysis.ipynb` notebook. This will train both models, evaluate them, and save the best-performing one.
5.  **Make a Prediction**: Run the prediction script to use the final saved model:
    ```bash
    python predict_churn.py
    ```