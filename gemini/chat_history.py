from google import genai
from dotenv import load_dotenv
import pyfiglet

load_dotenv()

ascii_banner = pyfiglet.figlet_format("GEMINI")
print(ascii_banner)

print()
print()
print("*" * 50)
print("*" * 50)

client = genai.Client()
history = ""

for i in range(20):
    user_query = input("Gemini : What do you wanna ask ")
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=history + user_query,
    )
    print(interaction.output_text)
    history = history + "user : " + user_query + " gemini :" + interaction.output_text
    history = history + "\n\n"

    print(history)
    input("Stop")
    print("\n\n\n\n")