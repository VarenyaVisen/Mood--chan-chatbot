# 🎌 Anime Recommender Chatbot

An engaging and personalized **anime recommendation chatbot** that suggests shows based on your **mood** and **available time**. Built using **Streamlit** and powered by the **AniList GraphQL API**, this project transforms a simple chatbot task into a smart anime discovery experience.

🔗 **[Live Demo »](https://varenyavisen-mood--chan-chatbot-app-nmbivp.streamlit.app/)**

---

## 💡 About the Project

Originally part of a **virtual internship at Kodacy**, the project was designed to explore API integration and user interaction. Instead of building a generic chatbot, I decided to create something meaningful for anime fans like myself—a fun tool that recommends anime based on how you're feeling and how much time you have.

This project combines:
- **Real-time data fetching**
- **Mood/time-based logic**
- **Clean, user-friendly UI**

It reflects my personal effort in bringing emotion-driven recommendations to life.

---

## ✨ Key Features

- 🎭 **Mood-based suggestions**: happy, sad, bored, romantic, angry, excited, chill  
- ⏱️ **Time filters**:  
  - Short (≤12 episodes)  
  - Medium (13–25 episodes)  
  - Long (26+ episodes or unknown)  
- 🔍 Smart filtering of shows even when episode count is missing  
- 📡 Live recommendations using the **AniList GraphQL API**  
- 🖥️ Intuitive, interactive UI with **Streamlit**  
- 🌐 Easily deployable and open-source

---

## 🧠 Tech Stack

| Layer         | Tools Used                                  |
|---------------|----------------------------------------------|
| UI            | Streamlit                                   |
| Backend       | Python, Requests                            |
| External API  | AniList GraphQL API                         |
| Deployment    | Streamlit Cloud                             |
| Dev Tools     | Git, `venv`, `requirements.txt`             |

---

## 🚀 How It Works

1. **Choose your mood** (e.g., happy, sad, chill)
2. **Select your available time** (short, medium, long)
3. App queries AniList for top trending anime
4. Results are **filtered** based on selected mood tags and episode count
5. Users see a **clean recommendation card** with:
   - English and Romaji titles  
   - Average rating  
   - Genre tags  
   - Episode count  

If no match is found, the bot responds with a thoughtful fallback suggestion.

---

## 📸 Preview

![Screenshot](chatbot_preview.png) <!-- Replace with the actual image path -->

---

## 📌 Final Note

This project not only meets the internship objectives but also reflects my personal touch—turning a basic chatbot into a **smart, mood-aware anime recommender** that blends tech with fandom.  
Perfect for anime lovers who want quick, relevant suggestions.
