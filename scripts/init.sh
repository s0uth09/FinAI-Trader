#!/bin/bash

# Init script for FinAI Trader setup

echo "Starting FinAI Trader setup..."

# Check for dependencies
if ! command -v docker &> /dev/null; then
    echo "Docker is required. Please install it."
    exit 1
fi

if ! command -v make &> /dev/null; then
    echo "Make is required. Please install it."
    exit 1
fi

# Copy .env.example to .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file. Please fill in your API keys."
else
    echo ".env file already exists."
fi

# Install Python dependencies
make install

# Install pre-commit hooks
pre-commit install

# Build and start dev environment
make dev

echo "Setup complete! Access the app at http://localhost:8000"
echo "Run 'make test' to verify."