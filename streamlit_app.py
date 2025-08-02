import streamlit as st
import requests
import json
import base64
from typing import Dict, Any
import os

# Page configuration
st.set_page_config(
    page_title="Personal Finance Chatbot",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# API Configuration
API_BASE_URL = "http://127.0.0.1:8000/api/v1"

def set_background():
    """Set custom background and styling"""
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .white-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .frosted-glass {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .title {
        color: white;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.37);
        text-align: center;
        color: white;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .json-output {
        background: rgba(0, 0, 0, 0.8);
        color: #00ff00;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        max-height: 600px;
        overflow-y: auto;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def container_wrapper(func):
    """Wrapper function to add consistent styling to content"""
    def wrapper(*args, **kwargs):
        with st.container():
            st.markdown('<div class="white-box">', unsafe_allow_html=True)
            result = func(*args, **kwargs)
            st.markdown('</div>', unsafe_allow_html=True)
            return result
    return wrapper

def make_api_request(endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Make API request to the backend"""
    try:
        response = requests.post(f"{API_BASE_URL}/{endpoint}", json=data, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Cannot connect to the API server. Please make sure the FastAPI server is running on port 8000."
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out. The server might be processing your request."
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API request failed: {str(e)}"
        }

def show_home_page():
    """Display the home page"""
    st.markdown('<div class="frosted-glass">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">💰 Personal Finance Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Intelligent Guidance for Savings, Taxes, and Investments</p>', unsafe_allow_html=True)
    
    st.write("""
    Welcome to your AI-powered financial advisor! This chatbot leverages IBM Watson AI to provide 
    personalized financial guidance tailored to your needs. Whether you're a student managing a tight 
    budget or a professional planning for the future, we're here to help.
    """)
    
    # Demo notice
    st.info("""
    🧪 **Demo Mode Active**: This application is currently running in demo mode with sample responses. 
    To enable full IBM Watson AI functionality, please configure your API keys in the `.env` file.
    The demo responses showcase the application's capabilities with realistic financial advice.
    """)
    
    # Feature buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🧠 NLU Analysis", use_container_width=True):
            st.session_state.page = "nlu"
        
        if st.button("💬 Q&A Chat", use_container_width=True):
            st.session_state.page = "generate"
    
    with col2:
        if st.button("📊 Budget Summary", use_container_width=True):
            st.session_state.page = "budget-summary"
        
        if st.button("💡 Spending Insights", use_container_width=True):
            st.session_state.page = "spending-insights"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Instructions
    st.markdown('<div class="white-box">', unsafe_allow_html=True)
    st.markdown("### 🚀 How to Get Started")
    st.write("""
    1. **NLU Analysis**: Analyze the sentiment and key topics in your financial questions
    2. **Q&A Chat**: Ask any financial question and get personalized advice
    3. **Budget Summary**: Get a comprehensive analysis of your monthly budget
    4. **Spending Insights**: Receive detailed insights about your spending patterns and goals
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def show_nlu_page():
    """Display NLU Analysis page"""
    st.markdown('<div class="frosted-glass">', unsafe_allow_html=True)
    st.markdown('<h2 class="title">🧠 NLU Analysis</h2>', unsafe_allow_html=True)
    st.write("Analyze the sentiment, keywords, and entities in your financial text using IBM Watson NLU.")
    
    # Input section
    st.markdown("### Input Text")
    text_input = st.text_area(
        "Enter your financial question or concern:",
        placeholder='Example: "I\'m struggling to save money each month and wondering if there are ways to cut my spending."',
        height=100
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Send", use_container_width=True):
            if text_input.strip():
                with st.spinner("Analyzing text..."):
                    result = make_api_request("nlu", {"text": text_input})
                    st.session_state.nlu_result = result
                    # Force a rerun to show results immediately
                    st.rerun()
            else:
                st.warning("Please enter some text to analyze.")
    
    with col2:
        if st.button("🏠 Back", use_container_width=True):
            st.session_state.page = "home"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results section
    if 'nlu_result' in st.session_state and st.session_state.nlu_result:
        st.markdown('<div class="white-box">', unsafe_allow_html=True)
        st.markdown("### Analysis Results")
        
        if st.session_state.nlu_result.get("success", False):
            data = st.session_state.nlu_result.get("data", {})
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**Sentiment**")
                sentiment = data.get("sentiment", {}).get("document", {})
                st.write(f"Label: {sentiment.get('label', 'N/A')}")
                st.write(f"Score: {sentiment.get('score', 0):.2f}")
            
            with col2:
                st.markdown("**Keywords**")
                keywords = data.get("keywords", [])
                if keywords:
                    for kw in keywords[:5]:
                        st.write(f"• {kw}")
                else:
                    st.write("No keywords found")
            
            with col3:
                st.markdown("**Entities**")
                entities = data.get("entities", [])
                if entities:
                    for ent in entities[:5]:
                        st.write(f"• {ent}")
                else:
                    st.write("No entities found")
        else:
            st.error(f"Error: {st.session_state.nlu_result.get('error', 'Unknown error')}")
        
        st.markdown('</div>', unsafe_allow_html=True)

def show_generate_page():
    """Display Q&A Generation page"""
    st.markdown('<div class="frosted-glass">', unsafe_allow_html=True)
    st.markdown('<h2 class="title">💬 Q&A Chat</h2>', unsafe_allow_html=True)
    st.write("Ask any financial question and get personalized advice based on your persona.")
    
    # Input section
    col1, col2 = st.columns([3, 1])
    with col1:
        question = st.text_area(
            "Your Question:",
            placeholder='Example: "How can I save while repaying student loans?"',
            height=100
        )
    with col2:
        personal = st.selectbox(
            "Your Personal:",
            ["student", "professional", "general"],
            help="Select your financial profile for personalized advice"
        )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Send", use_container_width=True):
            if question.strip():
                with st.spinner("Generating response..."):
                    result = make_api_request("generate", {
                        "question": question,
                        "personal": personal
                    })
                    st.session_state.generate_result = result
                    st.rerun()
            else:
                st.warning("Please enter a question.")
    
    with col2:
        if st.button("🏠 Back", use_container_width=True):
            st.session_state.page = "home"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results section
    if 'generate_result' in st.session_state and st.session_state.generate_result:
        st.markdown('<div class="white-box">', unsafe_allow_html=True)
        st.markdown("### AI Response")
        
        if st.session_state.generate_result.get("success", False):
            data = st.session_state.generate_result.get("data", {})
            response = data.get("response", "")
            
            st.markdown("#### Financial Advice:")
            st.write(response)
            
            # Show analysis details in expandable section
            with st.expander("View Analysis Details"):
                nlu_data = data.get("nlu_analysis", {})
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Sentiment Analysis:**")
                    sentiment = nlu_data.get("sentiment", {}).get("document", {})
                    st.write(f"• {sentiment.get('label', 'neutral')} ({sentiment.get('score', 0):.2f})")
                
                with col2:
                    st.markdown("**Key Topics:**")
                    keywords = nlu_data.get("keywords", [])
                    for kw in keywords[:3]:
                        st.write(f"• {kw}")
        else:
            st.error(f"Error: {st.session_state.generate_result.get('error', 'Unknown error')}")
        
        st.markdown('</div>', unsafe_allow_html=True)

def show_budget_summary_page():
    """Display Budget Summary page"""
    st.markdown('<div class="frosted-glass">', unsafe_allow_html=True)
    st.markdown('<h2 class="title">📊 Budget Summary</h2>', unsafe_allow_html=True)
    st.write("Get a comprehensive analysis of your monthly budget with personalized recommendations.")
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Information")
        income = st.number_input("Monthly Income (₹)", min_value=0.0, value=3000.0, step=100.0)
        savings_goal = st.number_input("Monthly Savings Goal (₹)", min_value=0.0, value=500.0, step=50.0)
        persona = st.selectbox("Your Profile:", ["student", "professional"])
    
    with col2:
        st.markdown("### Monthly Expenses")
        rent = st.number_input("Rent (₹)", min_value=0.0, value=1000.0, step=50.0)
        food = st.number_input("Food & Groceries (₹)", min_value=0.0, value=400.0, step=25.0)
        transportation = st.number_input("Transportation (₹)", min_value=0.0, value=200.0, step=25.0)
        utilities = st.number_input("Utilities (₹)", min_value=0.0, value=150.0, step=25.0)
        entertainment = st.number_input("Entertainment (₹)", min_value=0.0, value=200.0, step=25.0)
        other = st.number_input("Other Expenses (₹)", min_value=0.0, value=100.0, step=25.0)
    
    expenses = {
        "rent": rent,
        "food": food,
        "transportation": transportation,
        "utilities": utilities,
        "entertainment": entertainment,
        "other": other
    }
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Generate Summary", use_container_width=True):
            with st.spinner("Generating budget summary..."):
                result = make_api_request("budget-summary", {
                    "income": income,
                    "expenses": expenses,
                    "savings_goal": savings_goal,
                    "currency_symbol": "₹",
                    "persona": persona
                })
                st.session_state.budget_result = result
                st.rerun()
    
    with col2:
        if st.button("🏠 Back", use_container_width=True):
            st.session_state.page = "home"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results section
    if 'budget_result' in st.session_state and st.session_state.budget_result:
        st.markdown('<div class="white-box">', unsafe_allow_html=True)
        st.markdown("### Budget Analysis")
        
        if st.session_state.budget_result.get("success", False):
            data = st.session_state.budget_result.get("data", {})
            summary = data.get("summary", "")
            
            st.markdown(summary)
        else:
            st.error(f"Error: {st.session_state.budget_result.get('error', 'Unknown error')}")
        
        st.markdown('</div>', unsafe_allow_html=True)

def show_spending_insights_page():
    """Display Spending Insights page"""
    st.markdown('<div class="frosted-glass">', unsafe_allow_html=True)
    st.markdown('<h2 class="title">💡 Spending Insights</h2>', unsafe_allow_html=True)
    st.write("Get detailed insights about your spending patterns and financial goals.")
    
    # Basic Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Information")
        income = st.number_input("Monthly Income (₹)", min_value=0.0, value=4000.0, step=100.0, key="insights_income")
        savings_goal = st.number_input("Monthly Savings Goal (₹)", min_value=0.0, value=600.0, step=50.0, key="insights_savings")
        persona = st.selectbox("Your Profile:", ["student", "professional"], key="insights_persona")
    
    with col2:
        st.markdown("### Monthly Expenses")
        rent = st.number_input("Rent (₹)", min_value=0.0, value=1200.0, step=50.0, key="insights_rent")
        groceries = st.number_input("Groceries (₹)", min_value=0.0, value=300.0, step=25.0)
        dining_out = st.number_input("Dining Out (₹)", min_value=0.0, value=200.0, step=25.0)
        transportation = st.number_input("Transportation (₹)", min_value=0.0, value=250.0, step=25.0, key="insights_transportation")
        entertainment = st.number_input("Entertainment (₹)", min_value=0.0, value=150.0, step=25.0, key="insights_entertainment")
        shopping = st.number_input("Shopping (₹)", min_value=0.0, value=200.0, step=25.0)
    
    # Financial Goals
    st.markdown("### Financial Goals")
    num_goals = st.number_input("Number of Goals", min_value=0, max_value=5, value=2, step=1)
    
    goals = []
    for i in range(int(num_goals)):
        col1, col2, col3 = st.columns(3)
        with col1:
            goal_name = st.text_input(f"Goal {i+1} Name:", value=f"Goal {i+1}", key=f"goal_name_{i}")
        with col2:
            goal_amount = st.number_input(f"Amount (₹):", min_value=0.0, value=5000.0, step=100.0, key=f"goal_amount_{i}")
        with col3:
            goal_deadline = st.number_input(f"Deadline (months):", min_value=1, value=12, step=1, key=f"goal_deadline_{i}")
        
        goals.append({
            "name": goal_name,
            "amount": goal_amount,
            "deadline_months": goal_deadline
        })
    
    expenses = {
        "rent": rent,
        "groceries": groceries,
        "dining_out": dining_out,
        "transportation": transportation,
        "entertainment": entertainment,
        "shopping": shopping
    }
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Generate Insights", use_container_width=True):
            with st.spinner("Generating spending insights..."):
                result = make_api_request("spending-insights", {
                    "income": income,
                    "expenses": expenses,
                    "savings_goal": savings_goal,
                    "goals": goals,
                    "currency_symbol": "₹",
                    "persona": persona
                })
                st.session_state.insights_result = result
                st.rerun()
    
    with col2:
        if st.button("🏠 Back", use_container_width=True):
            st.session_state.page = "home"
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results section
    if 'insights_result' in st.session_state and st.session_state.insights_result:
        st.markdown('<div class="white-box">', unsafe_allow_html=True)
        st.markdown("### Spending Analysis")
        
        if st.session_state.insights_result.get("success", False):
            data = st.session_state.insights_result.get("data", {})
            insights = data.get("insights", "")
            
            st.markdown('<div class="json-output">', unsafe_allow_html=True)
            st.text(insights)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"Error: {st.session_state.insights_result.get('error', 'Unknown error')}")
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    # Set background and styling
    set_background()
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Navigation
    if st.session_state.page == 'home':
        show_home_page()
    elif st.session_state.page == 'nlu':
        show_nlu_page()
    elif st.session_state.page == 'generate':
        show_generate_page()
    elif st.session_state.page == 'budget-summary':
        show_budget_summary_page()
    elif st.session_state.page == 'spending-insights':
        show_spending_insights_page()

if __name__ == "__main__":
    main()
