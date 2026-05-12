import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("meridian_financials_2022_2025.csv")
df["yoy_growth_pct"] = df["revenue_usd_m"].pct_change(periods=4) * 100

plot_df = df.dropna(subset=["yoy_growth_pct"]).reset_index(drop=True)

fig, ax1 = plt.subplots(figsize=(11, 6))

color_growth = "#c0392b"
ax1.plot(plot_df["quarter"], plot_df["yoy_growth_pct"],
         color=color_growth, marker="o", linewidth=2.5, label="YoY revenue growth (%)")
ax1.set_xlabel("Quarter", fontsize=11)
ax1.set_ylabel("YoY revenue growth (%)", color=color_growth, fontsize=11)
ax1.tick_params(axis="y", labelcolor=color_growth)
ax1.set_ylim(0, 25)

for x, y in zip(plot_df["quarter"], plot_df["yoy_growth_pct"]):
    ax1.annotate(f"{y:.1f}%", (x, y), textcoords="offset points",
                 xytext=(0, 10), ha="center", color=color_growth, fontsize=9)

ax2 = ax1.twinx()
color_margin = "#2c7fb8"
ax2.plot(plot_df["quarter"], plot_df["operating_margin_pct"],
         color=color_margin, marker="s", linewidth=2.5, label="Operating margin (%)")
ax2.set_ylabel("Operating margin (%)", color=color_margin, fontsize=11)
ax2.tick_params(axis="y", labelcolor=color_margin)
ax2.set_ylim(0, 25)

for x, y in zip(plot_df["quarter"], plot_df["operating_margin_pct"]):
    ax2.annotate(f"{y:.1f}%", (x, y), textcoords="offset points",
                 xytext=(0, -15), ha="center", color=color_margin, fontsize=9)

catherine_q = "2025Q1"
if catherine_q in plot_df["quarter"].values:
    idx = plot_df.index[plot_df["quarter"] == catherine_q][0]
    ax1.axvline(idx, color="gray", linestyle="--", alpha=0.6)
    ax1.text(idx, 24, "Catherine\nbecomes CEO", ha="center", fontsize=9,
             color="gray", style="italic")

plt.title("Meridian: Growth is decelerating while margin is expanding\n"
          "YoY revenue growth vs. operating margin, 2023Q1–2025Q4",
          fontsize=13, pad=15)
ax1.set_xticks(range(len(plot_df)))
ax1.set_xticklabels(plot_df["quarter"], rotation=45, ha="right")
ax1.grid(True, alpha=0.25)

fig.tight_layout()
plt.savefig("growth_vs_margin.png", dpi=150, bbox_inches="tight")
print("Saved growth_vs_margin.png")
print(plot_df[["quarter", "yoy_growth_pct", "operating_margin_pct"]].to_string(index=False))
