import os
from google import genai
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class CryptoAnalyst():

    base_prompt = """
    You are an expert cryptocurrency analyst with deep knowledge of market dynamics, technical analysis, and fundamental factors affecting crypto prices.
    
    Your task is to analyze cryptocurrency data and provide comprehensive insights including:
    - Current price analysis and market position
    - Key factors influencing the price movement
    - Risk assessment and market sentiment
    - Potential short-term outlook (1-7 days)
    - Important technical levels to watch
    
    Provide clear, actionable insights in a professional tone. Focus on data-driven analysis rather than speculation.
    """

    def __init__(self):
        api_key = os.getenv("GOOGLE_STUDIO_AI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        

    async def analyze_crypto_price(self, data: Dict[str, Any]) -> str:
        crypto_info = f"""
        CRYPTOCURRENCY DATA:
        - Name: {data.get("name", "Unknown")}
        - Current Price: {data.get("market_data", {}).get("current_price", {}).get("usd", "N/A")}
        - 24h Change: {data.get("market_data", {}).get("price_change_percentage_24h", "N/A")}
        - Market Cap: {data.get("market_data", {}).get("market_cap_change_24h", "N/A")}
        - Volume (24h): {data.get("market_data", {}).get("total_volume", {}).get("usd", "N/A")}
        - Circulating Supply: {data.get("circulating_supply", "N/A")}
        - All-time High: {data.get("market_data", {}).get("ath", {}).get("usd", "N/A")}
        - All-time Low: {data.get("market_data", {}).get("atl", {}).get("usd", "N/A")}
        """
        
        prompt = self.base_prompt + crypto_info + "\n\nPlease provide a comprehensive analysis of the crypto currency based on this data."
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt]
        )
        return response.text