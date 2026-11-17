from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    system_instruction="You are a rapper you always reply in rap",
    input="Tell me abt Napolean ",
)

print(interaction.output_text)
print(interaction.model)
print(interaction.status)

print("\n\n\n")

usage = interaction.usage

print("Input tokens:", usage.total_input_tokens)
print("Output tokens:", usage.total_output_tokens)
print("Total tokens:", usage.total_tokens)
