import json
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

# Set up the model
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Load sample emails
with open("sample_emails.json", "r") as f:
    emails = json.load(f)

# Process each email
for i, email in enumerate(emails, 1):
    print(f"\n--- Email #{i} from {email['from']} ---")

    prompt = (
        f"Subject: {email['subject']}\n\n{email['body']}\n\n"
        "Summarize this email in a few bullet points and extract any action items."
    )

    response = llm.predict(prompt)
    print(response)
