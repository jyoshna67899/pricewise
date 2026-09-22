# PriceWise Project Guide

## Folder structure

PriceWise/
- index.html — main web page
- style.css — design/responsive styles
- script.js — frontend logic and demo catalog
- data/products.json — backend catalog data
- backend/app.py — Flask REST API
- backend/requirements.txt — Python dependency
- README.md — GitHub documentation

## Important distinction

The UI compares four retailer entries:
Amazon, Flipkart, Croma, and Reliance Digital.

These are sample values in this portfolio build. The application does not pretend to have live access to retailer systems.

## Next upgrade

Replace the local catalog with permitted API/feed responses and persist price snapshots in SQLite/PostgreSQL. Then implement scheduled updates and alerts.
