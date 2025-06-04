from google_play_scraper import Sort, reviews_all
import pandas as pd
from datetime import datetime

from google_play_scraper import reviews_all
import pandas as pd

apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

all_reviews = []

for bank, app_id in apps.items():
    reviews = reviews_all(app_id, lang='en', country='us')
    for r in reviews:
        all_reviews.append({
            'review': r['content'],
            'rating': r['score'],
            'date': r['at'].strftime('%Y-%m-%d'),
            'bank': bank,
            'source': 'Google Play'
        })

df = pd.DataFrame(all_reviews)
df.to_csv('data/raw_reviews.csv', index=False)