from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

stream = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain about Mythology in 15 sentences ",
    stream=True,
    generation_config={
        "thinking_level": "low"
    },
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
