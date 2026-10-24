import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

print('1. Loading the refined dataset from Excel...')
# Reading from your Excel file shown in VS Code
df_refined = pd.read_excel('refined_phishing_dataset.xlsx')

X = df_refined.drop(columns=['status'])
y = df_refined['status'].apply(lambda x: 1 if x == 'phishing' else 0)

print('2. Splitting data into training and testing sets...')
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print('3. Training the Random Forest model...')
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f'Model Training Complete! Test Accuracy: {acc * 100:.2f}%')

print('4. Saving model artifact as best_phishing_model.pkl...')
joblib.dump(model, 'best_phishing_model.pkl')
print(
    'Success! best_phishing_model.pkl has been created in your project folder!'
)