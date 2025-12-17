import streamlit as st

pages = {
    "Menu": [
        st.Page("pages/UploadPage.py", title="Upload Data"),
        st.Page("pages/CalculatePage.py", title="Perhitungan"),
    ]
}

pg = st.navigation(pages)
pg.run()