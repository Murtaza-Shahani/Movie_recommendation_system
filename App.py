# to run the file write in terminal streamlit run App.py(file_name)
from typing import List, Any

import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)

]

imageCarouselComponent(imageUrls=imageUrls, height=200)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # getting the index of movies
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommended_movies = []
    recommend_poster = []
    for i in movies_list:  # printing these similar movies
        movies_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommended_movies, recommend_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name  = st.selectbox('Watch what You love', movies['title'].values)

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selected_movie_name)

    num_recommendations = min(5, len(movie_name))  # Ensure not to exceed the number of recommendations

    # Create columns dynamically based on the number of recommendations
    cols = st.columns(num_recommendations)

    for i in range(num_recommendations):
        with cols[i]:
            st.text(movie_name[i])
            st.image(movie_poster[i])




