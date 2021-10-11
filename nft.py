import streamlit as st
import requests, json

# TO RUN THE CODE -> streamlit run nft.py
endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"Boring - {endpoint}")

st.sidebar.write("Filters")

#User can choose the collection
collection_input = st.sidebar.text_input("Collection (https://opensea.io/collection/ -> boredapeyachtclub <-)")
# Examples
# boredapeyachtclub
# mutant-ape-yacht-club
# bored-ape-kennel-club


owner = st.sidebar.text_input("Owner (0x0000000000000000000000000000000000000000)")
# Examples
# 0x0000000000000000000000000000000000000000
# 0xfe65a9C1D475740327454FeDf10fBCC0dDd72fDB

#Assets
if endpoint == "Assets":
    params = {}

    if collection_input:
        params['collection'] = collection_input
    if owner:
        params ['owner'] = owner 



    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

    response = r.json()
    for asset in response["assets"]:
        #st.write(asset['collection']['symbol'])
        st.write(f"{asset ['collection'] ['name']} #{asset ['token_id']}")

        st.image (asset["image_url"])

    st.write(r.json())

 #Rarity
