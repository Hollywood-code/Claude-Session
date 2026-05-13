import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

competitors = [
    ("Smartsheet",            1.4, 3.9, "#7f8c8d", False),
    ("Monday.com",            2.4, 1.0, "#e67e22", False),
    ("Asana",                 3.5, 1.4, "#d4a017", False),
    ("Atlassian (Rovo)",      4.4, 4.0, "#2c7fb8", False),
    ("Meridian today",        2.0, 3.4, "#c0392b", True),
    ("Meridian proposed",     4.2, 4.3, "#1a7a3e", True),
]

fig, ax = plt.subplots(figsize=(11, 8))

ax.axvline(3.0, color="gray", linestyle="--", alpha=0.5, linewidth=1)
ax.axhline(2.5, color="gray", linestyle="--", alpha=0.5, linewidth=1)

ax.fill_between([3.0, 5.0], 2.5, 5.0, color="#1a7a3e", alpha=0.06)
ax.text(4.0, 4.85, "WHITE SPACE\nAgentic + premium governance",
        ha="center", va="top", fontsize=10, color="#1a7a3e",
        fontstyle="italic", fontweight="bold")

for name, x, y, color, is_meridian in competitors:
    size = 480 if is_meridian else 320
    edge = "black" if is_meridian else "white"
    ew = 2 if is_meridian else 1
    ax.scatter(x, y, s=size, c=color, edgecolors=edge,
               linewidths=ew, zorder=5, alpha=0.92)
    weight = "bold" if is_meridian else "normal"
    fontsize = 11 if is_meridian else 10
    if name == "Meridian today":
        ax.annotate(name, (x, y), xytext=(-12, -8),
                    textcoords="offset points", ha="right",
                    fontsize=fontsize, fontweight=weight, color=color)
    elif name == "Meridian proposed":
        ax.annotate(name, (x, y), xytext=(12, 8),
                    textcoords="offset points", ha="left",
                    fontsize=fontsize, fontweight=weight, color=color)
    else:
        ax.annotate(name, (x, y), xytext=(0, 14),
                    textcoords="offset points", ha="center",
                    fontsize=fontsize, fontweight=weight, color=color)

mer_today = next(c for c in competitors if c[0] == "Meridian today")
mer_prop = next(c for c in competitors if c[0] == "Meridian proposed")
arrow = FancyArrowPatch((mer_today[1], mer_today[2]),
                        (mer_prop[1], mer_prop[2]),
                        arrowstyle="-|>", mutation_scale=22,
                        color="#1a7a3e", linewidth=2,
                        linestyle="-", alpha=0.65, zorder=3)
ax.add_patch(arrow)

ax.text(0.4, 0.4, "PM-with-AI\nBundled\n(Monday)",
        fontsize=9, color="#888", ha="left", va="bottom", fontstyle="italic")
ax.text(0.4, 4.85, "PM-with-AI\nPremium\n(Smartsheet)",
        fontsize=9, color="#888", ha="left", va="top", fontstyle="italic")
ax.text(4.85, 0.4, "Agentic\nBundled\n(Asana)",
        fontsize=9, color="#888", ha="right", va="bottom", fontstyle="italic")

ax.set_xlim(0, 5.2)
ax.set_ylim(0, 5.2)
ax.set_xticks([0.5, 4.7])
ax.set_xticklabels(["PM-centric", "Agentic"], fontsize=11)
ax.set_yticks([0.5, 4.7])
ax.set_yticklabels(["Bundled\npricing", "Premium\npricing"], fontsize=11)
ax.set_xlabel("Product positioning", fontsize=12, labelpad=10)
ax.set_ylabel("Pricing posture", fontsize=12, labelpad=10)
ax.set_title("Competitive Positioning Matrix\n"
             "Meridian's proposed move into the agentic + premium-governance quadrant",
             fontsize=13, pad=14)
ax.grid(True, alpha=0.15)

for spine in ax.spines.values():
    spine.set_edgecolor("#bbb")

plt.tight_layout()
plt.savefig("positioning_matrix.png", dpi=150, bbox_inches="tight")
print("Saved positioning_matrix.png")
