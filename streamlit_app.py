#created the new python file

import pandas
import streamlit
import requests
import snowflake.connector



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("FOOD LIST")
streamlit.dataframe(my_data_rows)

fruit_choices = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choices)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choices)


# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# streamlit.header("Fruityvice Fruit Advice!")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)

# my_fruit_list = my_fruit_list.set_index('Fruit')
# # Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]


# streamlit.title('My Parents New Healthy Diner')

# streamlit.header('Breakfast Menu')

# streamlit.text('🥗 Tapsilog')
# streamlit.text('🥗 Hotsilog')
# streamlit.text('🥗 Longsilog')

# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# my_fruit_list = my_fruit_list.set_index('Fruit')
# # Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# # Display the table on the page.
# streamlit.dataframe(fruits_to_show)
