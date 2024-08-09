from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

API_KEY = '1e836c3b9510bc25ea5664b6'  # Replace w ur personal API key


class ConversionRequest(BaseModel):
    amount: float
    currency: str
    target_currency: str


class ConversionResponse(BaseModel):
    amount: float


@app.post("/convert", response_model=ConversionResponse)
async def convert_currency(request: ConversionRequest):
    try:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{request.currency}")
        response_data = response.json()

        # Debugging info
        print(f"API Status Code: {response.status_code}")
        print(f"API Response: {response_data}")

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response_data.get('error', 'Unknown error'))

        rates = response_data.get("conversion_rates")
        if not rates or request.target_currency not in rates:
            raise HTTPException(status_code=400, detail="Invalid target currency")

        converted_amount = request.amount * rates[request.target_currency]
        return ConversionResponse(amount=converted_amount)

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching conversion rates")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
