# ShopEasy Consumer Intelligence
### SQL · Python (VADER NLP) · Power BI | E-commerce Sentiment Analysis

---

## Business Problem
ShopEasy, an e-commerce retailer, is experiencing declining customer 
satisfaction. The goal is to analyze 1,363 customer reviews, identify 
root causes of dissatisfaction, and recommend data-driven actions to 
improve product ratings and customer experience.

---

## Dataset
- **Source:** Simulated e-commerce customer reviews dataset
- **Size:** 1,363 reviews across 20 product categories
- **Tables:** customer_reviews, negative_reviews, sentiment_distribution,
  complaint_categories, sentiment_trend

---

## Tools & Technologies
- **SQL (SQLite)** — Data validation, cleaning, aggregation queries
- **Python (VADER NLP)** — Sentiment scoring on 1,363 review texts
- **Power BI** — Interactive dashboard with KPI cards and trend analysis

---

## Key Findings

### 1. Unmet Expectations is #1 complaint
31% of all negative reviews cite unmet expectations — product 
descriptions are misleading customers before purchase.

### 2. No product crosses the 4.0 rating benchmark
All 20 products rated between 3.48–3.91 — indicating a systemic 
quality or expectation gap across the entire catalogue.

### 3. Sentiment declined in 2024 then recovered
Average sentiment dropped from 0.201 (2023) to 0.182 (2024) 
before recovering to 0.195 (2025) — root cause needs investigation.

---

## Business Recommendation
> Rewrite product descriptions for top 5 complaint products to 
> set accurate expectations. Launch quality review for bottom 3 
> rated products. Estimated impact: 35 additional purchases per 
> cycle by improving checkout conversion from 19% to 25%.

---

## Dashboard Preview
<img width="960" height="537" alt="image" src="https://github.com/user-attachments/assets/4bc9f759-869d-4c49-8467-7286d08f5d64" />


---

## Project Structure

ShopEasy-Consumer-Intelligence/
│
├── create_tables.py          # SQLite database setup
├── load_data.py              # CSV to database loader
├── analysis.py               # SQL queries + EDA
├── sentiment_analysis.py     # VADER NLP pipeline
├── shopeasy_dashboard.pbix   # Power BI dashboard
├── shopeasy_dashboard_final.png  # Dashboard screenshot
└── README.md                 # Project documentation

---

## SQL Highlights
```sql
-- Top complaint categories
SELECT IssueCategory, COUNT(*) as Frequency,
    ROUND(COUNT(*) * 100.0 / 
    (SELECT COUNT(*) FROM negative_reviews), 2) as Percentage
FROM negative_reviews
GROUP BY IssueCategory
ORDER BY Frequency DESC;
```
