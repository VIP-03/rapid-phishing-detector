import pandas as pd

df = pd.read_excel(r'.\refined_phishing_dataset.xlsx')
print('shape=', df.shape)
print('columns=', df.columns.tolist())
print(df.head(3).to_string(index=False))
print(df['status'].value_counts().to_dict())
