import sqlite3
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

conn = sqlite3.connect('shopeasy.db')

# Load reviews
reviews = pd.read_csv('customer_reviews_sentiment.csv')
print(f"Total reviews: {len(reviews)}")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Run VADER on each review text
def get_sentiment(text):
    if pd.isna(text):
        return 0
    scores = analyzer.polarity_scores(str(text))
    return scores['compound']

# Apply sentiment scoring
reviews['VADER_Score'] = reviews['ReviewText'].apply(get_sentiment)

# Classify sentiment
def classify(score, rating):
    if score >= 0.05 and rating >= 4:
        return 'Positive'
    elif score <= -0.05 and rating <= 2:
        return 'Negative'
    elif score <= -0.05 and rating >= 3:
        return 'Mixed Negative'
    elif score >= 0.05 and rating <= 3:
        return 'Mixed Positive'
    else:
        return 'Neutral'

reviews['Final_Sentiment'] = reviews.apply(
    lambda x: classify(x['VADER_Score'], x['Rating']), axis=1
)

# Results
print("\nVADER Sentiment Distribution:")
print(reviews['Final_Sentiment'].value_counts())

print("\nSample scored reviews:")
print(reviews[['ReviewText', 'Rating', 
               'VADER_Score', 'Final_Sentiment']].head(5))

# Save output
reviews.to_csv('reviews_vader_scored.csv', index=False)
reviews.to_sql('reviews_scored', conn, 
               if_exists='replace', index=False)

print("\nVADER scoring complete! File saved.")
conn.close()