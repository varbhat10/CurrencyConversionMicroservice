# Currency Conversion Microservice

## Overview

This microservice allows you to convert an amount from one currency to another using real-time exchange rates.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/currency-converter.git
    cd currency-converter
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn requests
    ```

4. Replace `YOUR_EXCHANGE_RATE_API_KEY` in `main.py` with your actual API key from [ExchangeRate-API](https://www.exchangerate-api.com).

### Running the Microservice

Start the FastAPI server:

```bash
uvicorn main:app --reload
```
The server will run on http://localhost:8000.

### Requesting Data
Endpoint
- URL: http://localhost:8000/convert
- Method: POST
- Content-Type: application/json

Example Request
```bash
{
  "amount": 300,
  "currency": "USD",
  "target_currency": "JPY"
}
```
Example Call Using curl
```bash
curl -X POST http://localhost:8000/convert -H "Content-Type: application/json" -d '{"amount":300,"currency":"USD","target_currency":"JPY"}'
```

Example Call Using Python Requests
```bash
import requests

url = "http://localhost:8000/convert"
payload = {
    "amount": 300,
    "currency": "USD",
    "target_currency": "JPY"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### Receiving Data

Response Format
- Content-Type: application/json

Example Response
```bash
{
  "amount": 2342
}
```
### UML Sequence Diagram
![uml-diagram png](https://github.com/user-attachments/assets/6054afee-ee8e-4007-a7d6-b5041710c309)

Diagram Explanation
1. Client Program sends a conversion request:
- POST /convert (amount, currency, target_currency)

2. CurrencyConversionService requests conversion rate from External API:
- GET /latest/currency (currency)

3. External API responds with conversion rates:
- Response (conversion_rates)
4. CurrencyConversionService calculates the converted amount:
- Calculation logic
5. CurrencyConversionService sends the converted amount back to the Client Program:
- Response (converted_amount)

