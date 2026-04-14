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
    ("第一項：痛楚程度", ["現在沒有任何痛楚。", "現在只感到輕微的痛楚。", "現在感到中等程度的痛楚。", "現在感到非常痛楚。", "現在的痛楚程度非常嚴重。", "現在感到極度痛楚，痛楚的程度非其他人能夠想像。"]),
    ("第二部份：個人起居（梳洗、穿衣等）", ["我可以如常的照顧自己，不會感到任何額外的痛楚。", "我可以如常的照顧自己，但感到非常痛楚。", "照顧自己時感到痛楚，我需小心及緩慢行動。", "我能應付大部分的起居生活，但需要其他人的一些幫助。", "我每天都需要別人幫助照顧大部份的起居生活。", "我不能夠自己穿衣，梳洗也有困難，只可以臥床休息。"]),
    ("第三部份：提起物件", ["我可以提起很重的物件，而不會造成額外的痛楚。", "我可以提起很重的物件，但會造成額外的痛楚。", "疼痛使我不能從地上提起很重的物件，但假如物件放在一個適當的位置，我仍可以拿起。", "疼痛使我不能提起很重的物件，但假如物件放在一個適當的位置，我可以拿起一些輕便或不太重的物件。", "我只可以提起一些非常輕的物件。", "我根本不能提起任何物件。"]),
    ("第四部份：步行", ["疼痛不會影響我步行多少路程。", "疼痛使我不能步行多過一小時。", "疼痛使我不能步行多過半小時。", "疼痛使我不能步行多過十五分鐘。", "我需要用拐杖行路。", "我大部份時間臥床，只能爬去洗手間。"]),
    ("第五部份：坐下", ["我可以坐在任何座椅上多久也沒有問題。", "我可以坐在慣常的座椅上多久也沒有問題。", "疼痛使我不能坐超過一小時。", "疼痛使我不能坐超過半小時。", "疼痛使我不能坐超過十五分鐘。", "疼痛使我根本不能坐下。"]),
    ("第六部份：站立", ["我可以站久也不會造成任何額外的痛楚。", "我可以站很久，但會有額外的痛楚。", "疼痛使我不能站立超過一小時。", "疼痛使我不能站立超過半小時。", "疼痛使我不能站立超過十分鐘。", "疼痛使我完全不能站立。"]),
    ("第七部份：睡眠", ["疼痛從不影響我的睡眠。", "有時候疼痛影響我的睡眠。", "疼痛使我不能睡眠超過六小時。", "疼痛使我不能睡眠超過四小時。", "疼痛使我不能睡眠超過兩小時。", "疼痛使我根本不能入睡。"]),
    ("第八部份：性生活（註：如沒有性生活，毋須填寫此欄）", ["我的性生活正常，沒有任何額外的痛楚。", "我的性生活正常，但有點額外的痛楚。", "我的性生活正常，但非常疼痛。", "痛楚嚴重限制了我的性生活。", "由於痛楚關係，我差不多沒有性生活。", "痛楚使我完全不能有性生活。"]),
    ("第九部份：社交生活", ["我的社交生活正常，沒有引起任何額外的痛楚。", "我的社交生活正常，但會增加痛楚的程度。", "疼痛不太影響我的社交生活，但使我不能作一些較劇烈的活動，例如運動等。", "疼痛限制了我的社交生活，使我不能經常外出活動。", "疼痛限制了我的社交生活，我只能留在家裡活動。", "由於痛楚的關係，我根本沒有任何社交生活。"]),
    ("第十部份：舟車勞頓", ["我可以去任何地方，而旅途上的勞頓不會引起任何痛楚。", "我可以去任何地方，但旅途上的勞頓造成額外的痛楚。", "雖然很痛，但我仍可作多於兩小時的旅程。", "痛楚使我只可以作不超過一小時的旅程。", "痛楚使我只可以作少於三十分鐘的短途旅程。", "除了外出接受治療，疼痛使我不能有任何的舟車勞頓。"])
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
