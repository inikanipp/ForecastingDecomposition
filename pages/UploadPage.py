import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

if "df" not in st.session_state:
    st.session_state.df = None

st.title("Decomposition Forecasting")
# st.write("Aplikasi Streamlit pertamaku 🚀")

st.markdown("""
           <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

import streamlit as st
with open("style.css") as f:
    css = f"<style>{f.read()}</style>"

# with st.sidebar:
#     st.write("apalah")


# layout

row1 = st.container()
row2 = st.container()
row3 = st.container()

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
                "", accept_multiple_files=False, type=["csv", "xlsx"]
            )
            if uploaded_files is not None and st.session_state.df is None:
                if uploaded_files.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_files)

                elif uploaded_files.name.endswith(".xlsx"):
                    df = pd.read_excel(uploaded_files)

                cols = df.columns.to_list()
                df.rename(columns={
                    cols[0]: "Tahun",
                    cols[1]: "Periode",
                    cols[2]: "Aktual"
                }, inplace=True)

                df["periode"] = range(1, len(df) + 1)

                st.session_state.df = df

    # ========================= kolom 2 baris 1 =========================
    with col2:
        tile = st.container(height=180)

        with tile :
            st.markdown("""
                <div class="header-title">
                Amount of Data
                </div>
            """, unsafe_allow_html=True)


            if st.session_state.df is not None:
                amount = st.session_state.df.shape[0]
            else:
                amount = 0

            st.markdown(f"""
                <div class="data-card">
                    <div class="data-numberApp">{amount}</div>
                    <div class="data-labelApp">Amount of Data</div>
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


            if st.session_state.df is not None :
                chart = alt.Chart(st.session_state.df).mark_line().encode(
                        x='periode',
                        y='Aktual',
                    ) 
                st.altair_chart(chart, use_container_width=True)
               

            else :
                st.markdown(f"""
                        <div class="background-wrapper">
                        <div class="modal-container">
                            <div class="status-box">
                            Tidak Ada Dataa
                            </div>
                        </div>
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
    
           
            if st.session_state.df is not None :
                column_names = st.session_state.df.columns.to_list()
                st.markdown(f"""
                        <div class="date-selector-container-headerApp">
                        <span class="date-item month">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item month">{column_names[2]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                for _,row in st.session_state.df.iterrows() :
                    st.markdown(f"""
                        <div class="date-selector-containerApp">
                        <span class="date-item month">{row['Tahun']}</span>
                        <span class="date-item month">{row['Periode']}</span>
                        <span class="date-item month">{row['Aktual']}</span>
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

with row3:
    col1= st.columns(1)[0]
    # ========================= kolom 1 baris 3 =========================
    with col1:
        tile = st.container(height=300)

        with tile :
            
        
            if st.session_state.df is not None :
                st.markdown("""
                <div class="header-title">
                Tambah Data
                </div>
            """, unsafe_allow_html=True)
                st.markdown("""
                    <div class="space">
                    
                    </div>
            """, unsafe_allow_html=True)
                
                column_names = st.session_state.df.columns.to_list()
                unique_periode = tuple(st.session_state.df['Periode'].unique())
                
                colIn1, colIn2, colIn3 = st.columns([1,1,1])
                with colIn1 :
                    tahun = st.number_input(
                                "Tahun",
                                min_value=2025,
                                max_value=2100,
                                value=2025,
                                step=1,
                                key=1
                            )
                with colIn2 :
                    periode = st.selectbox(
                        column_names[1],
                        unique_periode,
                    )
                with colIn3 :
                    Aktual = st.number_input(
                                "Nilai",
                                min_value=0,
                                max_value=9999999999,
                                value=205,
                                step=1,
                                key=3
                            )
                
                
                
                if st.button("tambah", key='tambah'):
                    data_baru = pd.DataFrame([
                        {"Tahun": tahun, "Periode": periode, "Aktual": Aktual},
                    ])

                    st.session_state.df = pd.concat(
                        [st.session_state.df, data_baru],
                        ignore_index=True
                    )

                    st.rerun()

            
              


            else :
                st.markdown("""
                <div class="status-box-input">
                Tidak Ada Data
                </div>
            """, unsafe_allow_html=True)

st.markdown(css, unsafe_allow_html=True)

# suntikkan ke streamlit