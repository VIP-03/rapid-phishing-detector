from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / 'best_phishing_model.pkl'
DATASET_PATH = PROJECT_DIR / 'refined_phishing_dataset.xlsx'

FEATURES: List[str] = []
MODEL = None


def load_model_and_features() -> None:
    global FEATURES, MODEL

    if not MODEL_PATH.exists():
        raise FileNotFoundError('Model file not found. Please run train_model.py first.')
    if not DATASET_PATH.exists():
        raise FileNotFoundError('Dataset file not found.')

    df = pd.read_excel(DATASET_PATH)
    FEATURES[:] = [col for col in df.columns if col != 'status']
    MODEL = joblib.load(MODEL_PATH)


def parse_input(payload: Dict[str, Any]) -> Dict[str, float]:
    parsed: Dict[str, float] = {}
    for feature in FEATURES:
        raw_value = payload.get(feature)
        if raw_value in (None, ''):
            raise ValueError(f'Missing required field: {feature}')
        parsed[feature] = float(raw_value)
    return parsed


def explain_prediction(payload: Dict[str, Any]) -> Dict[str, Any]:
    if MODEL is None:
        load_model_and_features()

    feature_values = parse_input(payload)
    row_df = pd.DataFrame([feature_values], columns=FEATURES)
    prediction = MODEL.predict(row_df)[0]
    probability = MODEL.predict_proba(row_df)[0]
    explanation = []

    for feature, weight in sorted(
        zip(FEATURES, MODEL.feature_importances_),
        key=lambda item: item[1],
        reverse=True,
    ):
        explanation.append(
            {
                'feature': feature,
                'importance': round(float(weight), 6),
                'value': round(float(feature_values[feature]), 6),
            }
        )

    top_factors = explanation[:5]
    result = {
        'prediction': 'phishing' if prediction == 1 else 'legitimate',
        'probability': {
            'legitimate': round(float(probability[0]), 6),
            'phishing': round(float(probability[1]), 6),
        },
        'top_factors': top_factors,
        'all_features': explanation,
        'model_accuracy': '96.28% (validated on the project test split)',
    }
    return result


@app.route('/')
def index() -> str:
    if not FEATURES:
        load_model_and_features()
    return render_template('index.html', features=FEATURES)


@app.route('/predict', methods=['POST'])
def predict() -> Any:
    if not FEATURES:
        load_model_and_features()
    try:
        payload = request.get_json(silent=True) or request.form.to_dict(flat=True)
        row = parse_input(payload)
        df = pd.DataFrame([row], columns=FEATURES)
        prediction = int(MODEL.predict(df)[0])
        probability = MODEL.predict_proba(df)[0]
        response = {
            'prediction': 'phishing' if prediction == 1 else 'legitimate',
            'probability': {
                'legitimate': round(float(probability[0]), 6),
                'phishing': round(float(probability[1]), 6),
            },
        }
        return jsonify(response)
    except Exception as exc:  # pragma: no cover - API error reporting
        return jsonify({'error': str(exc)}), 400


@app.route('/explain', methods=['POST'])
def explain() -> Any:
    if not FEATURES:
        load_model_and_features()
    try:
        payload = request.get_json(silent=True) or request.form.to_dict(flat=True)
        explanation = explain_prediction(payload)
        return jsonify(explanation)
    except Exception as exc:  # pragma: no cover - API error reporting
        return jsonify({'error': str(exc)}), 400


@app.route('/health')
def health() -> Any:
    return jsonify({'status': 'ok', 'features': len(FEATURES)})


if __name__ == '__main__':
    load_model_and_features()
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
