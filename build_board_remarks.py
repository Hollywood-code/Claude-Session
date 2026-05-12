from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("Board Opening Remarks")
run.bold = True
run.font.size = Pt(18)

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_run = subtitle.add_run("Catherine Park, CEO  •  Annual Strategic Review  •  ~5 minutes")
sub_run.italic = True
sub_run.font.size = Pt(11)
sub_run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_paragraph()

h = doc.add_paragraph()
h_run = h.add_run("Headline")
h_run.bold = True
h_run.font.size = Pt(13)
hl = doc.add_paragraph()
hl_run = hl.add_run(
    "Meridian is a healthy company with a decelerating growth story, and 2026 is "
    "the year we decide whether to defend that or break it."
)
hl_run.italic = True
hl_run.font.size = Pt(12)

doc.add_paragraph()

s = doc.add_paragraph()
s_run = s.add_run("Where we stand (30 seconds)")
s_run.bold = True
s_run.font.size = Pt(13)
doc.add_paragraph(
    "Good morning. I want to use my five minutes to do three things: tell you "
    "honestly where Meridian stands at the end of my first year, name the three "
    "issues I believe deserve this board's attention, and ask you for one thing."
)
doc.add_paragraph(
    "We closed 2025 at $400 million in revenue, up eleven percent. ARR ended the "
    "year at $413 million. Operating margin expanded to 12.4 percent. Free cash "
    "flow margin 17.8 percent. Cash on hand $463 million, no debt. In absolute "
    "terms these are good numbers. They are also the slowest growth Meridian has "
    "ever reported as a public company."
)

doc.add_paragraph()

i = doc.add_paragraph()
i_run = i.add_run("Three issues the board needs to weigh in on")
i_run.bold = True
i_run.font.size = Pt(13)

p1 = doc.add_paragraph()
p1.add_run("1. The deceleration is structural, not transitory. ").bold = True
p1.add_run(
    "Revenue grew 28% in 2022, 19% in 2023, 16% in 2024, and 11% in 2025. Our "
    "2026 guide of 10-14% concedes the trend continues. Overall NRR has "
    "compressed from 114% to 109%; CAC payback has lengthened from 18 to 22 "
    "months; magic number is now 0.92, down from 1.20. We are trading growth "
    "for margin discipline (see chart below). This is a deliberate choice. It "
    "deserves a deliberate board conversation."
)

p2 = doc.add_paragraph()
p2.add_run("2. The AI window is open, and it is closing. ").bold = True
p2.add_run(
    "We GA'd Copilot in September after an 18-month delay. We closed Helio Labs "
    "in November - 28 engineers, $10M cash plus $68M retention equity over four "
    "years, compressing our roadmap an estimated 15 months. Copilot paying seats "
    "went from zero to 710 in three quarters, with a 44% attach rate on Q4 "
    "enterprise renewals. Those are real proof points. But Asana shipped their "
    "full agent suite in November and is bundling it into the standard tier. "
    "Monday is now larger than us by ARR. Atlassian launched agentic Jira last "
    "week and will be in our enterprise deals directly. The window to be a "
    "credible AI-native enterprise platform is measured in quarters, not years."
)

p3 = doc.add_paragraph()
p3.add_run("3. The fragile asset is mid-market, not SMB. ").bold = True
p3.add_run(
    "Enterprise (40% of ARR) is healthy: 21% YoY growth, NRR 125%, 2.6% logo "
    "churn. SMB (13% of ARR) is in managed decline at NRR 84% - that decision "
    "is made. The asset to defend is mid-market: 47% of ARR, NRR compressed "
    "from 108% to 102% in eight quarters, customers pushing for price holds "
    "and Copilot bundled at no cost. If mid-market NRR crosses below 100%, our "
    "deceleration story becomes a contraction story, and no Investor Day "
    "narrative will fix that."
)

doc.add_paragraph()

c = doc.add_paragraph()
c_run = c.add_run("The chart I'd ask you to remember")
c_run.bold = True
c_run.font.size = Pt(13)

doc.add_picture("growth_vs_margin.png", width=Inches(6.0))
caption = doc.add_paragraph()
caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
cap_run = caption.add_run(
    "YoY revenue growth (red) and operating margin (blue) crossed in Q1 2025. "
    "Companion chart - NRR by segment - in board pre-read appendix (nrr_by_segment.png)."
)
cap_run.italic = True
cap_run.font.size = Pt(9)
cap_run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_paragraph()

a = doc.add_paragraph()
a_run = a.add_run("My one ask of the board")
a_run.bold = True
a_run.font.size = Pt(13)

ask = doc.add_paragraph()
ask.add_run(
    "Before we leave this room, I want alignment on the identity question I "
    "raised on the Q4 call and that I will answer publicly at Investor Day on "
    "March 11: "
)
ask_bold = ask.add_run(
    "is Meridian a project management platform with AI features, or an agentic "
    "work platform with project management as one surface?"
)
ask_bold.bold = True
ask.add_run(
    " The two paths imply different R&D intensity, a different pricing model, "
    "a different sales motion, and different capital allocation in 2026. I have "
    "a recommendation. I need the board's challenge and the board's commitment "
    "before I take it to the Street."
)

doc.add_paragraph()

close = doc.add_paragraph()
close_run = close.add_run(
    "I'll stop there so we have time for the discussion that matters. Thank you."
)
close_run.italic = True

doc.save("board_opening_remarks.docx")
print("Saved board_opening_remarks.docx")
