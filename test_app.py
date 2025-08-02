import pytest
import json
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from main import app

client = TestClient(app)

class TestAPI:
    """Test suite for Personal Finance Chatbot API"""
    
    def test_root_endpoint(self):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "Personal Finance Chatbot API" in data["message"]
        assert data["version"] == "1.0.0"
    
    def test_health_check(self):
        """Test the health check endpoint"""
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
    
    @patch('app.ibm_api.analyze_nlu')
    def test_nlu_analysis(self, mock_analyze_nlu):
        """Test NLU analysis endpoint"""
        # Mock NLU response
        mock_analyze_nlu.return_value = {
            "sentiment": {"document": {"label": "positive", "score": 0.8}},
            "keywords": ["money", "savings"],
            "entities": ["monthly"]
        }
        
        response = client.post("/api/v1/nlu", json={
            "text": "I want to save money monthly"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "sentiment" in data["data"]
    
    @patch('app.ibm_api.invoke_llm')
    @patch('app.ibm_api.analyze_nlu')
    def test_generate_response(self, mock_analyze_nlu, mock_invoke_llm):
        """Test the generate response endpoint"""
        # Mock NLU and LLM responses
        mock_analyze_nlu.return_value = {
            "sentiment": {"document": {"label": "neutral", "score": 0.0}},
            "keywords": ["saving", "money"],
            "entities": []
        }
        mock_invoke_llm.return_value = "Here are some tips for saving money..."
        
        response = client.post("/api/v1/generate", json={
            "question": "How can I save money?",
            "persona": "student"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "response" in data["data"]
    
    @patch('app.ibm_api.generate_budget_summary')
    def test_budget_summary(self, mock_generate_budget_summary):
        """Test budget summary endpoint"""
        # Mock budget summary response
        mock_generate_budget_summary.return_value = {
            "response": "Budget summary analysis...",
            "prompt": "Budget prompt...",
            "error": None
        }
        
        response = client.post("/api/v1/budget-summary", json={
            "income": 3000,
            "expenses": {
                "rent": 1000,
                "food": 400,
                "transportation": 200
            },
            "savings_goal": 500,
            "currency_symbol": "$",
            "persona": "student"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "summary" in data["data"]
    
    @patch('app.ibm_api.generate_spending_insights')
    def test_spending_insights(self, mock_generate_spending_insights):
        """Test spending insights endpoint"""
        # Mock spending insights response
        mock_generate_spending_insights.return_value = {
            "response": "Spending insights analysis...",
            "prompt": "Insights prompt...",
            "error": None
        }
        
        response = client.post("/api/v1/spending-insights", json={
            "income": 4000,
            "expenses": {
                "rent": 1200,
                "groceries": 300,
                "dining_out": 200
            },
            "savings_goal": 600,
            "goals": [
                {
                    "name": "Emergency Fund",
                    "amount": 10000,
                    "deadline_months": 12
                }
            ],
            "currency_symbol": "$",
            "persona": "professional"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "insights" in data["data"]
    
    def test_invalid_request_data(self):
        """Test handling of invalid request data"""
        response = client.post("/api/v1/nlu", json={
            "invalid_field": "test"
        })
        
        assert response.status_code == 422  # Validation error

class TestUtils:
    """Test suite for utility functions"""
    
    def test_calculate_financial_metrics(self):
        """Test financial metrics calculation"""
        from app.utils import calculate_financial_metrics
        
        budget_data = {
            "income": 3000,
            "expenses": {
                "rent": 1000,
                "food": 400,
                "transportation": 200
            },
            "savings_goal": 500
        }
        
        metrics = calculate_financial_metrics(budget_data)
        
        assert metrics["annual_income"] == 36000
        assert metrics["total_monthly_expenses"] == 1600
        assert metrics["disposable_income"] == 1400
        assert metrics["surplus_after_savings"] == 900
    
    def test_build_simple_prompt(self):
        """Test simple prompt building"""
        from app.utils import build_simple_prompt
        
        prompt = build_simple_prompt("How to save money?", "student")
        
        assert "financial advisor for students" in prompt
        assert "How to save money?" in prompt
        assert "Response:" in prompt
    
    def test_persona_prompt_selection(self):
        """Test persona-based prompt selection"""
        from app.utils import build_budget_prompt
        
        budget_data = {
            "income": 3000,
            "expenses": {"rent": 1000},
            "savings_goal": 500,
            "persona": "professional"
        }
        
        prompt = build_budget_prompt(budget_data)
        
        # Should contain professional-specific language
        assert "strategic" in prompt.lower() or "professional" in prompt.lower()

if __name__ == "__main__":
    pytest.main([__file__])
