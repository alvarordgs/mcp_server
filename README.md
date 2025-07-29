# MCP Server

A proof of concept MCP (Model Context Protocol) server that demonstrates structured backend development and integration with external APIs. This project serves as a testing ground for MCP server building, structured backend architecture, and other development practices.

## 🎯 Project Overview

This MCP server is designed to consume data from the CoinGecko API using GenAI capabilities, providing a structured approach to building scalable and maintainable backend services.

## 🚀 Features

- **MCP Server Implementation**: Core MCP server functionality for model context management
- **CoinGecko API Integration**: Real-time cryptocurrency data consumption
- **Structured Backend**: Well-organized, maintainable codebase architecture
- **FastAPI Framework**: Modern, high-performance web framework
- **Pydantic Models**: Type-safe data validation and serialization
- **Testing Infrastructure**: Comprehensive testing setup for MCP server development

## 📋 Prerequisites

- Python 3.12.4 or higher
- Poetry (for dependency management)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mcp_server
   ```

2. **Install dependencies using Poetry**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

## 🏗️ Project Structure

```
mcp_server/
├── pyproject.toml          # Project configuration and dependencies
├── README.md              # This file
├── src/                   # Source code directory
│   └── mcp_server/       # Main package
├── tests/                # Test files
└── docs/                 # Documentation
```

## 🔧 Development

### Running the Server

```bash
# Development mode
make dev

# Production mode
make run
```

### Testing

```bash
# Run all tests
make test

# Run tests with coverage
poetry run pytest --cov=src/mcp_server

# Run specific test file
poetry run pytest tests/test_mcp_server.py
```

### Code Quality

```bash
# Format code
poetry run black src/ tests/

# Lint code
poetry run flake8 src/ tests/

# Type checking
poetry run mypy src/
```

## 📦 Dependencies

### Core Dependencies
- **FastAPI** (>=0.116.1,<0.117.0): Modern web framework for building APIs
- **Pydantic** (>=2.11.7,<3.0.0): Data validation and settings management

### Development Dependencies
- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting
- **mypy**: Static type checking

## 🔌 MCP Server Features

### Model Context Protocol
This server implements the Model Context Protocol, enabling:
- Structured data exchange between AI models and external services
- Context-aware API interactions
- Scalable model integration patterns

### CoinGecko Integration
- Real-time cryptocurrency data fetching
- Market data analysis capabilities
- Historical price data access

## 🧪 Testing Strategy

The project includes comprehensive testing for:
- MCP server functionality
- API endpoint validation
- Data model integrity
- Integration testing with external APIs
- Performance benchmarking

## 📚 Documentation

- API documentation available at `/docs` when running the server
- Interactive API explorer at `/redoc`
- Code documentation in docstrings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **MatheusHMR** - *Initial work* - [matheus.henrimr@gmail.com](mailto:matheus.henrimr@gmail.com)
- **alvarordgs** - *Initial work* - [alvarordgs98@gmail.com](mailto:alvarordgs98@gmail.com)

## 🆘 Support

For support and questions:
- Open an issue on GitHub
- Contact the maintainers via email

## 🔄 Version History

- **v0.1.0** - Initial release with basic MCP server functionality and CoinGecko API integration

---

**Note**: This is a proof of concept project for testing MCP server building, structured backend development, and related technologies. Use for educational and development purposes.

