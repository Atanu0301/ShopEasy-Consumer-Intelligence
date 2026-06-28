import sqlite3
import pandas as pd

conn = sqlite3.connect('shopeasy.db')
cursor = conn.cursor()

# Table 1 — Customer Journey
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_journey (
    JourneyID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ProductID VARCHAR(20),
    VisitDate DATE,
    Stage VARCHAR(20),
    Action VARCHAR(20),
    Duration REAL
)
''')

# Table 2 — Customer Reviews
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_reviews (
    ReviewID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ProductID VARCHAR(20),
    ReviewDate DATE,
    Rating INTEGER,
    ReviewText TEXT
)
''')

# Table 3 — Engagement Data
cursor.execute('''
CREATE TABLE IF NOT EXISTS engagement_data (
    EngagementID INTEGER PRIMARY KEY,
    ContentID INTEGER,
    ContentType VARCHAR(20),
    ProductID VARCHAR(20),
    ViewsClicksCombined VARCHAR(20),
    Likes INTEGER,
    EngagementDate DATE
)
''')

conn.commit()
print("All 3 tables created successfully!")
conn.close()