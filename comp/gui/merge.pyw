"""OmniVoice Auto Cut & Merge — standalone launcher.

The actual UI lives in merge_tab.MergeTab (also embedded as a tab in studio.pyw).

Launch via gui/merge.bat (venv pythonw, no console window).
"""

import sys
import tkinter as tk
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from merge_tab import MergeTab  # noqa: E402

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OmniVoice — Auto Cut & Merge")
    root.geometry("860x560")
    root.minsize(680, 460)
    MergeTab(root).pack(fill="both", expand=True)
    root.mainloop()
