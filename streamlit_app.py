import streamlit as st


# Function to calculate the ODI score based on user input
def calculate_odds(user_responses, skip_section_8):
    total_score = 0
    answered_sections = 0

    for i, response in enumerate(user_responses):
        if i == 7 and skip_section_8:  # Skip Section 8
            continue
        if response is None:
            st.warning(f"Please answer Section {i + 1}.")
            return None, None
        total_score += response
        answered_sections += 1

    max_possible = answered_sections * 5
    odi_percentage = (total_score / max_possible) * 100 if max_possible > 0 else 0

    return total_score, odi_percentage


# Streamlit User Interface
st.title("Oswestry Disability Index (ODI)")

# Section descriptions
sections = [
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
        "疼痛讓我無法從地面舉起重物，但如果放在方便的位置，我就可以。（例如：放在桌上）",
        "疼痛讓我無法舉起重物，但如果放在方聾的位置，我就可以舉起輕到中等重的東西。",
        "我只能舉起很輕的東西。",
        "我完全無法舉起或攜提任何東西。"
    ]),
    ("第四部份：走路", [
        "我不受疼痛阻礙，可以走任何距離。",
        "疼痛使我無法走超過 1.6 公里。（大約 4圈大操場）",
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
    ("第六部份：站", [
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
        "除了接受治療，疼痛讓我無法外出活動。"
    ]),
]

user_responses = []  # To store the user's responses
skip_section_8 = st.checkbox("Skip Section 8 (Social Life)")

# Loop through sections to create input options
for title, options in sections:
    st.subheader(title)
    response = st.radio(title, options)
    user_responses.append(options.index(response) if response else None)

if st.button("Calculate Score"):
    total_score, odi_percentage = calculate_odds(user_responses, skip_section_8)
    if total_score is not None:  # Only display if valid score was calculated
        st.success(f"Total Score: {total_score}")
        st.success(f"ODI Percentage: {odi_percentage:.2f}%")

if st.button("Clear All Selections"):
    user_responses = [None] * len(sections)  # Reset responses
    st.experimental_rerun()  # Rerun the app to reset input fields




