from flask import Flask, jsonify, request
from pathlib import Path
import json

app = Flask(__name__)
DATA = Path(__file__).resolve().parent.parent / "data" / "products.json"

def load_products():
    return json.loads(DATA.read_text(encoding="utf-8"))

@app.get("/api/products")
def products():
    items = load_products()
    q = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "").strip()
    if q:
        items = [p for p in items if q in f"{p['name']} {p['brand']} {p['category']}".lower()]
    if category and category.lower() != "all":
        items = [p for p in items if p["category"].lower() == category.lower()]
    return jsonify(items)

@app.get("/api/products/<int:product_id>")
def product(product_id):
    for p in load_products():
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "PriceWise API"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
