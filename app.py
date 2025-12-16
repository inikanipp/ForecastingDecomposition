import streamlit as st

st.title("Hello Streamlit!")
# st.write("Aplikasi Streamlit pertamaku 🚀")

st.markdown("""
           <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

import streamlit as st
with open("style.css") as f:
    css = f"<style>{f.read()}</style>"

with st.sidebar:
    st.write("apalah")


# layout

row1 = st.container()
row2 = st.container()

# ========================= start baris 1 =========================
with row1:
    col1,col2 = st.columns([4,2])
    # ========================= kolom 1 baris 1 =========================
    with col1:
        tile = st.container(height=180)

        with tile :
            st.markdown("""
                <div class="header-title">
                Upload Data
                </div>
            """, unsafe_allow_html=True)
            uploaded_files = st.file_uploader(
                "", accept_multiple_files=False, type="csv"
            )

    # ========================= kolom 2 baris 1 =========================
    with col2:
        tile = st.container(height=180)

        with tile :
            st.markdown("""
                <div class="header-title">
                Amount of Data
                </div>
            """, unsafe_allow_html=True)


            if uploaded_files is not None:
                import pandas as pd
                
                # baca csv
                df = pd.read_csv(uploaded_files)

                amount_of_data = df.shape[0]

                st.markdown(f"""
                    <div class="data-card">
                    <div class="data-number">{amount_of_data}</div>
                    <div class="data-label">Amount of Data</div>
                    </div>
                """, unsafe_allow_html=True)
            
            else :

                st.markdown("""
                    <div class="data-card">
                    <div class="data-number">0</div>
                    <div class="data-label">Amount of Data</div>
                    </div>
                """, unsafe_allow_html=True)
    

# ========================= end baris 1 =========================


# ========================= start baris 2 =========================
with row2:
    col4, col5 = st.columns([3,1])
    # ========================= kolom 1 baris 2 =========================
    with col4 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                Chart Plot
                </div>
            """, unsafe_allow_html=True)

    # ========================= kolom 2 baris 2 =========================
    with col5 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                Preview
                </div>
            """, unsafe_allow_html=True)

           
            if uploaded_files is not None :
                column_names = df.columns.to_list()
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item year">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item year">{column_names[2]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                for _,row in df.iterrows() :
                    st.markdown(f"""
                        <div class="date-selector-container">
                        <span class="date-item year">{row['Tahun']}</span>
                        <span class="date-item month">{row['Bulan']}</span>
                        <span class="date-item year">{row['Nilai']}</span>
                        </div>
                    """, unsafe_allow_html=True)

            else :
                st.markdown(f"""
                        <div class="background-wrapper">
                        <div class="modal-container">
                            <div class="status-box">
                            Tidak Ada Data
                            </div>
                        </div>
                        </div>

                    """, unsafe_allow_html=True)



# ========================= end baris 2 =========================


st.markdown(css, unsafe_allow_html=True)

# suntikkan ke streamlit