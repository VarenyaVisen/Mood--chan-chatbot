from utils.recommender import get_top_anime, recommend_by_mood, filter_by_episode_count

# Ask user input
user_mood = input("How are you feeling today? (e.g., happy, sad, bored): ")
time_pref = input("How much time do you have? (short, medium, long): ")

# Fetch data
anime_list = get_top_anime(25)  # Fetch more to filter better

# Step 1: Mood-based filtering
mood_filtered = recommend_by_mood(anime_list, user_mood)

# Step 2: Time-based filtering
final_recommendations = filter_by_episode_count(mood_filtered, time_pref)

# Output
if not final_recommendations:
    print("🥲 Sorry! I couldn’t find anything matching your mood and time. Try changing your input.")
else:
    print(
        f"\n✨ Anime Recommendations for mood '{user_mood}' and time preference '{time_pref}':\n")
    for anime in final_recommendations:
        print("🎥 Title:", anime['title']['english']
              or anime['title']['romaji'])
        print("📊 Score:", anime['averageScore'])
        print("🎭 Genres:", ", ".join(anime['genres']))
        print("📺 Episodes:", anime['episodes'])
        print("-" * 40)
