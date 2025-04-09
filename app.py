import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import time

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_brain = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_SkhtL8.json")

# API call
def call_api(query):
    api_url = "https://p1ooajzr61.execute-api.us-east-1.amazonaws.com/digidot-staging/chatapi"  # Replace this with your actual endpoint
    try:
        response = requests.post(api_url, json={"user_query": query})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ API Error: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        st.error(f"❌ JSON Decode Error: {str(e)}")
        return None

# Streamlit UI
def main():
    st.set_page_config(page_title="Digidot AI Assistant", page_icon="🧠", layout="wide")

    # Hero section
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
            <h1 style='font-size: 3rem; color: #4a4a4a;'>🤖 Meet Your Digidot Assistant</h1>
            <p style='font-size: 1.2rem;'>Ask questions, explore knowledge, and discover answers instantly.</p>
        """, unsafe_allow_html=True)

    with col2:
        st_lottie(lottie_brain, height=200, key="brain")

    st.markdown("---")

    # Chat input UI
    st.markdown("### 💬 Ask me anything:")
    user_question = st.text_input("Type your message here...", key="input", placeholder="e.g., How does search work?")

    if user_question:
        with st.spinner("💭 Thinking..."):
            result = call_api(user_question)

        if result:
            # Response output
            with st.chat_message("user"):
                st.markdown(f"**You:** {user_question}")
            with st.chat_message("assistant"):
                st.markdown(f"**Assistant:** {result.get('generated_response', 'No response')}")

            with st.expander("📄 View Response Details"):
                st.json({
                    "Query": result.get('query', 'N/A'),
                    "Status Code": result.get('statusCode', 'N/A'),
                    "Source": result.get('s3_location', 'N/A')
                })
        else:
            st.error("⚠️ No valid response returned.")
    else:
        st.info("👆 Ask your AI assistant anything to get started.")

    # Footer
    st.markdown("---")
    st.markdown("<center><small>Built with ❤️ by Abdul Qadir</small></center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

