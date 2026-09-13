"""OmniVoice Reference Clip Maker — standalone launcher.

The actual UI lives in refmaker_tab.RefMakerTab (so it can also be embedded as
a tab in studio.pyw). Produces the ref_audio clips that the TTS generator
clones from.

Launch via gui/refmaker.bat (venv pythonw, no console window).
"""

import sys
import tkinter as tk
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from refmaker_tab import RefMakerTab  # noqa: E402

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OmniVoice — Reference Clip Maker")
    root.geometry("860x620")
    root.minsize(680, 520)
    RefMakerTab(root).pack(fill="both", expand=True)
    root.mainloop()
