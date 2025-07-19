# app.py
import streamlit as st
from utils.recommender import get_top_anime, recommend_by_mood, filter_by_episode_count

st.set_page_config(page_title="Anime Recommender Bot", page_icon="🎌")

st.title("🎌 Anime Recommender Chatbot")
st.write("Tell me your mood and how much time you have, and I’ll find you the perfect anime!")

mood = st.selectbox("How are you feeling or what mood are you in?", 
                    ["happy", "sad", "bored", "romantic", "angry", "excited", "chill"])

time_pref = st.radio("How much time do you have?", ["short", "medium", "long"])

if st.button("🎥 Recommend Anime"):
    anime_list = get_top_anime(25)
    mood_filtered = recommend_by_mood(anime_list, mood)
    time_filtered = filter_by_episode_count(mood_filtered, time_pref)

    if not time_filtered:
        st.error("🥲 Sorry! I couldn't find anything that matches your mood and time preference.")
    else:
        st.success(f"🎉 Found {len(time_filtered)} anime for your mood '{mood}' and time '{time_pref}'")
        for anime in time_filtered:
            title = anime['title']['english'] or anime['title']['romaji']
            genres = ", ".join(anime['genres'])
            st.markdown(f"""
            ### 🎥 {title}
            - 📊 Score: {anime['averageScore']}
            - 🎭 Genres: {genres}
            - 📺 Episodes: {anime['episodes']}
            ---
            """)

