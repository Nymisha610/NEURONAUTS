#!/bin/bash

# Personal Finance Chatbot - Development Setup Script

echo "🚀 Setting up Personal Finance Chatbot Development Environment..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "🔑 Please edit .env file with your IBM Watson credentials!"
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your IBM Watson credentials"
echo "2. Start the backend: python main.py"
echo "3. Start the frontend: streamlit run streamlit_app.py"
echo ""
echo "🌐 Access the application at: http://localhost:8501"
