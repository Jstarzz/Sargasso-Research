"""Recreate original public figures from aggregate CSVs; no private data access."""
from pathlib import Path
import csv
from io import StringIO
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    with (ROOT / "results" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def save_svg(fig, path):
    buffer = StringIO()
    fig.savefig(buffer, format="svg", metadata={"Date": None})
    path.write_text("\n".join(line.rstrip() for line in buffer.getvalue().splitlines()) + "\n",
                    encoding="utf-8", newline="\n")


def main():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.spines.left": False, "axes.titleweight": "bold",
        "svg.hashsalt": "sargasso-research-2026-09-19",
    })
    output = ROOT / "figures"
    output.mkdir(exist_ok=True)
    benchmark = rows("forecast-benchmark.csv")
    values = [float(row["mean_iou"]) for row in benchmark]
    fig, ax = plt.subplots(figsize=(9, 4.2), layout="constrained")
    bars = ax.barh(["Persistence", "Frozen forecast"], values,
                   color=["#8c9eab", "#087e8b"], height=0.48)
    ax.set_xlim(0, 0.65)
    ax.set_xlabel("Mean spatial overlap (IoU)")
    ax.set_title("Historical 48-hour forecast benchmark", loc="left", pad=20)
    ax.bar_label(bars, labels=[f"{value:.4f}" for value in values], padding=8)
    ax.grid(axis="x", alpha=0.15)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    fig.suptitle("228 St. Kitts and Nevis cases · recorded aggregate result",
                 fontsize=10, color="#52616b")
    save_svg(fig, output / "forecast-benchmark.svg")
    fig.savefig(output / "forecast-benchmark.png", dpi=180)
    plt.close(fig)

    audit = rows("coastal-label-audit.csv")
    values = [float(row["inland_fraction_percent"]) for row in audit]
    fig, ax = plt.subplots(figsize=(9, 4.2), layout="constrained")
    bars = ax.bar([row["split"] for row in audit], values,
                  color=["#087e8b", "#399a91", "#78b7a4"], width=0.55)
    ax.set_ylim(0, 50)
    ax.set_ylabel("Positive weak-label pixels classified inland (%)")
    ax.set_title("Coastal label audit", loc="left", pad=20)
    ax.bar_label(bars, labels=[f"{value:.1f}%" for value in values], padding=5)
    ax.grid(axis="y", alpha=0.15)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    fig.suptitle("Geometric ≥100 m inland rule · not detector error or human ground truth",
                 fontsize=10, color="#52616b")
    save_svg(fig, output / "coastal-label-audit.svg")
    fig.savefig(output / "coastal-label-audit.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
