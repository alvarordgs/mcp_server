import os
from google import genai
from typing import Dict, Any

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
        genai.configure(api_key=api_key)
        self.client = genai.Client()
        

    def analyze_crypto_price(self, data: Dict[str, Any]) -> str:

        print(data)

        return "test"

        crypto_info = f"""
        CRYPTOCURRENCY DATA:
        - Name: {data.get("name", "Unknown")}
        - Current Price: {data.get("price", "N/A")}
        - 24h Change: {data.get("change_24h", "N/A")}
        - Market Cap: {data.get("market_cap", "N/A")}
        - Volume (24h): {data.get("volume_24h", "N/A")}
        - Circulating Supply: {data.get("circulating_supply", "N/A")}
        - All-time High: {data.get("ath", "N/A")}
        - All-time Low: {data.get("atl", "N/A")}
        """
        
        prompt = self.base_prompt + crypto_info + "\n\nPlease provide a comprehensive analysis based on this data."
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt]
        )
        return response.text