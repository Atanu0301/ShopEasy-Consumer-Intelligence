import sqlite3
import pandas as pd

conn = sqlite3.connect('shopeasy.db')

# Load reviews into database
reviews = pd.read_csv('customer_reviews_sentiment.csv')
reviews.to_sql('customer_reviews', conn, 
               if_exists='replace', index=False)
print(f"Reviews loaded: {len(reviews)} rows")

# Load negative reviews into database
negative = pd.read_csv('negative_reviews_issues.csv')
negative.to_sql('negative_reviews', conn, 
                if_exists='replace', index=False)
print(f"Negative reviews loaded: {len(negative)} rows")

# Verify both tables exist
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("\nTables in database:")
print(tables)

conn.close()
print("\nAll data loaded successfully!")