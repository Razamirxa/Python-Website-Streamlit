import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def add_custom_css():
    custom_css = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        .stSidebar {
             background-color: cyan;

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def data_dashboard():
    st.title("Simple Data Dashboard")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", columns)

        if st.button("Generate Plot"):
            st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on file upload...")

def website():
    st.title("My Python Website")

    # Sidebar navigation
    st.sidebar.title("Website Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

    # Homepage
    if menu == "Home":
        st.header("Welcome to My Website")
        st.write("This is a simple website built with Streamlit.")
        st.image("https://www.pushengage.com/wp-content/uploads/2022/02/Best-Website-Welcome-Message-Examples.png", caption="A Placeholder Image")

    # About Page
    elif menu == "About":
        st.header("About")
        st.write("This website is created using Python and Streamlit.")
        st.write("Streamlit is an open-source app framework for Machine Learning and Data Science projects.")

    # Contact Page
    elif menu == "Contact":
        st.header("Contact")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Submit")

            if submitted:
                if name and email and message:
                    st.success("Thank you for your message! We'll get back to you soon.")
                else:
                    st.error("Please fill out all fields.")

def main():
    add_custom_css()

    st.sidebar.title("Main Navigation")
    app_mode = st.sidebar.radio("Select an Application", ["Data Dashboard", "Website"])

    if app_mode == "Data Dashboard":
        data_dashboard()
    elif app_mode == "Website":
        website()

if __name__ == "__main__":
    main()
