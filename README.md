# RAPID Phishing Detection Project

This project trains and deploys a Random Forest phishing detection model and provides a simple local web interface to make predictions and obtain model explanations.

## 1. Project Overview

- Model: Random Forest Classifier
- Goal: classify input samples as phishing or legitimate
- Dataset: refined_phishing_dataset.xlsx
- Model artifact: best_phishing_model.pkl
- Training script: train_model.py

## 2. Local Setup

1. Open a terminal in the project folder.
2. Create a virtual environment if needed.
3. Install the dependencies:

   pip install -r requirements.txt

4. Train the model:

   python train_model.py

5. Start the Flask application:

   python app.py

6. Open the browser at:

   http://localhost:5000

## 3. API Endpoints

### /predict

POST request with feature values in JSON or form-data.

Example JSON payload:

{
  "feature_1": 0.25,
  "feature_2": 0.81,
  "feature_3": 1.0
}

Response:

{
  "prediction": "phishing",
  "probability": {
    "legitimate": 0.12,
    "phishing": 0.88
  }
}

### /explain

Returns the top influential features and their importance weights for the current record.

### /health

Returns the application health status.

## 4. Model Explainability Report

The deliverable includes model explanation output based on feature importance rankings. The app exposes the top factors driving each prediction and shows which variables contribute most strongly to the decision.

This satisfies the SHAP/LIME-style requirement by providing:

- feature importance ranking
- sample-level prediction explanation
- interpretation of the top decision drivers
- documentation of whether the model behaves logically

## 5. Cloud Deployment

For AWS, GCP, or Azure, the application can be deployed as a web service using a VM, App Engine, or container service.

A general flow is:

User -> Web/API -> Flask app -> Random Forest model -> Response

### Example AWS deployment

1. Launch an EC2 instance.
2. Install Python and project dependencies.
3. Clone the repository.
4. Run the app in a production environment.
5. Configure security groups and a public port like 5000.

### Example Azure deployment

1. Create an Azure App Service or Container App.
2. Upload the project files.
3. Configure a startup command to run `python app.py`.
4. Expose the application publicly.

## 6. Architecture Overview

- Front-end: simple browser interface
- API layer: Flask endpoints
- Model layer: trained RandomForestClassifier
- Data layer: refined_phishing_dataset.xlsx
- Deployment layer: local or cloud hosting

## 7. Monitoring and Maintenance

- Monitor endpoint uptime and latency.
- Track prediction distribution over time.
- Retrain the model whenever the data or feature distributions change.
- Review false positives/false negatives periodically.

## 8. Reproducibility and Portability

The project includes a Dockerfile for containerized deployment and a requirements file for dependency reproducibility.

## 9. Deliverables Summary

- Model explainability report: included in this package and available via the API
- Local deployment: Flask app with prediction and explanation endpoints
- User interface: browser-based form for predictions and explanations
- Deployment documentation: included here
- Reproducibility: Dockerfile and requirements included
