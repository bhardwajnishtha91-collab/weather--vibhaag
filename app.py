import streamlit as st
import time
import streamlit.components.v1 as components
import pandas as pd
import random
from datetime import date, timedelta

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Weather Vibhag",
    page_icon="weather_vibhag_logo.jpg",
    layout="wide"
)
# -------------------------------------------------
# ANIMATED WEATHER BACKGROUND
# -------------------------------------------------

st.markdown("""
<style>

/* =================================================
   STREAMLIT BACKGROUND
   ================================================= */

.stApp {
    background: transparent !important;
}

.main {
    background: transparent !important;
}

.block-container {
    position: relative;
    z-index: 10;
}


/* =================================================
   WEATHER ANIMATION STAGE
   ================================================= */

.weather-stage {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;

    overflow: hidden;
    pointer-events: none;

    z-index: 0;

    background: transparent;
}


/* =================================================
   COMMON SCENE
   ================================================= */

.weather-scene {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    opacity: 0;
}


/* =================================================
   SUN
   ================================================= */

.sun-scene {
    background:
        radial-gradient(
            circle at 50% 25%,
            rgba(255, 245, 150, 0.90) 0%,
            rgba(255, 210, 70, 0.55) 18%,
            rgba(255, 180, 30, 0.25) 38%,
            rgba(255, 170, 20, 0.08) 60%,
            transparent 75%
        );

    animation: sunnyScene 25s infinite;
}

.sun {
    position: absolute;

    top: 8%;
    left: 50%;

    transform: translateX(-50%);

    font-size: 150px;

    filter:
        drop-shadow(0 0 25px #fff176)
        drop-shadow(0 0 60px #ffd54f)
        drop-shadow(0 0 100px #ffb300);

    animation: sunGlow 2s ease-in-out infinite alternate;
}

@keyframes sunGlow {

    from {
        transform: translateX(-50%) scale(1);
    }

    to {
        transform: translateX(-50%) scale(1.08);
    }
}


/* =================================================
   CLOUDS
   ================================================= */

.cloud {
    position: absolute;

    font-size: 75px;

    opacity: 0.75;

    white-space: nowrap;

    animation: cloudMove 18s linear infinite;
}

.cloud1 {
    top: 12%;
    left: -10%;
}

.cloud2 {
    top: 24%;
    left: 12%;
    animation-delay: 3s;
}

.cloud3 {
    top: 8%;
    left: 42%;
    animation-delay: 6s;
}

.cloud4 {
    top: 30%;
    left: 65%;
    animation-delay: 2s;
}

.cloud5 {
    top: 18%;
    left: 82%;
    animation-delay: 8s;
}

@keyframes cloudMove {

    from {
        transform: translateX(-120px);
    }

    to {
        transform: translateX(120vw);
    }
}


/* =================================================
   RAIN
   ================================================= */

.rain-scene {
    background:
        linear-gradient(
            rgba(30, 70, 120, 0.72),
            rgba(15, 35, 75, 0.88)
        );

    animation: rainyScene 25s infinite;
}

.rain {
    position: absolute;

    inset: 0;
}

.drop {
    position: absolute;

    top: -80px;

    width: 4px;
    height: 65px;

    background:
        linear-gradient(
            transparent,
            #8fd8ff,
            #ffffff
        );

    border-radius: 50%;

    opacity: 0.9;

    animation: rainFall 1s linear infinite;
}

@keyframes rainFall {

    to {
        transform: translateY(115vh);
    }
}


/* =================================================
   SNOW
   ================================================= */

.snow-scene {
    background:
        radial-gradient(
            circle at 50% 35%,
            rgba(220, 245, 255, 0.55),
            rgba(100, 170, 220, 0.45),
            rgba(35, 75, 120, 0.82)
        );

    animation: snowyScene 25s infinite;
}

.snowflake {
    position: absolute;

    top: -60px;

    color: white;

    font-size: 32px;

    text-shadow:
        0 0 8px white,
        0 0 18px #bdefff;

    animation: snowFall 5s linear infinite;
}

@keyframes snowFall {

    to {
        transform:
            translateY(115vh)
            rotate(360deg);
    }
}


/* =================================================
   AUTUMN LEAVES
   ================================================= */

.autumn-scene {
    background:
        radial-gradient(
            circle at 50% 40%,
            rgba(255, 190, 70, 0.45),
            rgba(145, 70, 20, 0.65),
            rgba(55, 25, 10, 0.88)
        );

    animation: autumnScene 25s infinite;
}

.leaf {
    position: absolute;

    top: -70px;

    font-size: 34px;

    filter:
        drop-shadow(
            0 0 6px rgba(255, 150, 40, 0.7)
        );

    animation: leafFall 5s linear infinite;
}

@keyframes leafFall {

    to {
        transform:
            translateY(115vh)
            translateX(120px)
            rotate(360deg);
    }
}


/* =================================================
   THUNDERSTORM
   ================================================= */

.thunder-scene {
    background:
        radial-gradient(
            circle at 50% 35%,
            rgba(110, 120, 135, 0.65),
            rgba(35, 40, 48, 0.92),
            rgba(8, 10, 15, 0.98)
        );

    animation: thunderScene 25s infinite;
}

.lightning {
    position: absolute;

    top: 5%;
    left: 50%;

    transform: translateX(-50%);

    font-size: 230px;

    color: white;

    text-shadow:
        0 0 15px white,
        0 0 35px #b8eaff,
        0 0 70px #6ec8ff,
        0 0 120px white;

    animation: lightningFlash 2s infinite;
}

.storm-flash {
    position: absolute;

    inset: 0;

    background: rgba(255, 255, 255, 0.9);

    animation: flash 2s infinite;
}

@keyframes lightningFlash {

    0%,
    80%,
    100% {
        opacity: 0;
    }

    82%,
    86% {
        opacity: 1;
    }

    84% {
        opacity: 0.25;
    }
}

@keyframes flash {

    0%,
    80%,
    100% {
        opacity: 0;
    }

    82%,
    84% {
        opacity: 0.35;
    }

    86% {
        opacity: 0;
    }
}


/* =================================================
   25 SECOND WEATHER CYCLE
   ================================================= */

@keyframes sunnyScene {

    0%,
    18% {
        opacity: 1;
    }

    20%,
    100% {
        opacity: 0;
    }
}

@keyframes rainyScene {

    0%,
    19% {
        opacity: 0;
    }

    20%,
    38% {
        opacity: 1;
    }

    40%,
    100% {
        opacity: 0;
    }
}

@keyframes snowyScene {

    0%,
    39% {
        opacity: 0;
    }

    40%,
    58% {
        opacity: 1;
    }

    60%,
    100% {
        opacity: 0;
    }
}

@keyframes autumnScene {

    0%,
    59% {
        opacity: 0;
    }

    60%,
    78% {
        opacity: 1;
    }

    80%,
    100% {
        opacity: 0;
    }
}

@keyframes thunderScene {

    0%,
    79% {
        opacity: 0;
    }

    80%,
    98% {
        opacity: 1;
    }

    100% {
        opacity: 0;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================
# ANIMATED WEATHER SCENE
# ========================
st.markdown("""
<style>
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-35px); }
    100% { transform: translateY(0px); }
}

.weather-emojis {
    font-size: 70px;
    text-align: center;
    padding: 25px;
    animation: float 3s ease-in-out infinite;
background: linear-gradient(180deg, #87CEEB, #EAF8FF);
border-radius: 25px;
box-shadow: 0 8px 25px rgba(0, 120, 200, 0.25);
}
.weather-icon {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 80px;
    opacity: 0;
}

.sun {
    animation: sunScene 90s infinite;
}

.cloud {
    animation: cloudScene 90s infinite;
}

.rain {
    animation: rainScene 90s infinite;
}

.storm {
    animation: stormScene 90s infinite;
}

.night {
    animation: nightScene 90s infinite;
}

.wind {
    animation: windScene 90s infinite;
}

@keyframes sunScene {
    0%, 2% { opacity: 0; }
    4%, 14% { opacity: 1; }
    16.66%, 100% { opacity: 0; }
}

@keyframes cloudScene {
    0%, 14% { opacity: 0; }
    16.66%, 30% { opacity: 1; }
    33.33%, 100% { opacity: 0; }
}

@keyframes rainScene {
    0%, 30% { opacity: 0; }
    33.33%, 47% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 0; }
}

@keyframes stormScene {
    0%, 47% { opacity: 0; }
    50%, 64% { opacity: 1; }
    66.66%, 100% { opacity: 0; }
}

@keyframes nightScene {
    0%, 64% { opacity: 0; }
    66.66%, 80% { opacity: 1; }
    83.33%, 100% { opacity: 0; }
}

@keyframes windScene {
    0%, 80% { opacity: 0; }
    83.33%, 97% { opacity: 1; }
    100% { opacity: 0; }
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="weather-emojis">

    <div class="weather-scene sunScene">
        <div class="big-sun">☀️</div>
    </div>

    <div class="weather-scene cloudScene">
        <div class="cloud c1">☁️</div>
        <div class="cloud c2">☁️</div>
        <div class="cloud c3">☁️</div>
        <div class="cloud c4">☁️</div>
        <div class="cloud c5">☁️</div>
    </div>

    <div class="weather-scene rainScene">
        <div class="cloud rcloud">☁️</div>
        <div class="rain-drops">||||||||||||||||||||||||</div>
    </div>

    <div class="weather-scene stormScene">
        <div class="storm-cloud">🌩️</div>
        <div class="lightning">⚡</div>
    </div>

    <div class="weather-scene nightScene">
        <div class="moon">🌙</div>
        <div class="stars">✦　✧　⋆　✦　⋆　✧　✦　⋆</div>
    </div>

    <div class="weather-scene windScene">
        <div class="wind-lines">〰️　〰️　〰️</div>
        <div class="wind-cloud">☁️</div>
    </div>

</div>
""", unsafe_allow_html=True)
    

# -------------------------------------------------
# SAMPLE DELHI WEATHER DATA
# -------------------------------------------------
@st.cache_data
def create_weather_data():

    random.seed(10)

    start_date = date(2025, 1, 1)
    data = []

    for i in range(365):

        current_date = start_date + timedelta(days=i)
        month = current_date.month

        # Seasonal temperature pattern for Delhi
        if month in [1, 2]:
            temperature = random.uniform(8, 24)
        elif month in [3, 4]:
            temperature = random.uniform(18, 35)
        elif month in [5, 6]:
            temperature = random.uniform(28, 45)
        elif month in [7, 8]:
            temperature = random.uniform(27, 38)
        elif month in [9, 10]:
            temperature = random.uniform(20, 35)
        else:
            temperature = random.uniform(10, 27)

        # Humidity
        if month in [7, 8]:
            humidity = random.uniform(60, 90)
        elif month in [5, 6]:
            humidity = random.uniform(35, 65)
        else:
            humidity = random.uniform(30, 75)

        # Rainfall
        if month in [7, 8]:
            rainfall = random.uniform(0, 80)
        elif month in [6, 9]:
            rainfall = random.uniform(0, 40)
        else:
            rainfall = random.uniform(0, 10)

        data.append({
            "Date": current_date,
            "Temperature (°C)": round(temperature, 1),
            "Humidity (%)": round(humidity, 1),
            "Rainfall (mm)": round(rainfall, 1)
        })

    return pd.DataFrame(data)


df = create_weather_data()


# -------------------------------------------------
# LOGIN SYSTEM
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -------------------------------------------------
# MODULE 2 - SIGN IN
# -------------------------------------------------
if not st.session_state.logged_in:

    st.title("🌦️ Delhi Weather Data Analysis")

    st.subheader("🔐 Sign In")

    st.write("Please login to access the Weather Analytics Dashboard.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In", use_container_width=True):

        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            st.rerun()

        else:
            st.error("Invalid username or password.")

    st.info("Demo Login → Username: admin | Password: 1234")

    st.stop()


# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------
st.sidebar.title("🌦️ Weather Dashboard")

st.sidebar.write("Welcome, Admin 👋")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Homepage",
        "📊 Weather Analytics",
        "💡 Weather Insights"
    ]
)

if st.sidebar.button("🚪 Logout", use_container_width=True):

    st.session_state.logged_in = False
    st.rerun()


# =================================================
# =================================================
if page == "🏠 Homepage":

    st.title("🌦️ Delhi Weather Data Analysis")

    st.subheader("Project Introduction")

    st.write(
        """
        This project is a Python and Streamlit based Weather Data Analysis
        application. It analyzes temperature, humidity and rainfall data
        for Delhi and presents the information using interactive charts
        and statistical insights.
        """
    )

    st.divider()

    st.header("🌤️ What is Weather Data Analysis?")

    st.write(
        """
        Weather Data Analysis is the process of collecting, organizing
        and analyzing weather information such as temperature, humidity
        and rainfall. Data analytics helps us identify patterns,
        comparisons and seasonal trends in weather conditions.
        """
    )

    st.divider()

    st.header("📚 Project Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            - Project introduction  
            - Weather Data Analysis explanation  
            - Navigation """
        )

        st.info("""
        Module 2 - Sign In / Logout**

            - Username/password login  
            - Secure session-based access  
            - Logout functionality"""
        )

    with col2:
        st.info("""
        Module 3 - Weather Analytics**

            - Temperature analysis  
            - Humidity analysis  
            - Rainfall analysis  
            - Charts and comparisons"""
        )

        st.info("""
        Module 4 - Weather Insights**

            - Hottest/coldest day  
            - Highest rainfall day  
            - Seasonal trends  
            - Temperature vs humidity
            """)

    st.divider()

    st.success(
        "📍 Location: Delhi | 📅 Dataset: Sample 2025 Weather Data"
    )


# =================================================
# MODULE 3 - WEATHER ANALYTICS
# =================================================
elif page == "📊 Weather Analytics":

    st.title("📊 Weather Analytics")

    st.write(
        "Analyze temperature, humidity and rainfall patterns in Delhi."
    )

    # -----------------------------
    # SUMMARY
    # -----------------------------
    st.subheader("📌 Weather Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Temperature",
            f"{df['Temperature (°C)'].mean():.1f} °C"
        )

    with col2:
        st.metric(
            "Average Humidity",
            f"{df['Humidity (%)'].mean():.1f} %"
        )

    with col3:
        st.metric(
            "Total Rainfall",
            f"{df['Rainfall (mm)'].sum():.1f} mm"
        )

    st.divider()

    # -----------------------------
    # DATE FILTER
    # -----------------------------
    st.subheader("📅 Date Filter")

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    selected_dates = st.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(selected_dates) == 2:

        filtered_df = df[
            (df["Date"] >= selected_dates[0]) &
            (df["Date"] <= selected_dates[1])
        ]

    else:
        filtered_df = df

    # -----------------------------
    # TEMPERATURE
    # -----------------------------
    st.subheader("🌡️ Temperature Analysis")

    st.write(
        f"Average: **{filtered_df['Temperature (°C)'].mean():.2f} °C**"
    )

    st.write(
        f"Minimum: **{filtered_df['Temperature (°C)'].min():.2f} °C**"
    )

    st.write(
        f"Maximum: **{filtered_df['Temperature (°C)'].max():.2f} °C**"
    )

    temperature_chart = filtered_df.set_index("Date")[
        ["Temperature (°C)"]
    ]

    st.line_chart(temperature_chart)

    # -----------------------------
    # HUMIDITY
    # -----------------------------
    st.subheader("💧 Humidity Analysis")

    humidity_chart = filtered_df.set_index("Date")[
        ["Humidity (%)"]
    ]

    st.line_chart(humidity_chart)

    # -----------------------------
    # RAINFALL
    # -----------------------------
    st.subheader("🌧️ Rainfall Analysis")

    rainfall_chart = filtered_df.set_index("Date")[
        ["Rainfall (mm)"]
    ]

    st.bar_chart(rainfall_chart)

    # -----------------------------
    # MONTHLY COMPARISON
    # -----------------------------
    st.subheader("📅 Monthly Weather Comparison")

    monthly_data = df.copy()

    monthly_data["Month"] = monthly_data["Date"].dt.strftime("%B")

    monthly_avg = (
        monthly_data
        .groupby("Month")[
            [
                "Temperature (°C)",
                "Humidity (%)",
                "Rainfall (mm)"
            ]
        ]
        .mean()
    )

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    monthly_avg = monthly_avg.reindex(month_order)

    st.dataframe(monthly_avg.round(2))

    st.subheader("🌡️ Average Monthly Temperature")

    st.bar_chart(
        monthly_avg[["Temperature (°C)"]]
    )


# =================================================
# MODULE 4 - WEATHER INSIGHTS
# =================================================
elif page == "💡 Weather Insights":

    st.title("💡 Weather Insights")

    st.write(
        "Important insights generated from the Delhi weather dataset."
    )

    # -----------------------------
    # HOTTEST DAY
    # -----------------------------
    hottest = df.loc[
        df["Temperature (°C)"].idxmax()
    ]

    # -----------------------------
    # COLDEST DAY
    # -----------------------------
    coldest = df.loc[
        df["Temperature (°C)"].idxmin()
    ]

    # -----------------------------
    # HIGHEST RAINFALL
    # -----------------------------
    highest_rainfall = df.loc[
        df["Rainfall (mm)"].idxmax()
    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔥 Hottest Day",
            str(hottest["Date"]),
            f"{hottest['Temperature (°C)']} °C"
        )

    with col2:
        st.metric(
            "❄️ Coldest Day",
            str(coldest["Date"]),
            f"{coldest['Temperature (°C)']} °C"
        )

    with col3:
        st.metric(
            "🌧️ Highest Rainfall",
            str(highest_rainfall["Date"]),
            f"{highest_rainfall['Rainfall (mm)']} mm"
        )

    st.divider()

    # -----------------------------
    # SEASONAL TRENDS
    # -----------------------------
    st.subheader("🌤️ Seasonal Trends")

    seasonal = df.copy()

    def get_season(month):

        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Summer"
        elif month in [6, 7, 8, 9]:
            return "Monsoon"
        else:
            return "Autumn"

    seasonal["Date"] = pd.to_datetime(seasonal["Date"],errors="coerce")

    seasonal["Season"] =seasonal["Date"].dt.month.apply(get_season)
    season_data=(
          seasonal
        .groupby("Season")[
            [
                "Temperature (°C)",
                "Humidity (%)",
                "Rainfall (mm)"
            ]
        ]
        .mean()
    )

    st.dataframe(season_data.round(2))

    st.bar_chart(
        season_data[["Temperature (°C)"]]
    )

    # -----------------------------
    # TEMPERATURE VS HUMIDITY
    # -----------------------------
    st.subheader("🌡️ Temperature vs Humidity")

    correlation = df[
        ["Temperature (°C)", "Humidity (%)"]
    ].corr().iloc[0, 1]

    st.metric(
        label="Temperature-Humidity Correlation",
        value=f"{correlation:.2f}"
    )

    st.line_chart(
        df.set_index("Date")[
            ["Temperature (°C)", "Humidity (%)"]
        ]
    )

    st.info(
        "The correlation value shows the statistical relationship between "
        "temperature and humidity in the sample dataset."
    )

    # -----------------------------
    # DATA TABLE
    # -----------------------------
    st.subheader("📋 Weather Data")

    st.dataframe(
        df,
        use_container_width=True
    )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption("Delhi Weather Data Analysis | Python + Streamlit + Data Analytics")




























