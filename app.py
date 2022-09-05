import streamlit as st
import pickle
import pandas as pd

def recommend(show):
    show_idx = shows[shows['Title'] == show].index[0]
    distances = similarity[show_idx]
    shows_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_shows = {}
    for i in shows_list:
        recommended_shows[shows['Title'][i[0]]] = shows['Rating'][i[0]]
    return recommended_shows

def description(show):
    show_idx = shows[shows['Title'] == show].index[0]
    distances = similarity[show_idx]
    shows_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    description = {}
    for i in shows_list:
        description[shows['Title'][i[0]]] = shows['About'][i[0]]
    return description

shows_dict = pickle.load(open('shows.pkl', 'rb'))
shows = pd.DataFrame(shows_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('TV Show Recommender System')

selected_show_name = st.selectbox(
'Which show would you like to watch?',
shows['Title'])

if st.button('Recommend'):
    recommendations = recommend(selected_show_name)
    description = description(selected_show_name)
    for k in recommendations.keys():
        st.write('Show', ':', k)
        st.write('IMDB Rating', ':', recommendations[k])
        st.write('About', ':', description[k])
        st.markdown('##')
