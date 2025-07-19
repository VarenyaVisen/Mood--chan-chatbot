import requests

ANILIST_API_URL = 'https://graphql.anilist.co'


def get_top_anime(limit=5):
    query = '''
    query ($perPage: Int) {
      Page(perPage: $perPage) {
        media(type: ANIME, sort: POPULARITY_DESC) {
          title {
            romaji
            english
          }
          genres
          averageScore
          episodes
        }
      }
    }
    '''

    variables = {
        'perPage': limit
    }

    response = requests.post(ANILIST_API_URL, json={
                             'query': query, 'variables': variables})

    if response.status_code == 200:
        data = response.json()
        anime_list = data['data']['Page']['media']
        return anime_list
    else:
        raise Exception(
            f"Query failed: {response.status_code}, {response.text}")


# Mood dictionary
mood_genre_map = {
    "happy": ["Comedy", "Slice of Life", "Adventure"],
    "sad": ["Drama", "Psychological", "Romance"],
    "angry": ["Action", "Supernatural", "Thriller"],
    "bored": ["Mystery", "Sci-Fi", "Fantasy"],
    "romantic": ["Romance", "Drama"],
    "excited": ["Shounen", "Action", "Adventure"],
    "chill": ["Slice of Life", "Music"]
}

# Fucntion to filter anime by mood


def recommend_by_mood(anime_list, mood):
    mood = mood.lower()
    if mood not in mood_genre_map:
        return []

    preferred_genres = mood_genre_map[mood]
    recommendations = []

    for anime in anime_list:
        if any(genre in preferred_genres for genre in anime['genres']):
            recommendations.append(anime)

    return recommendations

# Function to filter anime by time


def filter_by_episode_count(anime_list, time_preference):
    filtered = []
    for anime in anime_list:
        episodes = anime['episodes']

        if episodes is None:
            # Include only if user selected "long"
            if time_preference == "long":
                filtered.append(anime)
        else:
            if time_preference == "short" and episodes <= 12:
                filtered.append(anime)
            elif time_preference == "medium" and 13 <= episodes <= 24:
                filtered.append(anime)
            elif time_preference == "long" and episodes > 24:
                filtered.append(anime)

    return filtered
