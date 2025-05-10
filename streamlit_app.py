import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/anime-filtered.csv")
    return df

anime_df = load_data()

st.title("🎌 Anime Explorer & Visual Analytics")

# Create two tabs
tab1, tab2 = st.tabs(["🔎 Anime Search", "📊 Visualizations"])

# --------------------- TAB 1: Anime Search ---------------------
# Search inputs
col1, col2 = st.columns([2, 1])

with col1:
    search_name = st.text_input("Search Anime by Name")

with col2:
    selected_score = st.slider("Filter by Score", 1, 10, 0)

# Filter logic
if search_name:
    result_df = anime_df[anime_df["Name"].str.contains(search_name, case=False, na=False)]
elif selected_score > 0:
    result_df = anime_df[anime_df["Score"].round(0) == selected_score]
else:
    result_df = pd.DataFrame()

# Display results
if not result_df.empty:
    for _, row in result_df.iterrows():
        st.markdown("---")
        st.markdown(f"### {row['Name']}")
        st.markdown(f"*{row.get('English name', '')}, {row.get('Japanese name', '')}*")

        st.markdown(f"<div style='color:gray'>{row.get('sypnopsis', 'No synopsis available.')}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 2])
        with col1:
            st.markdown(f"**Type**: {row.get('Type', 'N/A')}")
            st.markdown(f"**Studios**: {row.get('Studios', 'N/A')}")
            st.markdown(f"**Date Aired**: {row.get('Aired', 'N/A')}")
            st.markdown(f"**Status**: {'Finished Airing' if row.get('Completed', 0) > 0 else 'Ongoing'}")
            st.markdown(f"**Genre**: {row.get('Genres', 'N/A')}")
        with col2:
            st.markdown(f"**Score**: {row.get('Score', 'N/A')}")
            st.markdown(f"**Premiered**: {row.get('Premiered', 'N/A')}")
            st.markdown(f"**Duration**: {row.get('Duration', 'N/A')}")
            st.markdown(f"**Quality**: HD")
            st.markdown(f"**Views**: {int(row.get('Members', 0)):,}")
else:
    st.info("Enter an anime name or choose a score to begin.")



# --------------------- TAB 2: Visualizations ---------------------
with tab2:
    st.header("Anime Dataset Visualizations")
    
    st.subheader("Score Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.histplot(anime_df["Score"].dropna(), bins=20, kde=True, ax=ax, color="skyblue")
    ax.set_xlabel("Score")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    st.subheader("Top 10 Genres")
    genre_series = anime_df["Genres"].dropna().str.split(', ').explode()
    top_genres = genre_series.value_counts().head(10)
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette="viridis", ax=ax2)
    ax2.set_xlabel("Number of Anime")
    ax2.set_ylabel("Genre")
    st.pyplot(fig2)

    st.subheader("Top Studios by Anime Count")
    studios = anime_df["Studios"].dropna().str.split(', ').explode()
    top_studios = studios.value_counts().head(10)
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.barplot(x=top_studios.values, y=top_studios.index, palette="magma", ax=ax3)
    ax3.set_xlabel("Number of Anime")
    ax3.set_ylabel("Studio")
    st.pyplot(fig3)


# import streamlit as st
# import pandas as pd

# # Load data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/anime-filtered.csv")
#     return df

# anime_df = load_data()

# st.set_page_config(page_title="Anime Explorer", layout="wide")
# st.title("🎌 Anime Explorer")

# # Search inputs
# col1, col2 = st.columns([2, 1])

# with col1:
#     search_name = st.text_input("Search Anime by Name")

# with col2:
#     selected_score = st.slider("Filter by Score", 1, 10, 0)

# # Filter logic
# if search_name:
#     result_df = anime_df[anime_df["Name"].str.contains(search_name, case=False, na=False)]
# elif selected_score > 0:
#     result_df = anime_df[anime_df["Score"].round(0) == selected_score]
# else:
#     result_df = pd.DataFrame()

# # Display results
# if not result_df.empty:
#     for _, row in result_df.iterrows():
#         st.markdown("---")
#         st.markdown(f"### {row['Name']}")
#         st.markdown(f"*{row.get('English name', '')}, {row.get('Japanese name', '')}*")

#         st.markdown(f"<div style='color:gray'>{row.get('sypnopsis', 'No synopsis available.')}</div>", unsafe_allow_html=True)

#         col1, col2 = st.columns([2, 2])
#         with col1:
#             st.markdown(f"**Type**: {row.get('Type', 'N/A')}")
#             st.markdown(f"**Studios**: {row.get('Studios', 'N/A')}")
#             st.markdown(f"**Date Aired**: {row.get('Aired', 'N/A')}")
#             st.markdown(f"**Status**: {'Finished Airing' if row.get('Completed', 0) > 0 else 'Ongoing'}")
#             st.markdown(f"**Genre**: {row.get('Genres', 'N/A')}")
#         with col2:
#             st.markdown(f"**Score**: {row.get('Score', 'N/A')}")
#             st.markdown(f"**Premiered**: {row.get('Premiered', 'N/A')}")
#             st.markdown(f"**Duration**: {row.get('Duration', 'N/A')}")
#             st.markdown(f"**Quality**: HD")
#             st.markdown(f"**Views**: {int(row.get('Members', 0)):,}")
# else:
#     st.info("Enter an anime name or choose a score to begin.")
