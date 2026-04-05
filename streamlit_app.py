import streamlit as st

# --- Inject Custom CSS at the very beginning ---
st.markdown("""
    <style>
    /* Global font size adjustments and spacing */

    /* Main title (st.title) */
    h1 {
        font-size: 2.8em !important; /* Larger font for main title */
        margin-bottom: 0.8em !important;
    }

    /* Introductory paragraph */
    p {
        font-size: 1.5em !important; /* Slightly larger text for general paragraphs */
        line-height: 1.0 !important; /* Increase line spacing for readability */
        margin-bottom: 1.2em !important; /* More space after paragraphs */
    }

    /* Section subheaders (st.subheader) */
    h3 {
        font-size: 1.6em !important; /* Larger font for section titles */
        margin-top: 2em !important; /* More space before each new section heading */
        margin-bottom: 0.8em !important; /* Small space after subheader, before options */
    }

    /* Streamlit radio button group container */
    .stRadio {
        margin-top: 0.5em !important; /* Small space between subheader and radio options */
        margin-bottom: 2em !important; /* Significantly more space *after* each radio group to separate sections */
    }

    /* Individual radio button labels/options */
    .stRadio label {
        font-size: 1.1em !important; /* Larger font for radio options */
        line-height: 1.8 !important; /* Increase line spacing for radio options */
        margin-bottom: 0.5em !important; /* Space between individual radio options */
    }

    /* Specifically target the text within the radio options if the above isn't enough
       (Streamlit's internal class names can change, so this might need adjustment) */
    .stRadio div[data-testid="stForm"] > div > label > div { /* A more specific selector if needed */
        font-size: 1.1em !important;
    }

    /* Make the checkbox for skipping section 8 a bit larger */
    .stCheckbox label {
        font-size: 1.1em !important;
        line-height: 1.5 !important;
    }

    /* Adjust button font size */
    .stButton button {
        font-size: 1.1em !important;
        padding: 0.75em 1.5em !important; /* Increase button padding for better click area */
    }

    /* Adjust warning/success messages */
    .stAlert {
        font-size: 1.1em !important;
    }

    </style>
    """, unsafe_allow_html=True)

# Function to calculate the ODI score based on user input
def calculate_odds(user_responses, is_section_8_skipped):
    total_score = 0
    answered_sections = 0

    for i, response_value in enumerate(user_responses):
        # Section 8 is at index 7 (0-indexed)
        if i == 7 and is_section_8_skipped:
            continue # Don't count or check this section if it's skipped

        if response_value is None:
            # If an unskipped section is not answered, show a warning
            st.warning(f"Please answer Section {i + 1}.")
            return None, None # Indicate an incomplete questionnaire

        total_score += response_value
        answered_sections += 1

    max_possible = answered_sections * 5
    # Avoid division by zero if no sections are answered (shouldn't happen with warnings)
    odi_percentage = (total_score / max_possible) * 100 if max_possible > 0 else 0

    return total_score, odi_percentage

# Streamlit User Interface
st.title("Oswestry Disability Index (ODI)")
st.markdown("請選擇每個部分中對您最合適的選項。您可以選擇跳過第八部分（性生活）。") # This markdown will now use the new 'p' styles

# Section descriptions for parts 1 to 5
sections_data = [
    ("第一部份：疼痛程度", [
        "我現在不痛。",
        "我現在的疼痛非常輕微。",
        "我現在的疼痛中等程度。",
        "我現在的疼痛相當嚴重。",
        "我現在的疼痛非常嚴重。",
        "我現在的疼痛已無法形容。"
    ]),
    ("第二部份：自我照顧（例如洗澡、穿衣服等）", [
        "我可以自我照顧，不會更痛。",
        "我可以自我照顧，但覺得很痛。",
        "自我照顧時很痛，我的動作需小心緩慢進行。",
        "大部分自我照顧都可以自己來，但需要一些協助。",
        "每天的自我照顧大部分都需要協助。",
        "我無法自己穿衣服，洗澡有困難，我都躺在床上。"
    ]),
    ("第三部份：抬舉物品", [
        "我可以舉起重物，不會更痛。",
        "我可以舉起重物，但會更痛。",
        "疼痛讓我無法從地面舉起重物，但如果放在方聾的位置，我就可以。（例如：放在桌上）",
        "疼痛讓我無法舉起重物，但如果放在方聾的位置，我就可以舉起輕到中等重的東西。",
        "我只能舉起很輕的東西。",
        "我完全無法舉起或攜提任何東西。"
    ]),
    ("第四部份：走路", [
        "我不受疼痛阻礙，可以走任何距離。",
        "疼痛使我無法走超過 1.6 公 M。（大約 4圈大操場）",
        "疼痛使我無法走超過 400 公尺。（大約 1圈大操場）",
        "疼痛使我無法走超過 100 公尺。",
        "我只有依靠柺杖才能走。",
        "我大部分時間都臥床，無法走到廁所。"
    ]),
    ("第五部份：坐", [
        "我可以坐任何椅子，想坐多久都可以。",
        "我只能坐特定椅子，想坐多久都可以。",
        "疼痛使我無法坐超過 1小時。",
        "疼痛使我無法坐超過半小時。",
        "疼痛使我無法坐超過 10 分鐘。",
        "疼痛使我無法坐著。"
    ]),
]
# Section descriptions for parts 6 to 10
sections_data.extend([
    ("第六部份：站", [
        "我要站多久都可以，不會更痛。",
        "我要站多久都可以，但會更痛。",
        "疼痛使我無法站超過 1小時。",
        "疼痛使我無法站超過半小時。",
        "疼痛使我無法站超過 10 分鐘。",
        "疼痛使我無法站著。"
    ]),
    ("第七部份：睡眠", [
        "我的睡眠從未受到疼痛干擾。",
        "我的睡眠偶而受到疼痛干擾。",
        "因為疼痛，睡眠時間少於 6小時。",
        "因為疼痛，睡眠時間少於 4小時。",
        "因為疼痛，睡眠時間少於 2小時。",
        "疼痛使我無法入睡。"
    ]),
    ("第八部份：性生活（如果有的話）", [
        "我的性生活正常而且不會增加背痛。",
        "我的性生活正常但會增加背痛。",
        "我的性生活幾乎正常但背部非常疼痛。",
        "因為背痛，我的性生活受到嚴重限制。",
        "因為背痛，我幾乎沒有性生活。",
        "因為背痛，我完全沒有性生活。"
    ]),
    ("第九部份：社交生活", [
        "我的社交生活正常而且不會更痛。",
        "我的社交生活正常但會增加疼痛的程度。",
        "除了無法從事激烈運動外，身體疼痛對我的社交生活並無明顯影響。",
        "疼痛限制了我的社交生活，使我不常出門。",
        "疼痛使我的社交生活侷限在家裡。",
        "因為疼痛，我沒有社交生活。"
    ]),
    ("第十部份：旅遊", [
        "我可以到處旅遊不會疼痛。",
        "我可以到處旅遊但會更痛。",
        "我可以旅遊超過 2個小時，但疼痛令人不適。",
        "疼痛限制我只能從事少於 1個小時的旅程。",
        "疼痛限制我只能從事少於 30 分鐘必要的外出活動。",
        "除嶺接受治療，疼痛讓我無法外出活動。"
    ]),
])
# Initialize session state for user responses and skip flag
if 'user_responses' not in st.session_state:
    st.session_state.user_responses = [None] * len(sections_data)
if 'skip_section_8' not in st.session_state:
    st.session_state.skip_section_8 = False
# Loop through sections to create input options
for idx, (title, options) in enumerate(sections_data):
    st.subheader(title) # Display the title as a subheader

    # --- Handle "Skip Section 8" checkbox placement and logic ---
    # Section 8 is at index 7 (0-indexed)
    if idx == 7:
        st.session_state.skip_section_8 = st.checkbox(
            "跳過第八部分 (性生活)",
            value=st.session_state.skip_section_8,
            key=f"skip_cb_{idx}" # Unique key for the checkbox
        )

    # Determine if the current section's radio buttons should be disabled
    is_current_section_8_and_skipped = (idx == 7 and st.session_state.skip_section_8) # Corrected variable name

    # Determine initial selection for the radio button from session state
    current_selected_index = None
    if st.session_state.user_responses[idx] is not None:
        current_selected_index = st.session_state.user_responses[idx]

    # Render radio buttons for the current section
    # Use an empty string "" as the label for st.radio
    # because the title is already displayed by st.subheader(title)
    selected_option_str = st.radio(
        "", # <--- Empty label here
        options,
        index=current_selected_index, # Pre-select from session state if available
        disabled=is_current_section_8_and_skipped, # Disable if Section 8 is skipped
        key=f"radio_{idx}" # Unique key for each radio group
    )

    # --- Update user responses in session state ---
    if is_current_section_8_and_skipped:
        st.session_state.user_responses[idx] = None # Ensure response is None if section is skipped
    elif selected_option_str is not None:
        # If an option is selected and the section is not skipped, store its index (score)
        st.session_state.user_responses[idx] = options.index(selected_option_str)
    else:
        # If no option is selected (e.g., initial load), ensure it's None
        st.session_state.user_responses[idx] = None

st.markdown("---") # Visual separator for clarity - this also gets some default margin

col1, col2 = st.columns(2) # Use columns to place buttons side-by-side

with col1:
    if st.button("計算分數", key="calculate_button"):
        # Pass the user responses and the skip flag to the calculation function
        total_score, odi_percentage = calculate_odds(st.session_state.user_responses, st.session_state.skip_section_8)

        if total_score is not None: # Only display if a valid score was returned (no incomplete sections)
            # Calculate the maximum possible score, adjusting for skipped Section 8 if applicable
            max_overall_score = len(sections_data) * 5
            if st.session_state.skip_section_8:
                max_overall_score -= 5 # Subtract 5 points if Section 8 was skipped

            st.success(f"總分: {total_score} / {max_overall_score}")
            st.success(f"ODI 百分比: {odi_percentage:.2f}%")

            # Determine category based on ODI percentage
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

if st.button("清除所有選項", key="clear_button"):
    try:
        st.session_state.user_responses = [None] * len(sections_data)  # Reset all responses to None
        st.session_state.skip_section_8 = False  # Also reset the skip checkbox state
        st.experimental_rerun()  # Force a rerun to clear all input fields in the UI
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")  # Display the error message in the app

