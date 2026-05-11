import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8080/api/products"

st.title("🛒 E-Commerce Store")

menu = st.sidebar.selectbox(
    "Menu",
    ["View Products", "Add Product"]
)

if menu == "View Products":

    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.warning("No products found")

if menu == "Add Product":

    st.subheader("Add New Product")

    name = st.text_input("Product Name")
    description = st.text_area("Description")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)

    if st.button("Add Product"):

        payload = {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            st.success("Product Added Successfully!")
        else:
            st.error("Failed to add product")
