import pandas as pd

df = pd.read_csv('data/raw_reviews.csv')
df.drop_duplicates(subset=['review', 'bank'], inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

df.to_csv('data/cleaned_reviews.csv', index=False)