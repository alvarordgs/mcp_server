# Crypto MCP Server

A Model Context Protocol (MCP) server that provides cryptocurrency analysis tools using CoinGecko API data and AI-powered insights.

## Features

- **Real-time Crypto Data**: Get current prices, market cap, volume, and 24h changes
- **AI-Powered Analysis**: Comprehensive cryptocurrency analysis with risk assessment
- **Multi-Coin Support**: Analyze multiple cryptocurrencies simultaneously
- **MCP Protocol**: Standardized interface for AI assistants and tools

## Available Tools

### 1. `get_crypto_price`
Get current price and market data for a specific cryptocurrency.

**Parameters:**
- `coin_id` (string): The coin ID (e.g., 'bitcoin', 'ethereum', 'cardano')

**Example:**
```json
{
  "name": "get_crypto_price",
  "arguments": {
    "coin_id": "bitcoin"
  }
}
```

### 2. `analyze_crypto`
Get AI-powered analysis of cryptocurrency data with different analysis types.

**Parameters:**
- `coin_id` (string): The coin ID to analyze
- `analysis_type` (string, optional): Type of analysis ("price", "trend", or "comprehensive")

**Example:**
```json
{
  "name": "analyze_crypto",
  "arguments": {
    "coin_id": "ethereum",
    "analysis_type": "comprehensive"
  }
}
```

### 3. `get_market_data`
Get comprehensive market data for multiple cryptocurrencies.

**Parameters:**
- `coin_ids` (array): List of coin IDs
- `vs_currency` (string, optional): Target currency (default: "usd")

**Example:**
```json
{
  "name": "get_market_data",
  "arguments": {
    "coin_ids": ["bitcoin", "ethereum", "cardano"],
    "vs_currency": "usd"
  }
}
```

## Setup

### Prerequisites

- Python 3.12.4 or higher
- Poetry (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mcp_server
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_STUDIO_AI_API_KEY=your_google_ai_api_key_here
   ```

4. **Install the package:**
   ```bash
   poetry install
   ```

## Usage

### Running the MCP Server

The server runs using stdio protocol, which is the standard for MCP servers:

```bash
poetry run python -m mcp_server.main
```

### Integration with MCP Clients

To use this server with MCP-compatible clients (like Claude Desktop, etc.):

1. **Add to your MCP configuration:**
   ```json
   {
     "mcpServers": {
       "crypto-analysis": {
         "command": "python",
         "args": ["-m", "mcp_server.main"],
         "env": {
           "GOOGLE_STUDIO_AI_API_KEY": "${GOOGLE_STUDIO_AI_API_KEY}"
         }
       }
     }
   }
   ```

2. **Restart your MCP client**

3. **Use the tools in your AI assistant:**
   - Ask for crypto prices: "What's the current price of Bitcoin?"
   - Request analysis: "Analyze Ethereum's market position"
   - Compare multiple coins: "Compare Bitcoin, Ethereum, and Cardano"

## API Endpoints

The server uses the CoinGecko API for real-time cryptocurrency data:

- **Base URL**: `https://api.coingecko.com/api/v3`
- **Rate Limits**: Free tier with reasonable limits
- **Data Sources**: Real-time market data from multiple exchanges

## Development

### Project Structure

```
mcp_server/
├── src/
│   └── mcp_server/
│       ├── __init__.py
│       └── main.py          # Main MCP server implementation
├── pyproject.toml           # Dependencies and project config
├── mcp-config.json         # MCP client configuration
└── README.md              # This file
```

### Adding New Tools

To add a new tool to the MCP server:

1. **Define the tool in `setup_handlers()`:**
   ```python
   Tool(
       name="your_tool_name",
       description="Tool description",
       inputSchema={
           "type": "object",
           "properties": {
               "param1": {"type": "string"}
           },
           "required": ["param1"]
       }
   )
   ```

2. **Add the handler in `handle_call_tool()`:**
   ```python
   elif name == "your_tool_name":
       return await self.your_tool_method(arguments)
   ```

3. **Implement the tool method:**
   ```python
   async def your_tool_method(self, arguments: Dict[str, Any]) -> CallToolResult:
       # Your implementation here
       return CallToolResult(
           content=[TextContent(type="text", text="Your result")]
       )
   ```

## Error Handling

The server includes comprehensive error handling:

- **API Errors**: Graceful handling of CoinGecko API failures
- **Invalid Input**: Validation of tool parameters
- **Network Issues**: Timeout and connection error handling
- **Missing Data**: Fallback values for unavailable data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Create an issue in the repository
- Check the MCP documentation: https://modelcontextprotocol.io/
- Review CoinGecko API documentation: https://www.coingecko.com/en/api

