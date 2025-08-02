# Personal Finance Chatbot

**Intelligent Guidance for Savings, Taxes, and Investments**

A sophisticated AI-powered financial advisor built with IBM Watson AI services, FastAPI, and Streamlit. This chatbot provides personalized financial guidance tailored to different user personas (students and professionals) using advanced natural language processing and generation capabilities.

## 🌟 Features

### Core Capabilities
- **NLU Analysis**: Sentiment analysis, keyword extraction, and entity recognition using IBM Watson NLU
- **Personalized Q&A**: Context-aware financial advice adapted to user personas
- **Budget Summarization**: Comprehensive monthly budget analysis with actionable insights
- **Spending Insights**: Deep behavioral analysis of spending patterns and goal tracking

### AI-Powered Intelligence
- **IBM Granite 3.2-8B Instruct Model**: Advanced language generation for financial advice
- **Watson Natural Language Understanding**: Semantic analysis of user queries
- **Persona-Driven Responses**: Tailored advice for students vs. professionals
- **Goal-Based Planning**: Financial goal assessment and achievement tracking

## 🏗️ Architecture

```
📦 finance-bot/
├── 📁 app/
│   ├── __init__.py
│   ├── ibm_api.py          # IBM Watson API integration
│   ├── utils.py            # Prompt templates and utilities
│   ├── models.py           # Pydantic data models
│   └── routes.py           # FastAPI route handlers
├── main.py                 # FastAPI application entry point
├── streamlit_app.py        # Streamlit frontend application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- IBM Cloud account with Watson services
- API keys for IBM Watson NLU and Watsonx.ai

### 1. Clone and Setup
```bash
git clone <repository-url>
cd finance-bot
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your IBM Watson credentials
```

Required environment variables:
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

### 3. Start the Backend API
```bash
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Launch the Frontend
```bash
streamlit run streamlit_app.py
```

## 🔧 IBM Cloud Setup

### Watson Natural Language Understanding
1. Go to [IBM Cloud](https://cloud.ibm.com/)
2. Create a Watson NLU service instance
3. Generate API credentials
4. Copy the API key and service URL

### Watsonx.ai Setup
1. Access [IBM Watsonx.ai](https://www.ibm.com/products/watsonx-ai)
2. Create a new project
3. Generate API credentials
4. Note your project ID and model endpoint

## 📱 User Interface

### Home Dashboard
- **Frosted glass design** with gradient background
- **Four main features** accessible via intuitive buttons
- **Responsive layout** optimized for both desktop and mobile

### Feature Pages
1. **NLU Analysis**: Real-time sentiment and keyword analysis
2. **Q&A Chat**: Interactive financial Q&A with persona selection
3. **Budget Summary**: Comprehensive budget analysis with visual insights
4. **Spending Insights**: Advanced spending pattern analysis with goal tracking

## 🤖 AI Components

### Persona-Driven Responses
- **Student Persona**: Simple, educational financial advice focused on budgeting basics
- **Professional Persona**: Advanced strategic guidance with investment considerations

### Advanced Prompt Engineering
- **Context-Aware Prompts**: Incorporate NLU insights for personalized responses
- **Structured Output**: Consistent formatting for better user experience
- **Domain Constraints**: Financial-focused responses with safety guardrails

### Financial Analysis Features
- **Budget Categorization**: Automatic expense classification (needs vs. wants)
- **Risk Assessment**: Spending ratio analysis and red flag identification
- **Goal Tracking**: Timeline analysis for financial objectives
- **Optimization Recommendations**: Actionable cost-saving strategies

## 🔌 API Endpoints

### Core Endpoints
- `POST /api/v1/nlu` - Text analysis with Watson NLU
- `POST /api/v1/generate` - General financial Q&A
- `POST /api/v1/budget-summary` - Budget analysis and summary
- `POST /api/v1/spending-insights` - Advanced spending analysis
- `GET /api/v1/health` - Health check endpoint

### Example API Usage
```python
import requests

# Budget Summary Example
response = requests.post("http://localhost:8000/api/v1/budget-summary", json={
    "income": 4000,
    "expenses": {
        "rent": 1200,
        "food": 400,
        "transportation": 200,
        "entertainment": 150
    },
    "savings_goal": 500,
    "persona": "professional"
})
```

## 💻 Development

### Code Structure
- **Modular Design**: Clear separation between API logic, AI integration, and UI
- **Error Handling**: Comprehensive error management with user-friendly messages
- **Caching**: LRU cache for model initialization to improve performance
- **Type Safety**: Full Pydantic model validation for API requests/responses

### Testing
```bash
# Run tests
pytest

# Code formatting
black .

# Linting
flake8 .
```

## 🎯 Use Cases & Scenarios

### Scenario 1: Student Loan Management
*"How can I save while repaying student loans?"*
- Analyzes query sentiment and financial context
- Provides step-by-step budgeting strategies
- Offers student-specific money-saving tips

### Scenario 2: Budget Analysis
- Input monthly income and expenses
- Receive comprehensive spending breakdown
- Get personalized recommendations for optimization

### Scenario 3: Goal Planning
- Set financial goals (emergency fund, major purchases, vacations)
- Analyze achievability based on current spending
- Receive timeline and savings recommendations

### Scenario 4: Spending Pattern Recognition
- Identify top spending categories
- Highlight unconscious spending habits
- Suggest targeted areas for cost reduction

### Scenario 5: Financial Coaching
- Receive actionable next steps after budget review
- Get guidance on expense reduction strategies
- Learn about effective savings techniques

### Scenario 6: Emotional Financial Support
- Discuss financial stress and concerns
- Receive empathetic, supportive responses
- Get confidence-building financial advice

## 🚀 Deployment

### Local Development
1. Start FastAPI backend: `python main.py`
2. Launch Streamlit frontend: `streamlit run streamlit_app.py`
3. Access application at `http://localhost:8501`

### Production Deployment
- **Backend**: Deploy FastAPI with Gunicorn/Uvicorn
- **Frontend**: Use Streamlit Community Cloud or containerize with Docker
- **Environment**: Ensure all IBM Watson credentials are securely configured

## 🔐 Security & Privacy

- **API Key Security**: Environment-based credential management
- **Data Privacy**: No persistent storage of user financial data
- **Input Validation**: Comprehensive request validation with Pydantic
- **Error Handling**: Graceful error responses without exposing internal details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and add tests
4. Run tests and ensure code quality: `pytest && black . && flake8 .`
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/new-feature`
7. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IBM Watson AI**: For providing powerful natural language processing capabilities
- **IBM Granite Model**: For advanced financial reasoning and generation
- **FastAPI**: For the robust API framework
- **Streamlit**: For the intuitive frontend framework
- **LangChain**: For AI orchestration and integration

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Review the documentation
- Check the IBM Watson documentation for API-specific questions

---

**Built with ❤️ using IBM Watson AI, FastAPI, and Streamlit**
