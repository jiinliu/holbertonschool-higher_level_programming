from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def load_json_products():
    with open('products.json') as f:
        return json.load(f)

def load_csv_products():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return [ { "id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"]) } for row in reader ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        json_data = json.load(f)
    
    return render_template('items.html', items=json_data.get('items', []))




@app.route('/products')
def products():
    source = request.args.get('source')
    id_str = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = load_json_products()
    elif source == 'csv':
        products = load_csv_products()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error, products=[])

    if id_str:
        try:
            pid = int(id_str)
            products = [p for p in products if p["id"] == pid]
        except:
            products = []
        if not products:
            error = "Product not found"

    return render_template('product_display.html', error=error, products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
