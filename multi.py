import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

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
row3 = st.container()
row4 = st.container()

# ========================= layout =========================

# ========================= start baris 1 =========================
with row1:
    col11, col12, col13 = st.columns([1,2,2])  # hanya 1 kolom (kiri)

    with col11:
        tile = st.container(height=140)

        with tile:
            st.markdown("""
                <div class="header-title">
                Seasonal
                </div>
            """, unsafe_allow_html=True)
            st.slider(label="",min_value=4, max_value=12)
    with col12:
        tile = st.container(height=140)

        with tile:
            st.markdown("""
            <div class="header-title">
            Intercept (a)
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="data-card">
                <div class="data-number">8608,9640</div>
                </div>
            """, unsafe_allow_html=True)
        
    
    with col13:
        tile = st.container(height=140)

        with tile:
            st.markdown("""
                <div class="header-title">
                Slope (b)
                </div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div class="data-card">
                <div class="data-number">8608,9640</div>
                </div>
            """, unsafe_allow_html=True)

# ========================= end baris 1 =========================



# ========================= start baris 2 =========================
with row2:
    col5 = st.columns(1)[0]
   
    # ========================= kolom 2 baris 2 =========================
    with col5 :
        tile = st.container(height=410)

        with tile :
            st.markdown("""
                <div class="header-title">
                Table
                </div>
            """, unsafe_allow_html=True)
            uplodaed_files = True
            df = pd.read_excel('hasil.xlsx')
            if df is not None:
                column_names = df.columns.to_list()
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item year">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item year">{column_names[2]}</span>
                        <span class="date-item year">{column_names[3]}</span>
                        <span class="date-item month">{column_names[4]}</span>
                        <span class="date-item year">{column_names[5]}</span>
                        <span class="date-item year">{column_names[6]}</span>
                        <span class="date-item month">{column_names[7]}</span>
                        <span class="date-item year">{column_names[8]}</span>
                        <span class="date-item year">{column_names[9]}</span>
                        <span class="date-item month">{column_names[10]}</span>
                        <span class="date-item year">{column_names[11]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                for _, row in df.iterrows():
                    st.markdown(f"""
                        <div class="date-selector-container">
                            <span class="date-item year">{row['Tahun']}</span>
                            <span class="date-item month">{row['Bulan']}</span>
                            <span class="date-item month">{row['Nilai']:.2f}</span>
                            <span class="date-item year">{row['MA']:.2f}</span>
                            <span class="date-item year">{row['CMA']:.2f}</span>
                            <span class="date-item month">{row['x']:.2f}</span>
                            <span class="date-item year">{row['x2']:.2f}</span>
                            <span class="date-item year">{row['xy']:.2f}</span>
                            <span class="date-item month">{row['CMAT']:.2f}</span>
                            <span class="date-item year">{row['CF']:.2f}</span>
                            <span class="date-item year">{row['SI']:.2f}</span>
                            <span class="date-item month">{row['FORECAST']:.2f}</span>
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


# ========================= start baris 3 =========================
with row3:
    col4, col5 = st.columns([5,1])
    # ========================= kolom 1 baris 2 =========================
    with col4 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                Line Chart
                </div>
            """, unsafe_allow_html=True)

            df_long = df.melt(
                id_vars='x',
                value_vars=['Nilai', 'FORECAST'],
                var_name='Tipe',
                value_name='Value'
            )

            chart = alt.Chart(df_long).mark_line().encode(
                x='x',
                y='Value',
                color=alt.Color(
                    'Tipe',
                    scale=alt.Scale(
                        domain=['Nilai', 'FORECAST'],
                        range=['#1f77b4', '#d62728']
                    ),
                    legend=alt.Legend(title='Data')
                )
            )

            st.altair_chart(chart, use_container_width=True)

            

    # ========================= kolom 2 baris 2 =========================
    with col5 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                RMSE
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                    <div class="data-card">
                    
                    <div class="data-label2">5659.3719</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="header-title">
                MAPE
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                    <div class="data-card">
                    
                    <div class="data-label2">30.1369%</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="header-title">
                R^2
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                    <div class="data-card">
                    
                    <div class="data-label1">0.4122</div>
                    </div>
                """, unsafe_allow_html=True)
            
    
           
           



# ========================= end baris 3 =========================


# ========================= start baris 4 =========================
with row4:
    col4= st.columns(1)[0]
    # ========================= kolom 1 baris 2 =========================
    with col4 :
        tile = st.container(height=160)

        with tile :
            st.markdown("""
                <div class="header-title">
                Chart Plot
                </div>
            """, unsafe_allow_html=True)
            df = pd.read_excel('hasil.xlsx')
            column_names = df.columns.to_list()
            df = df.iloc[0]
            # df = df.reset_index()
            if df is not None:
                # column_names = df.columns.to_list()
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item year">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item year">{column_names[2]}</span>
                        <span class="date-item year">{column_names[3]}</span>
                        <span class="date-item month">{column_names[4]}</span>
                        <span class="date-item year">{column_names[5]}</span>
                        <span class="date-item year">{column_names[6]}</span>
                        <span class="date-item month">{column_names[7]}</span>
                        <span class="date-item year">{column_names[8]}</span>
                        <span class="date-item year">{column_names[9]}</span>
                        <span class="date-item month">{column_names[10]}</span>
                        <span class="date-item year">{column_names[11]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                        <div class="date-selector-container">
                            <span class="date-item year">{df['Tahun']}</span>
                            <span class="date-item month">{df['Bulan']}</span>
                            <span class="date-item month">{df['Nilai']:.2f}</span>
                            <span class="date-item year">{df['MA']:.2f}</span>
                            <span class="date-item year">{df['CMA']:.2f}</span>
                            <span class="date-item month">{df['x']:.2f}</span>
                            <span class="date-item year">{df['x2']:.2f}</span>
                            <span class="date-item year">{df['xy']:.2f}</span>
                            <span class="date-item month">{df['CMAT']:.2f}</span>
                            <span class="date-item year">{df['CF']:.2f}</span>
                            <span class="date-item year">{df['SI']:.2f}</span>
                            <span class="date-item month">{df['FORECAST']:.2f}</span>
                        </div>
                    """, unsafe_allow_html=True)
    
           
          



# ========================= end baris 4 =========================


st.markdown(css, unsafe_allow_html=True)

# suntikkan ke streamlit