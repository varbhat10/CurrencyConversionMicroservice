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

## Running the Microservice

Start the FastAPI server:

```bash
uvicorn main:app --reload

![uml](https://github.com/user-attachments/assets/bce80189-4005-42d9-adcf-664d4b2a523a)

