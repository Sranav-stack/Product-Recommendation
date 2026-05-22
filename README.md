# 🛍️ Product Recommendation Engine

A content-based filtering recommendation system built with Python and Flask.
Simulates the "Customers also liked" feature seen in retail platforms like Amazon and Flipkart.

## How it works
1. Products are described by name, category and tags
2. TF-IDF vectorization converts text into numerical vectors
3. Cosine similarity scores every product pair
4. Top 3 similar products are returned via a REST API

## Tech Stack
- Python · scikit-learn · Flask · Pandas
- Vanilla JS frontend with live search

## Run locally
pip install flask scikit-learn pandas flask-cors
python app.py
# Open frontend/index.html
