from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Hey Who are you in paragraph",
    generation_config={
        "max_output_tokens": 2100,
        "thinking_level": "medium",
    },
)

print(interaction.output_text)

token_usage = interaction.usage

print(token_usage)