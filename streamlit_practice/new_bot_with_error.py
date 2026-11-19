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
- If asked something unrelated, politely bring the chat back to coffee."""


WELCOME = "Welcome to The Botistic Barista Please tell your order"

def new_chat():
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        system_instruction=system_prompt,
        input="hi"
        )
    return interaction


st.set_page_config(page_title="My Cafe", page_icon="☕")
st.title("Welcome to Barista Bot")

if "chat" not in st.session_state:
    st.session_state.chat = []

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role":"assistant", "content": WELCOME})

st.sidebar.header("☕ Menu")
st.sidebar.write("Espresso - Rs.180")
st.sidebar.write("Cappuccino - Rs.220")
st.sidebar.write("Latte - Rs.240")
st.sidebar.write("Cold Brew - Rs.260")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat = new_chat()
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": WELCOME})
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("What do you want to order")

if prompt:
    # Show and save user message
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Gemini reply
    with st.chat_message("assistant"):
        with st.spinner("Barista soch raha hai..."):
            response = st.session_state.chat.send_message(prompt)
        reply = response.text
        st.write(reply)

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})