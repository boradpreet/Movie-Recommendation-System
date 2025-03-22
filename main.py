import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('movie_recommendation.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Load your dataset
data1 = pd.read_csv('Movie.csv')  # Ensure this dataset matches the model

def recommend(movie):
    movie_index = data1[data1["title"] == movie].index[0]
    distances = similarity[movie_index]
    final = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [data1.iloc[i[0]].title for i in final]

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Sidebar
with st.sidebar:
    st.markdown("## ☰ Menu")
    with st.expander("Navigation"):
        st.write("- Home")
        st.write("- Recommendations")
        st.write("- About")

# Header with Company Name
st.markdown("""
    <h2 style='text-align: center; color: #4682B4;'>Movie Recommendation System</h2>
    <hr style='border: 2px solid #4682B4;'>
    """, unsafe_allow_html=True)

# Movie Input Section
st.markdown("""
    <h3 style='text-align: center;'>Enter a movie name to get recommendations</h3>
    """, unsafe_allow_html=True)

movie_name = st.text_input("Movie Name", "Avatar")

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    
    st.markdown("""
        <h3 style='color: #FF4500;'>Top 5 Recommended Movies</h3>
        """, unsafe_allow_html=True)
    
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
