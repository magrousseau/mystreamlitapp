import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title='Hello')

st.title('Hello, Streamlit!')

# if st.button("Click 😉"):
#     st.image("raw_data/wagon.png")


# search_query = st.text_input("Search a gif")
# url = "https://api.giphy.com/v1/gifs/search"
# params = {
#     "api_key": "fd5ZBBwwanRUYg9XXMckjta9FEyUJlJ" ,
#     "q": search_query,
#     "limit": 10
# }

# #full_url = "https://api.giphy.com/v1/gifs/search?api_key=efd5ZBBwwanRUYg9XXMckjta9FEyUJlJ&q=dog&limit=25"

# while not search_query:
#     st.stop()

# response = requests.get(url, params=params).json()

# idx = np.random.randint(0,10)
# gif_url = response["data"][idx]["embed_url"]
# st.write(
#     f'<iframe src="{gif_url}" style="height:200px;width:300px;"></iframe>',
#     unsafe_allow_html=True
# )
# st.write(response["data"][0]["title"])
