import sqlite3
import pandas as pd

conn = sqlite3.connect('shopeasy.db')

# Query 1 — Overall sentiment breakdown
print("=" * 50)
print("QUERY 1: Sentiment Distribution")
print("=" * 50)
q1 = pd.read_sql("""
    SELECT 
        SentimentCategory,
        COUNT(*) as Total_Reviews,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_reviews), 2) as Percentage
    FROM customer_reviews
    GROUP BY SentimentCategory
    ORDER BY Total_Reviews DESC
""", conn)
print(q1)

# Query 2 — Average rating by product
print("\n" + "=" * 50)
print("QUERY 2: Top and Bottom Products by Rating")
print("=" * 50)
q2 = pd.read_sql("""
    SELECT 
        ProductID,
        ROUND(AVG(Rating), 2) as Avg_Rating,
        COUNT(*) as Total_Reviews
    FROM customer_reviews
    GROUP BY ProductID
    ORDER BY Avg_Rating DESC
""", conn)
print(q2)

# Query 3 — Top issue categories from negative reviews
print("\n" + "=" * 50)
print("QUERY 3: Top Complaint Categories")
print("=" * 50)
q3 = pd.read_sql("""
    SELECT 
        IssueCategory,
        COUNT(*) as Frequency,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM negative_reviews), 2) as Percentage
    FROM negative_reviews
    GROUP BY IssueCategory
    ORDER BY Frequency DESC
""", conn)
print(q3)

# Query 4 — Sentiment trend by year
print("\n" + "=" * 50)
print("QUERY 4: Sentiment Trend Over Time")
print("=" * 50)
q4 = pd.read_sql("""
    SELECT 
        strftime('%Y', ReviewDate) as Year,
        ROUND(AVG(SentimentScore), 3) as Avg_Sentiment,
        COUNT(*) as Total_Reviews
    FROM customer_reviews
    GROUP BY Year
    ORDER BY Year
""", conn)
print(q4)

# Save results for Power BI
q1.to_csv('sentiment_distribution.csv', index=False)
q2.to_csv('product_ratings.csv', index=False)
q3.to_csv('complaint_categories.csv', index=False)
q4.to_csv('sentiment_trend.csv', index=False)
print("CSVs saved for Power BI!")

conn.close()
print("\nAll queries completed!")