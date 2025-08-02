# Personal Finance Chatbot - Setup Guide

## 🚀 Project Overview

This is a complete implementation of the Personal Finance Chatbot as specified in your PDF document. The project uses:

- **FastAPI**: Backend API framework
- **Streamlit**: Interactive web frontend
- **IBM Watson NLU**: Natural language understanding
- **IBM Watsonx.ai Granite**: Large language model for financial advice
- **LangChain**: AI orchestration framework

## 📁 Project Structure

```
finance-bot/
├── app/                    # Core application modules
│   ├── __init__.py
│   ├── ibm_api.py         # IBM Watson API integration
│   ├── utils.py           # Prompt templates and utilities
│   ├── models.py          # Pydantic data models
│   └── routes.py          # FastAPI route handlers
├── main.py                # FastAPI application entry point
├── streamlit_app.py       # Streamlit frontend
├── test_app.py           # Test suite
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── setup.bat             # Windows setup script
├── setup.sh              # Unix setup script
└── README.md             # Comprehensive documentation
```

## ⚙️ Setup Instructions

### 1. Environment Setup

#### Option A: Automatic Setup (Recommended)
**Windows:**
```cmd
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

#### Option B: Manual Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

### 2. IBM Watson Credentials

Edit the `.env` file with your IBM Watson credentials:

```env
# IBM Watson NLU
NLU_KEY=your_watson_nlu_api_key
NLU_URL=https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id

# IBM Watsonx.ai
WATSONX_KEY=your_watsonx_api_key
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-2-8b-instruct
PROJECT_ID=your_watsonx_project_id
```

### 3. Get IBM Watson Credentials

#### Watson NLU Setup:
1. Go to [IBM Cloud](https://cloud.ibm.com/)
2. Create a Watson Natural Language Understanding service
3. Get your API key and service URL from the credentials section

#### Watsonx.ai Setup:
1. Access [IBM Watsonx.ai](https://www.ibm.com/products/watsonx-ai)
2. Create a new project
3. Generate API credentials
4. Copy your project ID, API key, and endpoint URL

## 🚀 Running the Application

### Method 1: Using Python directly

**Terminal 1 - Start Backend:**
```bash
python main.py
# Backend will run on http://localhost:8000
```

**Terminal 2 - Start Frontend:**
```bash
streamlit run streamlit_app.py
# Frontend will run on http://localhost:8501
```

### Method 2: Using Uvicorn (Production-ready)

**Terminal 1 - Start Backend:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 - Start Frontend:**
```bash
streamlit run streamlit_app.py
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest test_app.py -v
```

Run with coverage:
```bash
python -m pytest test_app.py --cov=app --cov-report=html
```

## 🌐 Using the Application

1. **Access the frontend**: http://localhost:8501
2. **API documentation**: http://localhost:8000/docs
3. **Alternative API docs**: http://localhost:8000/redoc

### Features Available:

1. **🧠 NLU Analysis**
   - Analyze sentiment and extract keywords from financial text
   - Test with: "I'm struggling to save money each month"

2. **💬 Q&A Chat**
   - Ask financial questions with persona selection
   - Example: "How can I save while repaying student loans?"

3. **📊 Budget Summary**
   - Enter income, expenses, and savings goals
   - Get comprehensive budget analysis

4. **💡 Spending Insights**
   - Advanced spending pattern analysis
   - Set financial goals and get achievability assessment

## 🎯 Example Usage Scenarios

### Scenario 1: Student Budget Help
```json
{
  "question": "How can I save money as a student?",
  "persona": "student"
}
```

### Scenario 2: Professional Budget Analysis
```json
{
  "income": 5000,
  "expenses": {
    "rent": 1500,
    "food": 600,
    "transportation": 300,
    "entertainment": 200
  },
  "savings_goal": 1000,
  "persona": "professional"
}
```

### Scenario 3: Goal Planning
```json
{
  "goals": [
    {
      "name": "Emergency Fund",
      "amount": 10000,
      "deadline_months": 12
    },
    {
      "name": "Vacation",
      "amount": 3000,
      "deadline_months": 6
    }
  ]
}
```

## 🔧 Development

### Code Structure
- **`app/ibm_api.py`**: IBM Watson integration with caching and error handling
- **`app/utils.py`**: Persona-driven prompt templates and financial calculations
- **`app/models.py`**: Pydantic models for request/response validation
- **`app/routes.py`**: FastAPI endpoints with comprehensive error handling
- **`main.py`**: FastAPI application with CORS and middleware configuration
- **`streamlit_app.py`**: Modern UI with frosted glass design and responsive layout

### Key Features Implemented
- ✅ **Persona-driven responses** (Student vs Professional)
- ✅ **NLU-enhanced prompts** with sentiment and keyword analysis
- ✅ **Budget summarization** with financial health assessment
- ✅ **Spending insights** with goal achievability analysis
- ✅ **Risk assessment** with spending ratio warnings
- ✅ **Responsive UI** with modern frosted glass design
- ✅ **Comprehensive error handling** and user feedback
- ✅ **API documentation** with OpenAPI/Swagger
- ✅ **Test coverage** for core functionality

## 🚨 Troubleshooting

### Common Issues:

1. **"Cannot connect to API server"**
   - Ensure FastAPI backend is running on port 8000
   - Check if port is already in use

2. **"IBM Watson API errors"**
   - Verify your API credentials in `.env`
   - Check IBM Cloud service status
   - Ensure you have sufficient API credits

3. **"Module not found"**
   - Activate your virtual environment
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **Streamlit connection issues**
   - Ensure backend is running first
   - Check CORS settings in `main.py`

### Debug Mode:
Add debug logging to track issues:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Additional Resources

- [IBM Watson NLU Documentation](https://cloud.ibm.com/apidocs/natural-language-understanding)
- [IBM Watsonx.ai Documentation](https://www.ibm.com/docs/en/watsonx/w-and-w/2.1.0)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://langchain.readthedocs.io/)

## 🎉 Success!

You now have a fully functional Personal Finance Chatbot that:
- Provides intelligent financial advice using IBM Watson AI
- Adapts responses based on user persona (student/professional)
- Analyzes budgets and spending patterns
- Tracks financial goals and provides actionable insights
- Features a modern, responsive web interface

Start the application and begin exploring your AI-powered financial advisor!
