from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

for section in doc.sections:
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(10)
style.paragraph_format.space_after = Pt(4)

def heading(text, size=12, color=(0x1a, 0x3d, 0x6e)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor(*color)
    return p

def body(text, italic=False, bold=False, size=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.italic = italic
    run.bold = bold
    run.font.size = Pt(size)
    return p

title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
tr = title_p.add_run("Investor Day Positioning Memo")
tr.bold = True
tr.font.size = Pt(16)
tr.font.color.rgb = RGBColor(0x1a, 0x3d, 0x6e)

sub_p = doc.add_paragraph()
sr = sub_p.add_run("Catherine Park, CEO  •  For board pre-read  •  Investor Day, March 11, 2026")
sr.italic = True
sr.font.size = Pt(9)
sr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
sub_p.paragraph_format.space_after = Pt(6)

heading("Executive summary")
body(
    "On March 11, I intend to declare Meridian the enterprise-grade agentic work platform — "
    "built on the most trusted governance infrastructure in the category. This is not a rebrand; "
    "it is a strategic commitment that aligns our R&D, sales motion, pricing, and capital allocation "
    "around a single white-space position no competitor occupies today. Three of four direct "
    "competitors have already moved decisively to agentic language; the fourth (Smartsheet) is "
    "decelerating and is a takeout candidate. Our customers — 18 of 22 enterprise advisory sessions "
    "in the last 90 days — are asking us for exactly the product this positioning describes: "
    "governed agents an audit committee can sign off on. We have the assets (Helio agent framework + "
    "FedRAMP/HIPAA infrastructure), the balance sheet ($506M total liquidity), and the customer "
    "demand to claim this slot. This memo lays out the position, the rationale, the competitive "
    "picture, the risks I own, and three commitments I will make to investors."
)

heading("The position")
pos_p = doc.add_paragraph()
pos_p.paragraph_format.space_after = Pt(2)
run = pos_p.add_run(
    "\"Meridian is the enterprise-grade agentic work platform — built on the most trusted "
    "governance infrastructure in the category.\""
)
run.bold = True
run.italic = True
run.font.size = Pt(11)
run.font.color.rgb = RGBColor(0x1a, 0x7a, 0x3e)

body(
    "Project management is the surface we started with. Agents are how enterprise work gets done "
    "in the next decade. Our differentiator is not the most ambitious agent — it is the agent that "
    "a chief compliance officer can deploy in production."
)

heading("Why this position wins")
why_items = [
    ("Category gravity is agentic.",
     "Asana, Monday, and Atlassian have all moved to agentic positioning in the last six months. "
     "Smartsheet — the only Option A holdout — is growing low-single-digits and is a takeout candidate. "
     "Staying in PM-with-AI is the loser's seat by 2027."),
    ("Customers are asking for the product only we can build.",
     "Governance for AI agents was the #1 enterprise theme in 18 of 22 advisory sessions: auditability, "
     "role-based agent permissions, model selection, data residency. PM competitors have not built this; "
     "AI-native upstarts likely never will. Helio's agent framework plus our existing governance is a "
     "combination no competitor has."),
    ("The white space is real.",
     "No competitor today occupies the agentic-platform + premium-governance quadrant with broad enterprise "
     "reach. Atlassian's Rovo is the nearest, but its governance story is dev-centric. Regulated industries "
     "(banking, pharma, federal) where we already win are the moat."),
    ("We can afford the bet.",
     "$506M total liquidity, $200M undrawn revolver, no debt, 17% FCF margin guided 2026. Option B's "
     "downside case is $550M revenue at 5% growth — still profitable, still cash-generative. The asymmetry "
     "is the right way around."),
]
for label, text in why_items:
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(label + " ")
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10)

heading("Competitive landscape (summary)")

headers = ["", "Asana", "Monday", "Smartsheet", "Atlassian"]
rows = [
    ["AI positioning",
     "PM platform w/ AI built in (soft-agentic)",
     "Work OS, AI as a layer",
     "Enterprise platform you can trust (rejects \"agentic\")",
     "Agentic enterprise platform (Rovo)"],
    ["Pricing posture",
     "Bundled (Advanced+)",
     "Bundled (Pro+)",
     "Base bundled; Compliance Pack +$15/seat",
     "Separate paid; consumption hybrid"],
    ["Latest flagship (last 6 mo.)",
     "Nov 2025: AI Studio bundled",
     "Jan 2026: monday AI Agents GA",
     "Dec 2025: AI Compliance Pack",
     "Jan 2026: Rovo Studio agent builder"],
    ["Closest to Meridian option",
     "B (Agentic)",
     "A in framing / B-lite in execution",
     "A (PM-with-AI)",
     "B (Agentic platform)"],
]

table = doc.add_table(rows=1 + len(rows), cols=len(headers))
table.style = "Light Grid Accent 1"
table.autofit = False
col_widths = [Inches(1.4), Inches(1.45), Inches(1.45), Inches(1.55), Inches(1.55)]
for col_idx, width in enumerate(col_widths):
    for row in table.rows:
        row.cells[col_idx].width = width

for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    p = cell.paragraphs[0]
    run = p.add_run(h)
    run.bold = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), "1a3d6e")
    tc_pr.append(shd)
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

for r_idx, row_data in enumerate(rows, start=1):
    for c_idx, val in enumerate(row_data):
        cell = table.rows[r_idx].cells[c_idx]
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(val)
        run.font.size = Pt(8.5)
        if c_idx == 0:
            run.bold = True
        cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP

ref_p = doc.add_paragraph()
ref_p.paragraph_format.space_before = Pt(4)
ref_p.paragraph_format.space_after = Pt(2)
rr = ref_p.add_run(
    "See positioning_matrix.png (embedded below) and competitive_landscape.docx for the full 8-dimension comparison."
)
rr.italic = True
rr.font.size = Pt(8.5)
rr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

try:
    doc.add_picture("positioning_matrix.png", width=Inches(5.6))
    last_para = doc.paragraphs[-1]
    last_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
except Exception as e:
    body(f"[positioning_matrix.png could not be embedded: {e}]", italic=True)

heading("Three risks I own")
risks = [
    ("Revenue air gap.",
     "Mid-market (47% of ARR, NRR 102%) is fragile while agentic revenue is small ($3.5M ARR). "
     "If PM gets maintenance-only investment before agentic compounds, Q2 2026 earnings becomes "
     "the durable narrative. Mitigation: bundle a Copilot baseline into mid-market standard tier "
     "on the same day as Investor Day."),
    ("Model lab disintermediation.",
     "If Anthropic or OpenAI ship native enterprise agent governance (audit, RBAC, model pinning), "
     "our moat compresses. Mitigation: public multi-model neutrality, vertical depth as the second moat."),
    ("Helio retention cliff.",
     "$68M retention equity vests through 2029; 2026 cash-comp cliff is the inflection. Mitigation: "
     "give the team genuine roadmap autonomy on the agent platform — Option B does exactly this."),
]
for label, text in risks:
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(label + " ")
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10)

heading("Three commitments to investors on March 11")
commitments = [
    ("Quarterly Copilot KPIs starting Q1 2026.",
     "Paying seats, ARR contribution, attach rate on enterprise renewals, and in-product usage of "
     "agentic actions — reported publicly each quarter."),
    ("Mid-market pricing redesign announced the same day.",
     "Baseline Copilot bundled into mid-market standard tier; consumption pricing on the agent "
     "platform rolled out H2 2026. Removes the renewal headwind."),
    ("Model neutrality, in writing.",
     "Meridian will not sign exclusive strategic partnerships with any model lab. BYO-model is "
     "the default. Customer optionality is the principle."),
]
for label, text in commitments:
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(label + " ")
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10)

doc.save("investor_day_positioning_memo.docx")
print("Saved investor_day_positioning_memo.docx")
