import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("meridian_kpis_2024.csv")

fig, ax = plt.subplots(figsize=(11, 6))

segments = [
    ("nrr_enterprise_pct", "Enterprise", "#1a7a3e", "o"),
    ("nrr_midmarket_pct", "Mid-market", "#d4a017", "s"),
    ("nrr_smb_pct", "SMB", "#c0392b", "^"),
]

for col, label, color, marker in segments:
    ax.plot(df["quarter"], df[col], color=color, marker=marker,
            linewidth=2.5, markersize=8, label=label)
    ax.annotate(f"{df[col].iloc[-1]:.0f}%",
                (len(df) - 1, df[col].iloc[-1]),
                textcoords="offset points", xytext=(10, 0),
                color=color, fontsize=11, fontweight="bold", va="center")
    ax.annotate(f"{df[col].iloc[0]:.0f}%",
                (0, df[col].iloc[0]),
                textcoords="offset points", xytext=(-10, 0),
                color=color, fontsize=10, ha="right", va="center")

ax.axhline(100, color="gray", linestyle=":", alpha=0.7, linewidth=1)
ax.text(len(df) - 0.5, 100.8, "100% (no expansion or contraction)",
        ha="right", fontsize=9, color="gray", style="italic")

ax.set_xlabel("Quarter", fontsize=11)
ax.set_ylabel("Net revenue retention (%)", fontsize=11)
ax.set_title("Where the deceleration is coming from: NRR by segment\n"
             "Enterprise is holding; mid-market is plateauing; SMB has fallen below 100%",
             fontsize=13, pad=15)
ax.set_ylim(80, 135)
ax.legend(loc="center left", fontsize=11, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df["quarter"], rotation=45, ha="right")

plt.tight_layout()
plt.savefig("nrr_by_segment.png", dpi=150, bbox_inches="tight")
print("Saved nrr_by_segment.png")
print(df[["quarter", "nrr_enterprise_pct", "nrr_midmarket_pct", "nrr_smb_pct"]].to_string(index=False))
