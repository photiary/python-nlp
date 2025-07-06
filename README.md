# Python Starter Kit

A modern Python development environment with Docker Compose setup.

## Features

- 🐍 Python 3.12 development environment
- 🐳 Docker Compose for easy development setup
- 🔧 Hot reload support for development
- 📦 Virtual environment management
- 🔍 Debug port support

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-starter-kit
   ```

2. **Start the development environment**
   ```bash
   docker-compose up -d
   ```

3. **Access your application**
   - App: http://localhost:8000

### Available Commands

```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d app

# View logs
docker-compose logs -f app

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Rebuild containers
docker-compose build --no-cache

# Execute commands in running container
docker-compose exec app python main.py
```

## Project Structure

```
python-starter-kit/
├── app/
│   ├── main.py          # Main application file
│   └── requirements.txt # Python dependencies
├── .devcontainer/
│   ├── Dockerfile       # Development container definition
│   ├── devcontainer.json # VS Code devcontainer configuration
│   └── post-create.sh   # Post-creation setup script
├── data/                # Data directory (mounted in container)
├── docker-compose.yml   # Docker Compose configuration
└── README.md
```

## Services

### App Service
- **Port**: 8000
- **Hot Reload**: Enabled in development
- **Debug Port**: 5678 (for debugging)

## Development

### Adding Dependencies

1. Add packages to `app/requirements.txt`
2. Rebuild the container:
   ```bash
   docker-compose build app
   docker-compose up -d app
   ```

## License

This project is licensed under the MIT License.