import joblib
import pandas as pd
import os

MODEL_PATH = 'saved_models/best_churn_model.joblib'
SCALER_PATH = 'saved_models/scaler.joblib'

def predict_new_customer(customer_data):
    """ Loads the best saved model and scaler to predict churn. """
    if not (os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH)):
        print("Model or scaler not found. Please run `notebooks/churn_analysis.ipynb` first.")
        return

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and scaler loaded successfully.")

    # Get the column order from the trained model
    training_columns = model.feature_names_in_
    new_customer_df = pd.DataFrame([customer_data]).reindex(columns=training_columns, fill_value=0)
    
    new_customer_scaled = scaler.transform(new_customer_df)
    prediction = model.predict(new_customer_scaled)
    prediction_proba = model.predict_proba(new_customer_scaled)

    print("\n--- New Customer Prediction ---")
    if prediction[0] == 1:
        print(f"Prediction: Customer WILL CHURN")
    else:
        print(f"Prediction: Customer WILL NOT CHURN")
    print(f"Probability of Churn: {prediction_proba[0][1]:.2%}")

if __name__ == '__main__':
    new_customer = {
        'tenure': 2,
        'MonthlyCharges': 95.50,
        'TotalCharges': 190.0,
        'InternetService_FiberOptic': 1,
        'Contract_One year': 0,
        'Contract_Two year': 0,
        'PaymentMethod_Electronic check': 1,
        'MonthlyChargeTenureRatio': 31.83
    }
    predict_new_customer(new_customer)