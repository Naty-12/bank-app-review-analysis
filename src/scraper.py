from google_play_scraper import Sort, reviews_all
import pandas as pd
from datetime import datetime

def scrape_reviews(app_id, bank_name, source='Google Play'):
    reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='us',
        sort=Sort.NEWEST
    )

    df = pd.DataFrame(reviews)
    df = df[['content', 'score', 'at']]
    df.columns = ['review', 'rating', 'date']
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    df['bank'] = bank_name
    df['source'] = source
    return df

banks = {
    'com.bankA.app': 'Bank A',
    'com.bankB.app': 'Bank B',
    'com.bankC.app': 'Bank C'
}

dfs = []
for app_id, name in banks.items():
    df = scrape_reviews(app_id, name)
    dfs.append(df)

combined_df = pd.concat(dfs).drop_duplicates().dropna()
combined_df.to_csv('data/bank_reviews.csv', index=False)