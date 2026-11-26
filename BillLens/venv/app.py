
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BillLens",
    page_icon="💡",
    layout="wide"
)

# Project title
st.title("💡 BillLens")
st.subheader("Turning Everyday Household Bills into Smart Savings")

st.write(
    "Upload your household bills and discover "
    "how you can save money every month."
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Upload Bill", "Dashboard", "Insights"]
)

if page == "Home":
    st.header("Welcome to BillLens!")
    st.write("Your smart household expense assistant.")

elif page == "Upload Bill":
    st.header("Upload Your Bill")

    uploaded_file = st.file_uploader(
        "Choose an electricity bill or grocery receipt",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    if uploaded_file:
        st.success("Your bill was uploaded successfully!")

elif page == "Dashboard":
    st.header("Your Household Dashboard")
    st.info("Your expense dashboard will appear here.")

elif page == "Insights":
    st.header("Smart Saving Suggestions")
    st.info("Your personalised insights will appear here.")
