
import tkinter as tk
from tkinter import messagebox

def calculate_result(user_vars, skip_social_var):
    total_score = 0
    answered_sections = 0
    skip = bool(skip_social_var.get())

    for i, var in enumerate(user_vars):
        if i == 7 and skip:  # section 8 skipped
            continue
        val = var.get()
        if val == -1:
            messagebox.showwarning("Incomplete", f"Please answer Section {i+1} (or mark Section 8 skipped).")
            return
        total_score += val
        answered_sections += 1

    max_possible = answered_sections * 5 if answered_sections > 0 else 1
    odi_percentage = (total_score / max_possible) * 100

    if odi_percentage <= 20:
        level = "Minimal disability (0% - 20%)"
    elif odi_percentage <= 40:
        level = "Moderate disability (21% - 40%)"
    elif odi_percentage <= 60:
        level = "Severe disability (41% - 60%)"
    elif odi_percentage <= 80:
        level = "Crippled (61% - 80%)"
    else:
        level = "Bed-bound or exaggerating symptoms (81% - 100%)"

    messagebox.showinfo(
        "ODI Result",
        f"Total Score: {total_score} / {max_possible}\n"
        f"ODI Percentage: {odi_percentage:.2f}%\n"
        f"Category: {level}"
    )

def clear_all(user_vars, skip_social_var):
    for v in user_vars:
        v.set(-1)
    skip_social_var.set(0)
def main():
    root = tk.Tk()
    root.title("Electronic Oswestry Disability Index (ODI)")
    root.geometry("900x700")

    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    

    frame = tk.Frame(canvas)
    scrollable_frame = frame
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    tk.Label(scrollable_frame, text="Oswestry Disability Index (ODI)", font=("Arial", 24, "bold")).pack(pady=10)
    tk.Label(scrollable_frame, text="Select one option per section. You may skip Section 8 (Social Life).",
             font=("Arial", 24), wraplength=800, justify="center").pack(pady=5)

    questionnaire_sections = [
        {"title": "第一部份：疼痛程度", "options": [
            "我現在不痛。",
            "我現在的疼痛非常輕微。",
            "我現在的疼痛中等程度。.",
            "我現在的疼痛相當嚴重。",
            "我現在的疼痛非常嚴重。",
            "我現在的疼痛已無法形容。"]},
        {"title": "第二部份：自我照顧（例如洗澡、穿衣服等）", "options": [
            "我可以自我照顧，不會更痛。",
            "我可以自我照顧，但覺得很痛。",
            "自我照顧時很痛，我的動作需小心緩慢進行。",
            "大部分自我照顧都可以自己來，但需要一些協助。",
            "每天的自我照顧大部分都需要協助。",
            "我無法自己穿衣服，洗澡有困難，我都躺在床上。"]},
        {"title": "第三部份：抬舉物品", "options": [
            "我可以舉起重物，不會更痛。",
            "我可以舉起重物，但會更痛。",
            "疼痛讓我無法從地面舉起重物，但如果放在方便的位置，我就可以。（例如：放在桌上）",
            "疼痛讓我無法舉起重物，但如果放在方便的位置，我就可以舉起輕到中等重的東西。",
            "我只能舉起很輕的東西。",
            "我完全無法舉起或攜提任何東西。"]},
        {"title": "第四部份：走路", "options": [
            "我不受疼痛阻礙，可以走任何距離。",
            "疼痛使我無法走超過 1.6 公里。（大約 4圈大操場）",
            "疼痛使我無法走超過 400 公尺。（大約 1圈大操場）",
            "疼痛使我無法走超過 100 公尺。",
            "我只有依靠柺杖才能走。",
            "我大部分時間都臥床，無法走到廁所。"]},
        {"title": "第五部份：坐", "options": [
            "我可以坐任何椅子，想坐多久都可以。",
            "我只能坐特定椅子，想坐多久都可以。",
            "疼痛使我無法坐超過 1小時。",
            "疼痛使我無法坐超過半小時",
            "疼痛使我無法坐超過 10 分鐘。",
            "疼痛使我無法坐著。"]},
        {"title": "第六部份：站", "options": [
            "我要站多久都可以，不會更痛。",
            "我要站多久都可以，但會更痛。",
            "疼痛使我無法站超過 1小時。",
            "疼痛使我無法站超過半小時。",
            "疼痛使我無法站超過 10 分鐘。",
            "疼痛使我無法站著。"]},
        {"title": "第七部份：睡眠 ", "options": [
            "我的睡眠從未受到疼痛干擾。 ",
            "我的睡眠偶而受到疼痛干擾。",
            "因為疼痛，睡眠時間少於 6小時。",
            "因為疼痛，睡眠時間少於 4小時",
            "因為疼痛，睡眠時間少於 2小時。",
            "疼痛使我無法入睡。"]},
        {"title": "第八部份：性生活 （如果有的話）", "options": [
            "我的性生活正常而且不會增加背痛。",
            "我的性生活正常但會增加背痛。 ",
            "我的性生活幾乎正常但背部非常疼痛。",
            "因為背痛，我的性生活受到嚴重限制。",
            "因為背痛，我幾乎沒有性生活。",
            "因為背痛，我完全沒有性生活。"]},
        {"title": "第九部份：社交生活", "options": [
            "我的社交生活正常而且不會更痛。",
            "我的社交生活正常但會增加疼痛的程度。",
            "除了無法從事激烈運動外，身體疼痛對我的社交生活並無明顯影響",
            "疼痛限制了我的社交生活，使我不常出門。",
            "疼痛使我的社交生活侷限在家裡。",
            "因為疼痛，我沒有社交生活。 "]},
        {"title": "第十部份：旅遊", "options": [
            "我可以到處旅遊不會疼痛。",
            "我可以到處旅遊但會更痛。",
            "我可以旅遊超過 2個小時，但疼痛令人不適。",
            "疼痛限制我只能從事少於 1個小時的旅程。 ",
            "疼痛限制我只能從事少於 30 分鐘必要的外出活動。",
            "除了接受治療，疼痛讓我無法外出活動。"]}
    ]

    user_vars = [tk.IntVar(value=-1) for _ in questionnaire_sections]
    skip_social_var = tk.IntVar(value=0)
    for idx, q in enumerate(questionnaire_sections):
        box = tk.LabelFrame(scrollable_frame, text=q["title"], font=("Arial", 24, "bold"), padx=10, pady=6)
        box.pack(fill="x", padx=20, pady=8)

        if idx == 7:
            def on_skip(var=user_vars[7], skip=skip_social_var):
                if skip.get() == 1:
                    var.set(-1)
            skip_cb = tk.Checkbutton(box, text="Skip this section", variable=skip_social_var, command=on_skip)
            skip_cb.pack(anchor="ne")

        row_frame = tk.Frame(box)
        row_frame.pack(fill="x")
        opts_frame = tk.Frame(row_frame)
        opts_frame.pack(side="left", fill="x", expand=True)

        for val, desc in enumerate(q["options"]):
            rb = tk.Radiobutton(opts_frame, text=desc, variable=user_vars[idx], value=val,
                                wraplength=760, justify="left", anchor="w", font=("Arial", 24) )
            rb.pack(anchor="w", padx=4, pady=1)

        clear_btn = tk.Button(row_frame, text="Clear", command=lambda v=user_vars[idx]: v.set(-1))
        clear_btn.pack(side="right", padx=6, pady=6)
    btn_frame = tk.Frame(scrollable_frame)
    btn_frame.pack(pady=12)

    calc_btn = tk.Button(btn_frame, text="Calculate Score", bg="#4CAF50", fg="red",
                         command=lambda: calculate_result(user_vars, skip_social_var))
    calc_btn.grid(row=0, column=0, padx=8)

    clear_all_btn = tk.Button(btn_frame, text="Clear All Selections", bg="#f44336", fg="black",
                              command=lambda: clear_all(user_vars, skip_social_var))
    clear_all_btn.grid(row=0, column=1, padx=8)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    root.bind_all("<MouseWheel>", _on_mousewheel)

    root.mainloop()

if __name__ == "__main__":
    main()
