from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="My name is Sanket",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="What is my name ",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)