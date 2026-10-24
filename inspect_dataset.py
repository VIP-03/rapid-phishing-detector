import pandas as pd

df = pd.read_excel('refined_phishing_dataset.xlsx')
print('shape:', df.shape)
print('columns:', df.columns.tolist())
print('sample:')
print(df.head(3).to_string(index=False))
print('target_counts:', df['status'].value_counts().to_dict())
