
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Step 1: Check API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is missing.")

# Step 2: Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Step 3: Create a specific prompt
prompt = """
Suggest exactly 5 healthy breakfast ideas.

Consider these healthy breakfast criteria:
- Include protein and dietary fiber.
- Prefer whole grains, fruits and vegetables.
- Avoid excessive added sugar.
- Include a balanced combination of nutrients.
- Prefer vegetarian South Indian breakfast options.

Output requirements:
- Numbered list from 1 to 5.
- One line per breakfast idea.
- No introduction or conclusion.
"""

# Step 4: Invoke the model
response = llm.invoke(prompt)

# Step 5: Print the complete message object
print("\n===== RAW LANGCHAIN RESPONSE =====")
print(response)

# Step 6: Extract and print only the response text
print("\n===== BREAKFAST IDEAS =====")
print(response.content)
