import streamlit as st
import pandas as pd

# Load the dataset
st.title("Iris Dataset Viewer")
st.write("This app displays the Iris dataset.")

# Load the Iris dataset
iris_data = pd.read_csv("iris.csv")

# Show the dataset
st.write(iris_data)
