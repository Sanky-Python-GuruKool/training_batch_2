from google import genai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

client = genai.Client()

image_path = Path(__file__).with_name("Guitar.png")
uploaded_file = client.files.upload(file=image_path)

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=[
        {"type": "text", "text": "generate a song on this image"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type,
        }
    ]
)
print(interaction.output_text)

print("\n" * 6)

print(interaction )