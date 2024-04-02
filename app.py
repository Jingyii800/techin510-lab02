# app.py
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Iris Flower Explorer",
    page_icon="🌸",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🌸 Iris Flower Explorer")
st.subheader('Iris Dataset Findings')
st.markdown("""
- **Species Distinction**: The dataset encompasses three Iris species: Setosa, Versicolor, and Virginica. Notably, Setosa species exhibit distinct characteristics, typically having smaller petal lengths and widths, contrasted with larger sepal widths, which simplifies its identification compared to Versicolor and Virginica.
- **Correlation**: Across all species, petal length and width demonstrate a pronounced positive correlation, indicating that increases in petal length are generally accompanied by proportional increases in petal width.
""")

iris = pd.read_csv('IRIS.csv')

# Title and introduction
st.subheader('Interactive Data Visualization')

# Side bar for filtering choices
# Dropdown for species selection
species = st.sidebar.selectbox(
    "What kind of Iris would you like to explore?",
    options=iris['species'].unique()
)
# Using "with" notation
with st.sidebar:
    sepal_length = st.slider('Sepal Length', float(iris['sepal_length'].min()), float(iris['sepal_length'].max()))
    sepal_width = st.slider('Sepal Width', float(iris['sepal_width'].min()), float(iris['sepal_width'].max()))
    petal_length = st.slider('Petal Length', float(iris['petal_length'].min()), float(iris['petal_length'].max()))
    petal_width = st.slider('Petal Width', float(iris['petal_width'].min()), float(iris['petal_width'].max()))

# Filter the dataset based on the user's choices
filtered_data = iris[
    (iris['species'] == species) &
    (iris['sepal_length'] >= sepal_length) &
    (iris['sepal_width'] >= sepal_width) &
    (iris['petal_length'] >= petal_length) &
    (iris['petal_width'] >= petal_width) 
]

# Display the filtered dataset
with st.expander(f"Filtered Data for {species}"):
    st.table(filtered_data)

# Visualiztion
col1, col2 = st.columns(2)
with col1:
    chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='sepal_length',
    y='sepal_width',
    tooltip=['sepal_length', 'sepal_width']
).interactive()
    st.altair_chart(chart, use_container_width=True)

with col2:
    chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='petal_length',
    y='petal_width',
    tooltip=['petal_length', 'petal_width']
).interactive()
    st.altair_chart(chart, use_container_width=True)