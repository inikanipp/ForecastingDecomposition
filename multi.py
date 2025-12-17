
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

from io import BytesIO
from matplotlib.figure import Figure
from altair_saver import save
from io import BytesIO
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

st.title("DECOMPOSITION FORECASTING")
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
st.title("ADITIF DECOMPOSITION")
row3 = st.container()
row4 = st.container()
st.title("MULTIPLIKATIF DECOMPOSITION")
row5 = st.container()
row6 = st.container()
row7 = st.container()

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
            df = pd.read_excel('hasil.xlsx')
            trend = st.slider(label="",min_value=4, max_value=12)
            # =======================================================
            periode = df.columns.to_list()

            df.rename(columns={periode[0]: 'Tahun'}, inplace=True)
            df.rename(columns={periode[1]: 'Periode'}, inplace=True)
            df.rename(columns={periode[2]: 'Aktual'}, inplace=True)

            df['Aktual'] = pd.to_numeric(df['Aktual'], errors='coerce')
            df['MA'] = df['Aktual'].rolling(window=trend).mean().shift(1)

            df['CMA'] = (df['MA'] + df['MA'].shift(1)) / 2

            df['x'] = range(len(df))

            df['x2'] = df['x'] ** 2

            df['xy'] = df['x'] * df['Aktual']

            sum_y = df['Aktual'].sum()
            sum_x = df['x'].sum()
            sum_x2 = df['x2'].sum()
            sum_xy = df['xy'].sum()
            n = len(df)

            a = ((sum_y * sum_x2) - (sum_x * sum_xy)) / ((n * sum_x2) - (sum_x)** 2)
            b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x2) - (sum_x)** 2)

            df['CMAT'] = a + b * df['x']

            df['CF'] = df['CMA'] / df['CMAT']

            cfa = df.groupby('Periode')['Aktual'].sum()

            rasio = cfa / cfa.sum()

            periode = df['Periode'].nunique()

            SI = rasio*periode

            df['SI'] = df['Periode'].map(SI)

            df['FORECAST'] = df['CMAT']+df['CF']+df['SI']+1
            df['FORECAST_M'] = df['CMAT']*df['CF']*df['SI']*1

            MA_F = df['Aktual'].iloc[-trend:].mean()

            CMA_F = (MA_F + df['MA'].iloc[-1])/2

            X_F = df['x'].iloc[-1] + 1

            X2_F = X_F ** 2

            CMAT_F = a + b * X_F

            CF_F = CMA_F / CMAT_F

            SI_F = df['SI'].iloc[0]

            FORECAST = CMAT_F + CF_F + SI_F + 1
            FORECAST_M = CMAT_F * CF_F * SI_F * 1

            df_forecast_A = pd.DataFrame({'Tahun':[2025], 'Periode':['Januari'],'MA':[MA_F], 'CMA':[CMA_F], 'x':[X_F], 'x2':[X2_F], 'CMAT':[CMAT_F], 'CF':[CF_F], 'SI':[SI_F], 'FORECAST':[FORECAST]})
            df_forecast_M = pd.DataFrame({'Tahun':[2025], 'Periode':['Januari'],'MA':[MA_F], 'CMA':[CMA_F], 'x':[X_F], 'x2':[X2_F], 'CMAT':[CMAT_F], 'CF':[CF_F], 'SI':[SI_F], 'FORECAST':[FORECAST_M]})

            temp_df = df.dropna(subset=['Aktual', 'FORECAST'])

            mse = mean_squared_error(temp_df['Aktual'], temp_df['FORECAST'])
            rmse = np.sqrt(mse)
            mape = mean_absolute_percentage_error(temp_df['Aktual'], temp_df['FORECAST']) * 100
            r2 = r2_score(temp_df['Aktual'], temp_df['FORECAST'])

            mse_M = mean_squared_error(temp_df['Aktual'], temp_df['FORECAST_M'])
            rmse_M = np.sqrt(mse)
            mape_M = mean_absolute_percentage_error(temp_df['Aktual'], temp_df['FORECAST_M']) * 100
            r2_M = r2_score(temp_df['Aktual'], temp_df['FORECAST_M'])
            # =======================================================
            # =======================================================

    with col12:
        tile = st.container(height=140)

        with tile:
            st.markdown("""
            <div class="header-title">
            Intercept (a)
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div class="data-card">
                <div class="data-number">{a:.4f}</div>
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
            st.markdown(f"""
                <div class="data-card">
                <div class="data-number">{b:.4f}</div>
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
            # df = pd.read_excel('hasil.xlsx')
            if df is not None:
                column_names = df.columns.to_list()
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item month">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item month">{column_names[2]}</span>
                        <span class="date-item month">{column_names[3]}</span>
                        <span class="date-item month">{column_names[4]}</span>
                        <span class="date-item month">{column_names[5]}</span>
                        <span class="date-item month">{column_names[6]}</span>
                        <span class="date-item month">{column_names[7]}</span>
                        <span class="date-item month">{column_names[8]}</span>
                        <span class="date-item month">{column_names[9]}</span>
                        <span class="date-item month">{column_names[10]}</span>
                        <span class="date-item month">{column_names[11]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                for _, row in df.iterrows():
                    st.markdown(f"""
                        <div class="date-selector-container">
                            <span class="date-item month">{row['Tahun']}</span>
                            <span class="date-item month">{row['Periode']}</span>
                            <span class="date-item month">{row['Aktual']:.0f}</span>
                            <span class="date-item month">{row['MA']:.2f}</span>
                            <span class="date-item month">{row['CMA']:.2f}</span>
                            <span class="date-item month">{row['x']:.0f}</span>
                            <span class="date-item month">{row['x2']:.0f}</span>
                            <span class="date-item month">{row['xy']:.0f}</span>
                            <span class="date-item month">{row['CMAT']:.2f}</span>
                            <span class="date-item month">{row['CF']:.4f}</span>
                            <span class="date-item month">{row['SI']:.4f}</span>
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
from io import BytesIO
import matplotlib.pyplot as plt
import altair as alt

with row3:
    col4, col5 = st.columns([5,1])

    with col4:
        tile = st.container(height=360)

        with tile:
            st.markdown("""
                <div class="header-title">
                Line Chart
                </div>
            """, unsafe_allow_html=True)

            # ====== DATA LONG ======
            df_long = df.melt(
                id_vars='x',
                value_vars=['Aktual', 'FORECAST'],
                var_name='Tipe',
                value_name='Value'
            )

            # ====== ALTAIR (DISPLAY) ======
            chart = alt.Chart(df_long).mark_line().encode(
                x='x',
                y='Value',
                color=alt.Color(
                    'Tipe',
                    scale=alt.Scale(
                        domain=['Aktual', 'FORECAST'],
                        range=['#1f77b4', '#d62728']
                    ),
                    legend=alt.Legend(title='Data')
                )
            )

            st.altair_chart(chart, use_container_width=True)

            # ====== MATPLOTLIB (EXPORT) ======
            fig, ax = plt.subplots()
            for tipe, data in df_long.groupby("Tipe"):
                ax.plot(data["x"], data["Value"], label=tipe)

            ax.set_xlabel("x")
            ax.set_ylabel("Value")
            ax.legend()

            img_buffer = BytesIO()
            fig.savefig(img_buffer, format="png", bbox_inches="tight")
            plt.close(fig)
            img_buffer.seek(0)

            # ====== DOWNLOAD BUTTON ======
            st.download_button(
                "⬇️ Download Grafik (PNG)",
                data=img_buffer.getvalue(),
                file_name="line_chart_forecast_Aditif.png",
                mime="image/png"
            )

    # ========================= kolom 2 baris 2 =========================
    with col5 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                MSE
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                    <div class="data-card">
                    
                    <div class="data-label2">{mse:.4f}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="header-title">
                MAPE
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                    <div class="data-card">
                    
                    <div class="data-label2">{mape:.2f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # st.markdown("""
            #     <div class="header-title">
            #     R^2
            #     </div>
            # """, unsafe_allow_html=True)

            # st.markdown(f"""
            #         <div class="data-card">
                    
            #         <div class="data-label1">{r2:.4f}</div>
            #         </div>
            #     """, unsafe_allow_html=True)

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
            column_names = df.columns.to_list()
            df_a = df.iloc[0]
            if df is not None:
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item month">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item month">{column_names[3]}</span>
                        <span class="date-item month">{column_names[4]}</span>
                        <span class="date-item month">{column_names[5]}</span>
                        <span class="date-item month">{column_names[6]}</span>
                        <span class="date-item month">{column_names[8]}</span>
                        <span class="date-item month">{column_names[9]}</span>
                        <span class="date-item month">{column_names[10]}</span>
                        <span class="date-item month">{column_names[11]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                        <div class="date-selector-container">
                            <span class="date-item month">{df_a['Tahun']}</span>
                            <span class="date-item month">{df_a['Periode']}</span>
                            <span class="date-item month">{MA_F:.0f}</span>
                            <span class="date-item month">{CMA_F:.0f}</span>
                            <span class="date-item month">{X_F:.0f}</span>
                            <span class="date-item month">{X2_F:.0f}</span>
                            <span class="date-item month">{CMAT_F:.2f}</span>
                            <span class="date-item month">{CF_F:.4f}</span>
                            <span class="date-item month">{SI_F:.4f}</span>
                            <span class="date-item month">{FORECAST:.4f}</span>
                        </div>
                    """, unsafe_allow_html=True)
# ========================= end baris 4 =========================

# ========================= start baris 5 ========================
with row5:
    col6, col7 = st.columns([5,1])

    with col6:
        tile = st.container(height=360)

        with tile:
            st.markdown("""
                <div class="header-title">
                Line Chart
                </div>
            """, unsafe_allow_html=True)

            # ====== DATA LONG ======
            df_long = df.melt(
                id_vars='x',
                value_vars=['Aktual', 'FORECAST_M'],
                var_name='Tipe',
                value_name='Value'
            )

            # ====== ALTAIR (DISPLAY) ======
            chart = alt.Chart(df_long).mark_line().encode(
                x='x',
                y='Value',
                color=alt.Color(
                    'Tipe',
                    scale=alt.Scale(
                        domain=['Aktual', 'FORECAST_M'],
                        range=['#1f77b4', '#d62728']
                    ),
                    legend=alt.Legend(title='Data')
                )
            )

            st.altair_chart(chart, use_container_width=True)

            # ====== MATPLOTLIB (EXPORT) ======
            figm, ax = plt.subplots()
            for tipe, data in df_long.groupby("Tipe"):
                ax.plot(data["x"], data["Value"], label=tipe)

            ax.set_xlabel("x")
            ax.set_ylabel("Value")
            ax.legend()

            img_bufferm = BytesIO()
            figm.savefig(img_bufferm, format="png", bbox_inches="tight")
            plt.close(figm)
            img_bufferm.seek(0)

            # ====== DOWNLOAD BUTTON ======
            st.download_button(
                "⬇️ Download Grafik (PNG)",
                data=img_bufferm.getvalue(),
                file_name="line_chart_forecast_Muiltiplikatif.png",
                mime="image/png"
            )

    # ========================= kolom 2 baris 2 =========================
    with col7 :
        tile = st.container(height=360)

        with tile :
            st.markdown("""
                <div class="header-title">
                MSE
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                    <div class="data-card">
                    
                    <div class="data-label2">{mse_M:.4f}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="header-title">
                MAPE
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                    <div class="data-card">
                    
                    <div class="data-label2">{mape_M:.2f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # st.markdown("""
            #     <div class="header-title">
            #     R^2
            #     </div>
            # """, unsafe_allow_html=True)

            # st.markdown(f"""
            #         <div class="data-card">
                    
            #         <div class="data-label1">{r2_M:.4f}</div>
            #         </div>
            #     """, unsafe_allow_html=True)

# ========================= end baris 5 =========================


# ========================= start baris 6 =========================
with row6:
    col8= st.columns(1)[0]
    # ========================= kolom 1 baris 2 =========================
    with col8 :
        tile = st.container(height=160)

        with tile :
            st.markdown("""
                <div class="header-title">
                Chart Plot
                </div>
            """, unsafe_allow_html=True)
            column_names = df.columns.to_list()
            df_m = df.iloc[0]
            if df is not None:
                st.markdown(f"""
                        <div class="date-selector-container-header">
                        <span class="date-item month">{column_names[0]}</span>
                        <span class="date-item month">{column_names[1]}</span>
                        <span class="date-item month">{column_names[3]}</span>
                        <span class="date-item month">{column_names[4]}</span>
                        <span class="date-item month">{column_names[5]}</span>
                        <span class="date-item month">{column_names[6]}</span>
                        <span class="date-item month">{column_names[8]}</span>
                        <span class="date-item month">{column_names[9]}</span>
                        <span class="date-item month">{column_names[10]}</span>
                        <span class="date-item month">{column_names[11]}</span>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                        <div class="date-selector-container">
                            <span class="date-item month">{df_m['Tahun']}</span>
                            <span class="date-item month">{df_m['Periode']}</span>
                            <span class="date-item month">{MA_F:.0f}</span>
                            <span class="date-item month">{CMA_F:.0f}</span>
                            <span class="date-item month">{X_F:.0f}</span>
                            <span class="date-item month">{X2_F:.0f}</span>
                            <span class="date-item month">{CMAT_F:.2f}</span>
                            <span class="date-item month">{CF_F:.4f}</span>
                            <span class="date-item month">{SI_F:.4f}</span>
                            <span class="date-item month">{FORECAST_M:.4f}</span>
                        </div>
                    """, unsafe_allow_html=True)
                # output = BytesIO()
                # with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                #     df.to_excel(writer, index=False, sheet_name="Hasil_MA")

                # st.download_button(
                #     label="⬇️ Download Data (Excel)",
                #     data=output.getvalue(),
                #     file_name=f"hasil_moving_average_{trend}.xlsx",
                #     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                # )
# ========================= end baris 6 ==========================

# ========================= start baris 7 ===========================
with row7:
    col8 = st.columns([1])[0]

    with col8:
        tile = st.container(height=200)

        with tile:
            st.markdown("""
                <div class="header-title">
                Download Forecast (Excel)
                </div>
            """, unsafe_allow_html=True)

            # ================= PILIH METODE =================
            metode = st.radio(
                "Pilih metode forecast",
                ["Additive", "Multiplicative"],
                horizontal=True,
                key="metode_forecast"
            )

            # ================= PILIH DATA & METRIK =================
            if metode == "Additive":
                df_export = df.copy()
                df_export = df_export.drop(columns=["FORECAST_M"], errors="ignore")

                mse_export = mse
                mape_export = mape

            else:  # Multiplicative
                df_export = df.copy()
                df_export = df_export.drop(columns=["FORECAST"], errors="ignore")

                mse_export = mse_M
                mape_export = mape_M

            # ================= INFO =================
            info_df = pd.DataFrame({
                "Keterangan": [
                    "Metode",
                    "Intercept (a)",
                    "Slope (b)",
                    "MSE",
                    "MAPE (%)"
                ],
                "Nilai": [
                    metode,
                    a,
                    b,
                    mse_export,
                    mape_export
                ]
            })

            # ================= EXCEL (1 SHEET) =================
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df_export.to_excel(
                    writer,
                    index=False,
                    sheet_name="Forecast",
                    startrow=0
                )

                info_df.to_excel(
                    writer,
                    index=False,
                    sheet_name="Forecast",
                    startrow=len(df_export) + 3
                )

            # ================= DOWNLOAD =================
            st.download_button(
                label="⬇️ Download Hasil Forecast Lengkap",
                data=output.getvalue(),
                file_name=f"forecast_{metode.lower()}_lengkap.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# ========================= end baris 7 =============================
st.markdown(css, unsafe_allow_html=True)

# suntikkan ke streamlit