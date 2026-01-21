# import streamlit as st
# import pandas as pd
# import pickle

# # -------------------- PAGE CONFIG --------------------
# st.set_page_config(
#     page_title="IPL Win Predictor",
#     page_icon="🏏",
#     layout="wide"
# )

# # -------------------- CUSTOM CSS (ALL IN ONE BLOCK) --------------------
# st.markdown("""
# <style>

# /* App background */
# .stApp {
#     background: linear-gradient(135deg, #0f172a 0%, #111827 40%, #0b1220 100%);
#     color: white;
# }

# /* FIX: Make all input labels readable */
# label {
#     color: #f1f5f9 !important;   /* very light gray */
#     font-weight: 700 !important;
#     font-size: 15px !important;
# }

# /* Selectbox & number input labels */
# div.stSelectbox > label,
# div.stNumberInput > label {
#     color: #f1f5f9 !important;
# }

# /* Card style */
# .card {
#     background: rgba(255, 255, 255, 0.06);
#     border: 1px solid rgba(255, 255, 255, 0.12);
#     border-radius: 18px;
#     padding: 18px;
#     box-shadow: 0 10px 25px rgba(0,0,0,0.25);
# }

# /* Big header ribbon */
# .ribbon {
#     background: linear-gradient(90deg, rgba(59,130,246,0.35), rgba(147,51,234,0.35));
#     border: 1px solid rgba(255,255,255,0.12);
#     border-radius: 18px;
#     padding: 18px 20px;
#     margin-bottom: 16px;
# }

# /* Buttons */
# .stButton > button {
#     width: 100%;
#     border-radius: 14px;
#     padding: 0.75rem 1rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #22c55e, #3b82f6);
#     border: 0px;
#     color: white;
#     transition: transform 0.05s ease-in-out;
# }
# .stButton > button:active {
#     transform: scale(0.99);
# }

# /* Inputs */
# div[data-baseweb="select"] > div,
# .stNumberInput input {
#     border-radius: 12px !important;
# }

# /* Hide Streamlit footer */
# footer {visibility: hidden;}

# </style>
# """, unsafe_allow_html=True)

# # -------------------- HEADER / BANNER --------------------
# st.markdown("""
# <div class="ribbon">
#     <div style="display:flex; align-items:center; gap:14px;">
#         <div style="font-size:34px;">🏏</div>
#         <div>
#             <div style="font-size:28px; font-weight:800; line-height:1;">IPL Win Predictor</div>
#             <div style="opacity:0.85; margin-top:6px;">
#                 Predict win probability with match situation — styled dashboard UI
#             </div>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # -------------------- SMALL INFO CARDS --------------------
# top1, top2, top3 = st.columns([1.3, 1, 1])

# with top1:
#     st.markdown('<div class="card">🔥 <b>Tip:</b> Enter overs as decimal (e.g., 5.333 for 5 overs 2 balls).</div>', unsafe_allow_html=True)

# with top2:
#     st.markdown('<div class="card">📊 <b>Live-style UI</b><br/>Progress bars + metric cards</div>', unsafe_allow_html=True)

# with top3:
#     st.markdown('<div class="card">⚡ <b>Fast</b><br/>Uses your saved ML pipeline (pipe.pkl)</div>', unsafe_allow_html=True)

# # -------------------- TEAM LOGOS --------------------
# team_logos = {
#     "Sunrisers Hyderabad": "https://upload.wikimedia.org/wikipedia/en/8/81/Sunrisers_Hyderabad.svg",
#     "Mumbai Indians": "https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg",
#     "Royal Challengers Bangalore": "https://upload.wikimedia.org/wikipedia/en/0/0d/Royal_Challengers_Bangalore_Logo.svg",
#     "Kolkata Knight Riders": "https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg",
#     "Kings XI Punjab": "https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg",
#     "Chennai Super Kings": "https://upload.wikimedia.org/wikipedia/en/2/2b/Chennai_Super_Kings_Logo.svg",
#     "Rajasthan Royals": "https://upload.wikimedia.org/wikipedia/en/6/60/Rajasthan_Royals_Logo.svg",
#     "Delhi Capitals": "https://upload.wikimedia.org/wikipedia/en/2/2f/Delhi_Capitals.svg",
# }

# # -------------------- ORIGINAL MODEL CODE --------------------

# teams = ['Sunrisers Hyderabad',
#          'Mumbai Indians',
#          'Royal Challengers Bangalore',
#          'Kolkata Knight Riders',
#          'Kings XI Punjab',
#          'Chennai Super Kings',
#          'Rajasthan Royals',
#          'Delhi Capitals']

# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
#           'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
#           'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#           'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#           'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#           'Sharjah', 'Mohali', 'Bengaluru']

# pipe = pickle.load(open('pipe.pkl', 'rb'))

# # -------------------- INPUT CARD --------------------
# st.markdown('<div class="card">', unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col1:
#     battingteam = st.selectbox('🏏 Select the batting team', sorted(teams))

# with col2:
#     bowlingteam = st.selectbox('🎯 Select the bowling team', sorted(teams))

# city = st.selectbox(
#     '📍 Select the city where the match is being played', sorted(cities))

# target = st.number_input('🎯 Target')

# col3, col4, col5 = st.columns(3)

# with col3:
#     score = st.number_input('🟢 Score')

# with col4:
#     overs = st.number_input('⏱️ Overs Completed')

# with col5:
#     wickets = st.number_input('❌ Wickets Fallen')

# st.markdown('</div>', unsafe_allow_html=True)

# # -------------------- TEAM VISUALS --------------------
# logo1, mid, logo2 = st.columns([1, 2, 1])

# with logo1:
#     try:
#         st.image(team_logos.get(battingteam, ""), use_container_width=True)
#     except:
#         pass

# with mid:
#     st.markdown(
#         '<div class="card" style="text-align:center;"><span style="font-size:22px;">🆚</span><br><b>Batting</b> vs <b>Bowling</b></div>',
#         unsafe_allow_html=True
#     )

# with logo2:
#     try:
#         st.image(team_logos.get(bowlingteam, ""), use_container_width=True)
#     except:
#         pass

# # -------------------- PREDICTION --------------------
# if st.button('Predict Probability'):

#     runs_left = target - score
#     balls_left = 120 - (overs * 6)
#     wickets_left = 10 - wickets
#     currentrunrate = score / overs if overs != 0 else 0
#     requiredrunrate = (runs_left * 6) / balls_left if balls_left != 0 else 0

#     input_df = pd.DataFrame({
#         'batting_team': [battingteam],
#         'bowling_team': [bowlingteam],
#         'city': [city],
#         'runs_left': [runs_left],
#         'balls_left': [balls_left],
#         'wickets': [wickets_left],
#         'total_runs_x': [target],
#         'cur_run_rate': [currentrunrate],
#         'req_run_rate': [requiredrunrate]
#     })

#     result = pipe.predict_proba(input_df)
#     lossprob = result[0][0]
#     winprob = result[0][1]

#     # -------------------- RESULTS CARD --------------------
#     st.markdown('<div class="card">', unsafe_allow_html=True)

#     st.subheader("📌 Match Snapshot")
#     a, b, c, d = st.columns(4)
#     a.metric("Target", int(target))
#     b.metric("Score", int(score))
#     c.metric("Runs Left", int(runs_left))
#     d.metric("Wickets Left", int(wickets_left))

#     st.subheader("📈 Win Probability")
#     left, right = st.columns(2)

#     with left:
#         st.markdown(f"### {battingteam}")
#         st.progress(float(winprob))
#         st.metric("Winning Chance", f"{round(winprob*100)}%")

#     with right:
#         st.markdown(f"### {bowlingteam}")
#         st.progress(float(lossprob))
#         st.metric("Winning Chance", f"{round(lossprob*100)}%")

#     st.markdown("</div>", unsafe_allow_html=True)

#     st.header(battingteam + " - " + str(round(winprob * 100)) + "%")
#     st.header(bowlingteam + " - " + str(round(lossprob * 100)) + "%")
import streamlit as st
import pandas as pd
import pickle

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="IPL Win Probability Predictor",
    page_icon="🏏",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

label {
    color: #e5e7eb !important;
    font-weight: 600;
}

.card {
    background: rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 15px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    background: linear-gradient(90deg, #22c55e, #3b82f6);
    color: white;
    border: none;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown("""
<div class="card">
    <h1>🏏 IPL Win Probability Predictor</h1>
    <p>Predict the winning chances of teams based on current match situation</p>
</div>
""", unsafe_allow_html=True)

# -------------------- MODEL DATA --------------------
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

pipe = pickle.load(open('pipe.pkl', 'rb'))

# -------------------- INPUT SECTION --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📥 Match Details")

col1, col2 = st.columns(2)
with col1:
    battingteam = st.selectbox("Batting Team", sorted(teams))
with col2:
    bowlingteam = st.selectbox("Bowling Team", sorted(teams))

city = st.selectbox("Match City", sorted(cities))
target = st.number_input("Target Score", min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input("Current Score", min_value=0)
with col4:
    overs = st.number_input("Overs Completed", min_value=0.0)
with col5:
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PREDICTION --------------------
if st.button("Predict Win Probability"):

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    currentrunrate = score / overs if overs != 0 else 0
    requiredrunrate = (runs_left * 6) / balls_left if balls_left != 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [battingteam],
        'bowling_team': [bowlingteam],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'cur_run_rate': [currentrunrate],
        'req_run_rate': [requiredrunrate]
    })

    result = pipe.predict_proba(input_df)
    lossprob = result[0][0]
    winprob = result[0][1]

    # -------------------- RESULT DISPLAY --------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Match Prediction Result")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Target", target)
    m2.metric("Score", score)
    m3.metric("Runs Left", runs_left)
    m4.metric("Wickets Left", wickets_left)

    st.subheader("🏆 Winning Probability")

    left, right = st.columns(2)
    with left:
        st.metric(battingteam, f"{round(winprob * 100)}%")
        st.progress(winprob)

    with right:
        st.metric(bowlingteam, f"{round(lossprob * 100)}%")
        st.progress(lossprob)

    st.markdown('</div>', unsafe_allow_html=True)
