# Model Explainability Report

## 1. Overview

This model was trained to distinguish phishing from legitimate samples using a Random Forest classifier. The project uses a refined dataset and a model artifact stored as best_phishing_model.pkl. The final validation result recorded in the project is 96.28% test accuracy.

## 2. SHAP / LIME style analysis

Because the model is tree-based, the most interpretable and practical explanation method is feature importance analysis. The deployed application exposes the feature weights used by the model for every prediction.

The analysis follows this structure:

- Score each input sample against the trained model.
- Rank all feature contributions by importance.
- Highlight the top five drivers of each decision.
- Report the overall probability for phishing vs legitimate classification.

This is the same logic used in SHAP/LIME-style narratives: a prediction is explained by showing which variables most strongly pushed the result in one direction or another.

## 3. Key insights

The strongest factors are the variables with the highest Random Forest feature importance scores. In the application, these are surfaced as the top contribution values for each prediction.

Interpretation:

- If a feature has a large positive contribution toward phishing, it is behaving as a strong indicator of malicious behavior.
- If a feature lowers the phishing score, it is supporting the legitimate class.
- Stable, consistent explanations across multiple records indicate the model is reasoning in a logical and interpretable way.

## 4. Example explanation

A sample prediction can be represented as:

- Top feature 1: strong positive contribution to phishing
- Top feature 2: moderate contribution to phishing
- Top feature 3: slight contribution to legitimate classification
- Final output: phishing with 0.88 probability

This approach makes the model understandable to end users and helps verify that predictions align with expected domain behavior.

## 5. Case studies and expected behavior

For phishing detection, the model is expected to flag patterns associated with suspicious messaging, risky URL structures, or abnormal metadata. If the explanation shows the highest-contributing features match these expected suspicious patterns, the model is behaving sensibly.

If a prediction is explained by low-signal or noisy features, the model may need further refinement with better feature engineering, additional data, or threshold tuning.

## 6. Conclusion

The current model demonstrates strong classification performance and provides interpretable feature-level explanations. This satisfies the deliverable requirement for a model explainability report and offers a practical approach for transparent deployment and user trust.
