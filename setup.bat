@echo off
REM Personal Finance Chatbot - Windows Development Setup Script

echo 🚀 Setting up Personal Finance Chatbot Development Environment...

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv .venv

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    echo ⚙️  Creating .env file from template...
    copy .env.example .env
    echo 🔑 Please edit .env file with your IBM Watson credentials!
)

echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your IBM Watson credentials
echo 2. Start the backend: python main.py
echo 3. Start the frontend: streamlit run streamlit_app.py
echo.
echo 🌐 Access the application at: http://localhost:8501
