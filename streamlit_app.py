import streamlit

streamlit.title('My Parent New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale,Spinach & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#python libary
import pandas
#pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv  to pull the data into a dataframe we'll call my_fruit_list.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
