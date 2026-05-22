import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('products.csv')
df['combined'] = df['name'] + ' ' + df['category'] + ' ' + df['tags']

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['combined'])
similarity = cosine_similarity(matrix)

def get_recommendations(product_name, n=3):
    matches = df[df['name'].str.lower() == product_name.lower()]
    if matches.empty:
        return []
    
    idx = matches.index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top = scores[1:n+1]
    
    results = []
    for i, score in top:
        # 1. Cleanly handle missing values (NaN) in the tags column if any exist
        query_tags_raw = str(df.iloc[idx]['tags']) if pd.notna(df.iloc[idx]['tags']) else ""
        product_tags_raw = str(df.iloc[i]['tags']) if pd.notna(df.iloc[i]['tags']) else ""
        
        # 2. Convert space-separated tag strings into python sets for instant comparison
        query_tags = set(query_tags_raw.lower().split())
        product_tags = set(product_tags_raw.lower().split())
        
        # 3. Intersect the sets to find matching keywords, and take up to the top 3
        common = list(product_tags & query_tags)[:3]
        
        results.append({
            "name": df.iloc[i]['name'],
            "category": df.iloc[i]['category'],
            "score": round(float(score), 2),
            "common_tags": common  # This matches the 'item.common_tags' property your UI expects
        })
        
    return results

def get_all_products():
    return df['name'].tolist()