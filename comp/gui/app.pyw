"""OmniVoice TTS — standalone launcher.

The actual UI lives in generate_tab.GenerateTab (so it can also be embedded as
a tab in studio.pyw). Server must be running first:
  cd <omnivoice-dir> && .venv/Scripts/python.exe server/app.py

Launch via gui/launch.bat (uses venv pythonw, no console window).
"""

import sys
import tkinter as tk
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_tab import GenerateTab  # noqa: E402

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OmniVoice TTS")
    root.geometry("820x680")
    root.minsize(620, 520)
    GenerateTab(root).pack(fill="both", expand=True)
    root.mainloop()
