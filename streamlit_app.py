import streamlit as st

# --- Inject Custom CSS ---
st.markdown("""
    <style>
    h1 { font-size: 2.8em !important; margin-bottom: 0.8em !important; }
    p { font-size: 1.5em !important; line-height: 1.0 !important; margin-bottom: 1.2em !important; }
    h3 { font-size: 1.6em !important; margin-top: 2em !important; margin-bottom: 0.8em !important; }
    .stRadio { margin-top: 0.5em !important; margin-bottom: 2em !important; }
    .stRadio label { font-size: 1.1em !important; line-height: 1.8 !important; margin-bottom: 0.5em !important; }
    .stRadio div[data-testid="stForm"] > div > label > div { font-size: 1.1em !important; }
    .stCheckbox label { font-size: 1.1em !important; line-height: 1.5 !important; }
    .stButton button { font-size: 1.1em !important; padding: 0.75em 1.5em !important; }
    .stAlert { font-size: 1.1em !important; }
    </style>
    """, unsafe_allow_html=True)
# Function to calculate the ODI score
def calculate_odds(user_responses, is_section_8_skipped):
    total_score = 0
    answered_sections = 0

    for i, response_value in enumerate(user_responses):
        if i == 7 and is_section_8_skipped:
            continue 

        if response_value is None:
            st.warning(f"請回答第 {i + 1} 部分 (Please answer Section {i + 1}).")
            return None, None 

        total_score += response_value
        answered_sections += 1

    max_possible = answered_sections * 5
    odi_percentage = (total_score / max_possible) * 100 if max_possible > 0 else 0

    return total_score, odi_percentage
# Streamlit User Interface
st.title("Oswestry Disability Index (ODI)")
st.markdown("請選擇每個部分中對您最合適的選項。您可以選擇跳過第八部分（性生活）。")

# Section descriptions
sections_data = [
    ("第一部份：痛楚程度", ["現在沒有任何痛楚。", "現在只感到輕微的痛楚。", "現在感到中等程度的痛楚。", "現在感到非常痛楚。", "現在的痛楚程度非常嚴重。", "現在感到極度痛楚，痛楚的程度非其他人能夠想像。"]),
    ("第二部份：個人起居（梳洗、穿衣等）", ["我可以如常的照顧自己，不會感到任何額外的痛楚。", "我可以如常的照顧自己，但感到非常痛楚。", "照顧自己時感到痛楚，我需小心及緩慢行動。", "我能應付大部分的起居生活，但需要其他人的一些幫助。", "我每天都需要別人幫助照顧大部份的起居生活。", "我不能夠自己穿衣，梳洗也有困難，只可以臥床休息。"]),
    ("第三部份：提起物件", ["我可以提起很重的物件，而不會造成額外的痛楚。", "我可以提起很重的物件，但會造成額外的痛楚!!!。", "疼痛讓我無法從地面舉起重物，但如果放在方聾的位置，我就可以。（例如：放在桌上）", "疼痛讓我無法舉起重物，但如果放在方聾的位置，我就可以舉起輕到中等重的東西。", "我只能舉起很輕的東西。", "我完全無法舉起或攜提任何東西。"]),
    ("第四部份：走路", ["我不受疼痛阻礙，可以走任何距離。", "疼痛使我無法走超過 1.6 公 M。（大約 4圈大操場）", "疼痛使我無法走超過 400 公尺。（大約 1圈大操場）", "疼痛使我無法走超過 100 公尺。", "我只有依靠柺杖才能走。", "我大部分時間都臥床，無法走到廁所。"]),
    ("第五部份：坐", ["我可以坐任何椅子，想坐多久都可以。", "我只能坐特定椅子，想坐多久都可以。", "疼痛使我無法坐超過 1小時。", "疼痛使我無法坐超過半小時。", "疼痛使我無法坐超過 10 分鐘。", "疼痛使我無法坐著。"]),
    ("第六部份：站", ["我要站多久都可以，不會更痛。", "我要站多久都可以，但會更痛。", "疼痛使我無法站超過 1小時。", "疼痛使我無法站超過半小時。", "疼痛使我無法站超過 10 分鐘。", "疼痛使我無法站著。"]),
    ("第七部份：睡眠", ["我的睡眠從未受到疼痛干擾。", "我的睡眠偶而受到疼痛干擾。", "因為疼痛，睡眠時間少於 6小時。", "因為疼痛，睡眠時間少於 4小時。", "因為疼痛，睡眠時間少於 2小時。", "疼痛使我無法入睡。"]),
    ("第八部份：性生活（如果有的話）", ["我的性生活正常而且不會增加背痛。", "我的性生活正常但會增加背痛。", "我的性生活幾乎正常但背部非常疼痛。", "因為背痛，我的性生活受到嚴重限制。", "因為背痛，我幾乎沒有性生活。", "因為背痛，我完全沒有性生活。"]),
    ("第九部份：社交生活", ["我的社交生活正常而且不會更痛。", "我的社交生活正常但會增加疼痛的程度。", "除了無法從事激烈運動外，身體疼痛對我的社交生活並無明顯影響。", "疼痛限制了我的社交生活，使我不常出門。", "疼痛使我的社交生活侷限在家裡。", "因為疼痛，我沒有社交生活。"]),
    ("第十部份：旅遊", ["我可以到處旅遊不會疼痛。", "我可以到處旅遊但會更痛。", "我可以旅遊超過 2個小時，但疼痛令人不適。", "疼痛限制我只能從事少於 1個小時的旅程。", "疼痛限制我只能從事少於 30 分鐘必要的外出活動。", "除嶺接受治療，疼痛讓我無法外出活動。"])
]
# Initialize session states
if 'user_responses' not in st.session_state:
    st.session_state.user_responses = [None] * len(sections_data)
if 'skip_section_8' not in st.session_state:
    st.session_state.skip_section_8 = False
if 'reset_counter' not in st.session_state:
    st.session_state.reset_counter = 0  # <--- MAGIC KEY TRICK

# Loop through sections
for idx, (title, options) in enumerate(sections_data):
    st.subheader(title) 

    if idx == 7:
        st.session_state.skip_section_8 = st.checkbox(
            "跳過第八部分 (性生活)",
            value=st.session_state.skip_section_8,
            key=f"skip_cb_{idx}_{st.session_state.reset_counter}"  # <--- Added counter to key
        )

    is_current_section_8_and_skipped = (idx == 7 and st.session_state.skip_section_8) 

    # Render radio buttons
    selected_option_str = st.radio(
        "", 
        options,
        index=st.session_state.user_responses[idx], 
        disabled=is_current_section_8_and_skipped, 
        key=f"radio_{idx}_{st.session_state.reset_counter}" # <--- Added counter to key
    )

    # --- Update user responses in session state ---
    if is_current_section_8_and_skipped:
        st.session_state.user_responses[idx] = None
    elif selected_option_str is not None:
        st.session_state.user_responses[idx] = options.index(selected_option_str)
    else:
        st.session_state.user_responses[idx] = None
st.markdown("---") 

col1, col2 = st.columns(2) 

with col1:
    if st.button("計算分數", key="calculate_button"):
        total_score, odi_percentage = calculate_odds(st.session_state.user_responses, st.session_state.skip_section_8)

        if total_score is not None: 
            max_overall_score = 50
            if st.session_state.skip_section_8:
                max_overall_score -= 5 

            st.success(f"總分: {total_score} / {max_overall_score}")
            st.success(f"ODI 百分比: {odi_percentage:.2f}%")

            if odi_percentage <= 20:
                level = "輕微功能障礙 (0% - 20%)"
            elif odi_percentage <= 40:
                level = "中度功能障礙 (21% - 40%)"
            elif odi_percentage <= 60:
                level = "嚴重功能障礙 (41% - 60%)"
            elif odi_percentage <= 80:
                level = "癱瘓 (61% - 80%)"
            else:
                level = "臥床或誇大症狀 (81% - 100%)"
            st.success(f"類別: {level}")

with col2:
    if st.button("清除所有選項", key="clear_button"):
        # Reset lists and states
        st.session_state.user_responses = [None] * len(sections_data)
        st.session_state.skip_section_8 = False
        
        # Increase the counter! This instantly changes ALL widget keys so Streamlit forgets them.
        st.session_state.reset_counter += 1 
        
        st.rerun()
