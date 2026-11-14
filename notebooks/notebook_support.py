"""Chart presentation only; SNMP retrieval and storage calculations remain visible SQL."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def theme():
    """Apply readable plotting defaults."""
    sns.set_theme(style="whitegrid", context="notebook", font_scale=1.05)
    plt.rcParams.update(
        {
            "figure.dpi": 130,
            "savefig.dpi": 150,
            "text.parse_math": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def finish(fig, name, title, subtitle):
    """Add synthetic provenance, save a review image and display."""
    fig.suptitle(title, x=0.1, y=0.98, ha="left", fontsize=17, fontweight="bold", color="#243e32")
    fig.text(0.1, 0.92, subtitle, ha="left", fontsize=11, color="#526b5b")
    fig.text(
        0.1,
        0.025,
        "Source: invented storage rows served by a local snmpsim agent · fixed fixture, no device measurements\n"
        "vgi-snmp / pysnmp 7.1.32 through Haybarn / VGI · GiB = 2^30 bytes",
        fontsize=9,
        color="#526b5b",
    )
    fig.subplots_adjust(left=0.21, right=0.96, bottom=0.23, top=0.76)
    folder = Path("validation/charts")
    folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(folder / f"{name}.png", bbox_inches="tight")
    plt.show()
