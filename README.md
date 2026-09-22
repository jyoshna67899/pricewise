# PriceWise — Smart Price Comparison Platform

PriceWise is a portfolio-ready price comparison dashboard. It lets users search products, compare prices across multiple retailer entries, inspect discounts/ratings/delivery, save products to a wishlist, and view price analysis charts.

## Included in this final project

### Frontend
- Responsive dashboard
- Product search
- Category filtering
- Sorting
- Multi-store comparison
- Lowest-price detection
- Discount calculation
- Ratings/specifications
- Delivery information
- Wishlist with LocalStorage
- Dark mode
- Price comparison chart
- Demo price-history chart
- Deal/savings summary
- Product details modal

### Backend starter
A Flask API is included in `backend/app.py` with:
- `GET /api/health`
- `GET /api/products`
- `GET /api/products/<id>`

The backend currently serves the project's local catalog. This is intentional: the project does NOT claim to scrape or provide live retailer prices.

## Run the frontend

Open `index.html` in a browser, or use VS Code Live Server.

## Run the Flask API

```bash
cd backend
pip install -r requirements.txt
python app.py
```

API:
- `http://127.0.0.1:5000/api/health`
- `http://127.0.0.1:5000/api/products`
- `http://127.0.0.1:5000/api/products?q=iphone`

## GitHub Pages

The frontend is static and can be deployed with GitHub Pages:
1. Create a repository.
2. Upload `index.html`, `style.css`, `script.js`, `README.md`, `data/`, and optionally `backend/`.
3. Go to Settings → Pages.
4. Select Deploy from branch → `main` → `/ (root)`.

The Flask API cannot run on GitHub Pages because GitHub Pages hosts static files. Deploy the API separately if you want the frontend to consume it online.

## Live retailer data

The retailer values included in this project are **demo/sample values**. They are not guaranteed current prices and are not fetched from Amazon, Flipkart, Croma, or Reliance Digital.

For a production version, connect to retailer APIs, affiliate/product feeds, or other sources whose terms explicitly permit price retrieval. Do not bypass bot protections or scrape sites in violation of their terms.

## Suggested resume line

**PriceWise — Smart Price Comparison Platform:** Built a responsive web application for comparing product prices across multiple retailer entries, with search/filtering, discount analysis, lowest-price detection, price-history visualization, wishlist persistence, dark mode, and a Flask REST API.
