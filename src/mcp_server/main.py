from mcp.server.fastmcp import FastMCP
from mcp_server.agents.crypto_analyst import CryptoAnalyst
import requests

class CryptoMCPServer:

    mcp: FastMCP
    api_base_url: str

    def __init__(self):
        self.api_base_url = "https://api.coingecko.com/api/v3"
        self.mcp = FastMCP(
            tools=[self.get_crypto_informations]
        )                    

    @mcp.tool
    def get_crypto_informations(self, crypto_id: str):
        url = f"{self.api_base_url}/coins/{crypto_id}"

        params = {
            "ids": 'bitcoin',
            "vs_currencies": "brl",
            "include_24hr_change": "true"
        }
        response = requests.get(url, params=params)
        data = response.json()
        print(data)
        return data

    def run(self):
        self.mcp.run()

if __name__ == "__main__":
    server = CryptoMCPServer()
    server.run()