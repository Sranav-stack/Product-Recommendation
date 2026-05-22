from flask import Flask, jsonify
from flask_cors import CORS
from recommender import get_recommendations, get_all_products

app = Flask(__name__)
CORS(app)

@app.route('/products')
def products():
    return jsonify(get_all_products())

@app.route('/recommend/<product_name>')
def recommend(product_name):
    results = get_recommendations(product_name)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)