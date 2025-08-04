from mcp_server.agents.crypto_analyst import CryptoAnalyst
import requests
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

# Debug: verificar se as variáveis estão sendo carregadas
print("GOOGLE_STUDIO_AI_API_KEY:", os.getenv("GOOGLE_STUDIO_AI_API_KEY"))
print("COINGECKO_API_KEY:", os.getenv("COINGECKO_API_KEY"))

app = FastAPI(title="Crypto MCP Server", version="1.0.0")

class CryptoMCPServer:

    api_base_url: str
    coingecko_api_key: str

    def __init__(self):
        self.api_base_url = "https://api.coingecko.com/api/v3"                  
        self.coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    
    def _get_crypto_informations(self, crypto_id: str):
        url = f"{self.api_base_url}/coins/{crypto_id}"

        params = {
            "ids": 'bitcoin',
            "vs_currencies": "brl",
            "include_24hr_change": "true"
        }

        headers = {
            "x-cg-demo-api-key": self.coingecko_api_key
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        return data

    def run(self):
        self._get_crypto_informations("bitcoin")

@app.get("/")
async def root():
    return {"message": "Crypto MCP Server is running!"}

@app.get("/analyze-crypto/{crypto_id}")
async def analyze_crypto(crypto_id: str):
    server = CryptoMCPServer()
    crypto_data = server._get_crypto_informations(crypto_id)
    crypto_analyst = CryptoAnalyst()
    analysis = await crypto_analyst.analyze_crypto_price(crypto_data)
    return analysis

if __name__ == "__main__":
    server = CryptoMCPServer()
    server.run()