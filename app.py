import streamlit as st
import pickle
import numpy as np

# Load pickled data
popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
similarity_score = pickle.load(open("similarity_score.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))

# UI
st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 Book Recommendation System")

# Split layout into 2 columns
left_col, right_col = st.columns([2, 1])  # Left is wider

# Left: Popular Books
with left_col:
    st.subheader("🔥 Popular Books")
    for i in range(len(popular_df)):
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(popular_df["Image-URL-M"].values[i], width=80)
        with cols[1]:
            st.markdown(f"**{popular_df['Book-Title'].values[i]}**")
            st.caption(f"Author: {popular_df['Book-Author'].values[i]}")
            st.caption(f"⭐ {round(popular_df['avg_rating'].values[i], 2)}  |  👍 {popular_df['num-ratings'].values[i]}")
        st.markdown("---")

# Right: Recommendation Section
with right_col:
    st.subheader("🔍 Recommend Books")
    book_list = pt.index.values
    selected_book = st.selectbox("Type or select a book title", book_list)

    if st.button("Recommend"):
        index = np.where(pt.index == selected_book)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

        st.write("### 📖 Recommended:")
        for i in similar_items:
            temp_df = books[books["Book-Title"] == pt.index[i[0]]].drop_duplicates("Book-Title")
            title = temp_df["Book-Title"].values[0]
            author = temp_df["Book-Author"].values[0]
            image_url = temp_df["Image-URL-M"].values[0]

            cols = st.columns([1, 2])
            with cols[0]:
                st.image(image_url, width=80)
            with cols[1]:
                st.markdown(f"**{title}**")
                st.caption(f"Author: {author}")
            st.markdown("---")
