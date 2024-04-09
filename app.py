from flask import Flask, render_template, jsonify
import json
import requests
from typing import Optional

app = Flask(__name__)

class Product:
    def __init__(self, Id: int, Name: str, Description: str, Category: str, SubCategory: str, RegularPrice: float, 
                 SalePrice: Optional[float], ImageUrl: str, VideoUrl: str, SKU: str, StockStatus: str, Weight: float, 
                 Dimensions: str, Variants: str, Reviews: str, Ratings: str, RelatedProducts: str, MetaTitle: str, 
                 MetaDescription: str, Keywords: str, ProductType: str):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Category = Category
        self.SubCategory = SubCategory
        self.RegularPrice = RegularPrice
        self.SalePrice = SalePrice
        self.ImageUrl = ImageUrl
        self.VideoUrl = VideoUrl
        self.SKU = SKU
        self.StockStatus = StockStatus
        self.Weight = Weight
        self.Dimensions = Dimensions
        self.Variants = Variants
        self.Reviews = Reviews
        self.Ratings = Ratings
        self.RelatedProducts = RelatedProducts
        self.MetaTitle = MetaTitle
        self.MetaDescription = MetaDescription
        self.Keywords = Keywords
        self.ProductType = ProductType

def fetch_products(url: str):
    response = requests.get(url)
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
        data = response.json()
        products = [Product(**item) for item in data]
        return products
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return []

@app.route('/')
def home():
    products = fetch_products('http://localhost:5000/products')
    return render_template('home.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products', methods=['GET'])
def get_products():
    with open('products.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/fetch_products', methods=['GET'])
def fetch_products_route():
    products = fetch_products('http://localhost:5000/products')
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)