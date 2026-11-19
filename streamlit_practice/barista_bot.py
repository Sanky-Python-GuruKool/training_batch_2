import streamlit as st 
from google import genai
from dotenv import load_dotenv
load_dotenv(r"D:\GanitAnk\2026\Batch 2\Programs\training\training_batch_2\gemini\.env")

client = genai.Client()

system_prompt = """You are 'Brew', the friendly barista at Brew Cafe.
Talk in a warm, casual Hinglish tone. Keep answers short (2-4 lines).

Menu:
- Espresso    Rs.180
- Cappuccino  Rs.220
- Latte       Rs.240
- Cold Brew   Rs.260
- Add-ons: Croissant Rs.120, Brownie Rs.150, Bagel Rs.130

Rules:
- Suggest drinks based on the customer's mood, weather or taste.
- Only recommend items from the menu.
- If asked something unrelated, politely Sorry I am just a Barista Bot ."""


WELCOME = "Welcome to The Botistic Barista Please tell your order"

st.set_page_config(page_title="My cafe", page_icon="☕")
st.title("☕ My cafe - Barista Bot Welcomes You")
st.caption("Ek baar aaoge humesha aaoge",text_alignment="right")
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role":"assistant", "content": WELCOME})

st.sidebar.header("☕ Menu")
st.sidebar.write("Espresso - 500")
st.sidebar.write("Latte - 300")
st.sidebar.write("Moca - 800")
st.sidebar.write("Capucino - 200")
st.divider()


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
            st.write(msg["content"])

prompt = st.chat_input("Talk to my Barista Bot.... It's damn good ")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role":"user", "content": prompt})
    conversation = ""
    for msg in st.session_state.messages:
         conversation = conversation + msg["role"] + msg["content"] + "\n\n"
    with st.chat_message("assistant"):
        with st.spinner("Barista Bot is Thinking....."):
            response = client.interactions.create(
                        model="gemini-3.1-flash-lite",
                        system_instruction=system_prompt,
                        input=conversation
                        )
            

            st.write(response.output_text)
            st.session_state.messages.append({"role":"assistant", "content": response.output_text})

