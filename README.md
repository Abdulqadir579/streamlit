🤖 Digidot AI Assistant
Digidot AI Assistant is a Streamlit-based chatbot that leverages Amazon Bedrock's foundation models and a knowledge base stored in Amazon OpenSearch and S3. It enables users to ask natural language questions and get accurate, contextual answers based on custom uploaded documents.

📌 Project Architecture
The overall architecture is designed to be scalable, serverless, and efficient using the following AWS components:


🔁 Workflow:
1. User interacts with the chatbot UI built using Streamlit.

2. The frontend sends a request to the API Gateway.

3. API Gateway triggers an AWS Lambda function.

The Lambda function:

Accepts the user query.

Uses Amazon Bedrock's RetrieveAndGenerate API.

Retrieves relevant documents from the Knowledge Base.

The Knowledge Base:

Stores vector embeddings using Amazon OpenSearch.

Fetches reference data from Amazon S3.

A response is generated using a foundation model (e.g., Claude v2.1) and sent back to the frontend.

🚀 How to Run the Project Locally
✅ Prerequisites
Python 3.12
Pip

AWS account with access to Amazon Bedrock and Lambda

API Gateway endpoint connected to your Lambda

🧩 Installation
Clone the repository:


git clone https://github.com/your-username/digidot-ai-assistant.git
cd digidot-ai-assistant

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install required dependencies:
pip install -r requirements.txt

requirements.txt should contain:

streamlit
requests
streamlit-lottie

🧠 Run the Streamlit Chatbot
Update your code in app.py to replace the API-GATEWAY-URL with your actual API Gateway endpoint.

Then run:

streamlit run app.py
Visit http://localhost:8501 in your browser to interact with your chatbot.

📂 File Structure

digidot-ai-assistant/
│
├── app.py                  # Streamlit chatbot UI
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── architecture.png        # AWS Architecture Diagram
💡 Example Usage
Ask questions like:

“How does search work?”

“What are the benefits of vector databases?”

Get detailed answers with citations from your knowledge base.

🔒 Security
Ensure your API Gateway is protected with proper authentication (e.g., Cognito or API key) before exposing it to the public.

🧰 Technologies Used
Frontend: Streamlit + Lottie animations

Backend: AWS Lambda + API Gateway

AI Model: Amazon Bedrock (Claude v2.1)

Knowledge Base: Amazon OpenSearch + S3
