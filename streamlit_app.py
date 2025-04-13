# app.py

import streamlit as st
import random

# Core modules
from core.chatbot import chat_with_soulmate
from core.journal import journal_entry
from core.memory import recall_memory
from core.summary import generate_daily_summary
from core.wellness import show_wellness_tools
from core.emotion_detect import detect_emotion_from_webcam
from core.audio_input import recognize_speech_from_microphone
from core.audio_output import speak_text
from models.trainer import simulate_lora_training
from security.vault import read_encrypted_vault

# ===========================
# App Configuration
# ===========================
st.set_page_config(page_title="SoulMate.AGI", layout="wide")
st.title("✨ SoulMate.AGI – Your Evolving Emotional Companion")

# Sidebar: Menu
menu = st.sidebar.selectbox("📌 Choose Mode", [
    "Chat with SoulMate",
    "Journal",
    "Memory Recall",
    "Summary",
    "Wellness Mode"
])

# Sidebar: Emotion Detection
with st.sidebar:
    if st.button("🧠 Detect Emotion"):
        mood = detect_emotion_from_webcam()
        st.write(f"Your mood: {mood}")

# Helper: Supportive Response for Journal
def supportive_response():
    responses = [
        "That sounds like a lot to carry. I'm here for you 💙",
        "Thank you for sharing that. How do you feel now?",
        "It's okay to feel this way. You're doing your best 🌱",
        "Would you like to talk more about this?",
        "I appreciate your honesty. You're not alone 🤝"
    ]
    return random.choice(responses)

# ===========================
# Page Logic
# ===========================

# 💬 Chat with SoulMate
if menu == "Chat with SoulMate":
    st.subheader("💬 Talk to Your SoulMate")

    if "last_response" not in st.session_state:
        st.session_state.last_response = ""

    user_input = st.chat_input("Talk to SoulMate 👇")

    if user_input:
        response = chat_with_soulmate(user_input)
        st.session_state.last_response = response
        st.markdown(f"**🧍 You:** {user_input}")
        st.markdown(f"**🧠 SoulMate:** {response}")

    if st.button("🎙️ Speak Instead"):
        spoken_input = recognize_speech_from_microphone()
        if spoken_input:
            st.write(f"🧍 You said: {spoken_input}")
            response = chat_with_soulmate(spoken_input)
            st.session_state.last_response = response
            st.markdown(f"**🧠 SoulMate:** {response}")

    if st.button("🔊 Play Response"):
        if st.session_state.last_response:
            speak_text(st.session_state.last_response)
        else:
            st.warning("⚠️ No response available to play.")

# 📝 Journal Mode
elif menu == "Journal":
    st.subheader("📝 Journal Your Thoughts")
    entry = st.text_area("Write your thoughts here...", height=200)

    if st.button("Save Journal Entry") and entry:
        result = journal_entry(entry)
        st.success(result)

        st.markdown("#### 💬 SoulMate Reflects:")
        reflection_prompt = f"The user just journaled this thought:\n\n\"{entry}\"\n\nGive a compassionate, emotionally supportive response or thoughtful reflection."
        response = chat_with_soulmate(reflection_prompt)
        st.write(response)

    if st.button("🔒 View My Encrypted Diary"):
        entries = read_encrypted_vault()
        for i, e in enumerate(entries[::-1]):
            st.info(f"📝 Entry {i+1}: {e}")

# 📚 Memory Recall
elif menu == "Memory Recall":
    st.subheader("📚 Memory Recall")
    recalled = recall_memory()
    st.success(recalled)

    st.markdown("#### 💭 SoulMate Reflects on Your Growth:")
    reflection_prompt = f"These are some of the user's past memories or journal entries:\n\n{recalled}\n\nCan you help them reflect on their personal growth, emotional progress, or any recurring themes?"
    response = chat_with_soulmate(reflection_prompt)
    st.write(response)

# 📊 Daily Summary
elif menu == "Summary":
    st.subheader("📊 Daily Summary")
    summary = generate_daily_summary()
    st.write(summary)

    if st.button("🛠️ Run Nightly Training"):
        simulate_lora_training()
        st.success("✅ Model evolved with today’s learning!")

# 🌈 Wellness Tools
elif menu == "Wellness Mode":
    st.subheader("🌈 Wellness Tools")
    show_wellness_tools()
