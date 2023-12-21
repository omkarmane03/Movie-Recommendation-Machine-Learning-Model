import streamlit as st
import numpy as np 
import pandas as pd
import pickle as pk

st.header('Movie Recommendation Machine Learning Model')

movie_dataset = pk.load(open(movie_dataset.pk1),'rb')
similarity = pk.load(open(similarity.pk1),'rb')

def recommend_movie(movie_name):
    movie_index = movie_dataset[movie_dataset['title']==movie_name].index[0]
    similar_movies = similar_movies = sorted(list(enumerate(similarity[5696])),reverse=True,key = lambda vector: vector[1])
    recommendations = []

    for i in similar_movies [1:6]:
        recommendations.append(movie_dataset.iloc[i[0]].title + 'with similarity of ' + str(round(i[1]*100,2)) + '%')
    return recommendations

selected_movie = st.selectbox('Select Movie/TV Show', movie_dataset['title'])

if st.button('Recommend'):
    result = recommend_movie(selected_movie)

    st.text(result[0])
    st.text(result[1])
    st.text(result[2])
    st.text(result[3])
    st.text(result[4])