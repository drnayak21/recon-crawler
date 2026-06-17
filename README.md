# recon-crawler

A CLI tool that crawls websites and extracts hidden API endpoints from JavaScript files.

## Features
- Extracts all JS files from a target website
- Searches JS files for API routes and fetch calls
- Works on any website with readable JavaScript

## Installation
```bash
pip install requests beautifulsoup4
```

## Usage
```bash
python main.py https://target.com
```

## Example Output
```
Found API endpoints in https://juice-shop.herokuapp.com/main.js
Found API Route: /rest/admin
Found API Route: /rest/wallet/balance
Found API Route: /api/Products
```